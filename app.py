
from flask import Flask, render_template, request, redirect, url_for
from algoritmo.merge_sort import merge_sort

app = Flask(__name__)

# Publicações fictícias para começar
publicacoes = [
    {
        "autor": "Ana Silva",
        "cargo": "Estudante de Engenharia de Software",
        "texto": "Comecei a estudar algoritmos de ordenação! "
                 "É incrível entender como os dados podem ser organizados.",
        "data": "2026-10-11",
        "curtidas": 12
    },
    {
        "autor": "Pedro Santos",
        "cargo": "Desenvolvedor Python",
        "texto": "Compartilhando meu novo projeto desenvolvido "
                 "com Python e Flask!",
        "data": "2026-10-10",
        "curtidas": 28
    },
    {
        "autor": "Julia Costa",
        "cargo": "Estudante de Tecnologia",
        "texto": "Nunca pare de aprender. Cada pequeno projeto "
                 "é uma oportunidade de evoluir.",
        "data": "2026-10-09",
        "curtidas": 19
    }
]

# Vagas fictícias
vagas = [
    {
        "empresa": "Tech Solutions",
        "cargo": "Estágio em Desenvolvimento Python",
        "local": "Brasília - DF",
        "modalidade": "Híbrido"
    },
    {
        "empresa": "Inova Tecnologia",
        "cargo": "Desenvolvedor(a) Júnior",
        "local": "Remoto",
        "modalidade": "Remoto"
    },
    {
        "empresa": "Data Brasil",
        "cargo": "Estágio em Dados",
        "local": "Brasília - DF",
        "modalidade": "Presencial"
    }
]


@app.route("/")

@app.route("/")
def inicio():
    criterio = request.args.get("ordenar", "data")

    print("Critério escolhido:", criterio)

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

    print("Ordem do feed:")
    for post in publicacoes_ordenadas:
        print(post["autor"], "-", post["curtidas"], "curtidas")

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
        publicacoes.append({
            "autor": autor,
            "cargo": cargo,
            "texto": texto,
            "data": __import__("datetime").date.today().isoformat(),
            "curtidas": 0
        })

    return redirect(url_for(
        "inicio",
        ordenar=request.args.get("ordenar", "data")
    ))


if __name__ == "__main__":
    app.run(debug=True)
