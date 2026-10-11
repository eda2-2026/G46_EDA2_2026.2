
from flask import Flask, render_template, request, redirect, url_for
from algoritmo.merge_sort import merge_sort
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Conecta ao banco de dados
def conectar_banco():
    conexao = sqlite3.connect("conectunb.db")
    conexao.row_factory = sqlite3.Row
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao


@app.route("/")
def inicio():
    criterio = request.args.get("ordenar", "data")

    # Busca as publicações e os dados dos usuários
    conexao = conectar_banco()

    registros = conexao.execute("""
        SELECT
            publicacoes.id,
            usuarios.nome AS autor,
            usuarios.cargo AS cargo,
            publicacoes.texto,
            publicacoes.data,
            publicacoes.curtidas
        FROM publicacoes
        JOIN usuarios
            ON publicacoes.usuario_id = usuarios.id
    """).fetchall()

    # Busca as vagas
    registros_vagas = conexao.execute("""
        SELECT empresa, cargo, local, modalidade, descricao
        FROM vagas
    """).fetchall()

    conexao.close()

    publicacoes = []

    for registro in registros:
        post = dict(registro)
        post["data"] = datetime.fromisoformat(post["data"])
        publicacoes.append(post)

    vagas = [dict(vaga) for vaga in registros_vagas]

    # Ordena usando o Merge Sort
    if criterio == "curtidas":
        publicacoes_ordenadas = merge_sort(
            publicacoes,
            chave=lambda post: post["curtidas"]
        )
    else:
        criterio = "data"
        publicacoes_ordenadas = merge_sort(
            publicacoes,
            chave=lambda post: post["data"]
        )

    return render_template(
        "index.html",
        publicacoes=publicacoes_ordenadas,
        vagas=vagas,
        criterio=criterio
    )


@app.route("/publicar", methods=["POST"])
def publicar():
    autor = request.form.get("autor", "").strip()
    cargo = request.form.get("cargo", "").strip()
    texto = request.form.get("texto", "").strip()

    if autor and cargo and texto:
        conexao = conectar_banco()

        try:
            # Procura o usuário pelo nome e cargo.
            usuario = conexao.execute("""
                SELECT id
                FROM usuarios
                WHERE nome = ? AND cargo = ?
                LIMIT 1
            """, (autor, cargo)).fetchone()

            if usuario is None:
                cursor = conexao.execute("""
                    INSERT INTO usuarios (nome, cargo)
                    VALUES (?, ?)
                """, (autor, cargo))
                usuario_id = cursor.lastrowid
            else:
                usuario_id = usuario["id"]

            # Salva a publicação no banco.
            conexao.execute("""
                INSERT INTO publicacoes
                    (usuario_id, texto, data, curtidas)
                VALUES (?, ?, ?, ?)
            """, (
                usuario_id,
                texto,
                datetime.now().isoformat(timespec="seconds"),
                0
            ))

            conexao.commit()

        finally:
            conexao.close()

    criterio = request.args.get("ordenar", "data")

    return redirect(url_for("inicio", ordenar=criterio))


if __name__ == "__main__":
    app.run(debug=True)
