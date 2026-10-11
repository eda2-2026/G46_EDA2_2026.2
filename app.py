
from flask import Flask, render_template

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
def inicio():
    return render_template(
        "index.html",
        publicacoes=publicacoes,
        vagas=vagas
    )


if __name__ == "__main__":
    app.run(debug=True)
