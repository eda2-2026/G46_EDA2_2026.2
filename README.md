# ConectaUnB 🎓💻

O **ConectaUnB** é um protótipo de uma rede social profissional voltada para a comunidade universitária, inspirado na ideia de conectar estudantes, compartilhar conhecimentos e divulgar oportunidades profissionais.

🌐 **Acesse o projeto:** [https://g46-eda2-2026-2.onrender.com](https://g46-eda2-2026-2.onrender.com) | [https://youtu.be/af6YJ9LMo5o](https://youtu.be/af6YJ9LMo5o)

## 📌 Sobre o projeto

A ideia do ConectaUnB surgiu em uma disciplina anterior de **Requisitos de Software**, na qual foi desenvolvida a proposta de uma plataforma para conectar pessoas da comunidade universitária.

Posteriormente, o projeto foi utilizado na disciplina de **Estrutura de Dados e Algoritmos 2 (EDA2)** para demonstrar, na prática, o funcionamento do algoritmo de ordenação **Merge Sort**.

O sistema apresenta um feed de publicações que pode ser ordenado por data, exibindo as mais recentes primeiro, ou por quantidade de curtidas, exibindo as publicações mais curtidas primeiro.

## 🎯 Objetivo

Demonstrar a aplicação de um algoritmo de ordenação em um contexto prático, utilizando uma aplicação web como interface para visualizar os resultados.

## ⚙️ Tecnologias utilizadas

- **Python** — linguagem de programação.
- **Flask** — framework para desenvolvimento web.
- **Merge Sort** — algoritmo de ordenação das publicações.
- **HTML e CSS** — estrutura e estilização da interface.
- **SQLite** — banco de dados para armazenamento de usuários, publicações e vagas.

## 🔀 Por que utilizar Merge Sort?

O Merge Sort foi escolhido por ser um algoritmo de ordenação eficiente, baseado na estratégia de **divisão e conquista**.

Seu funcionamento consiste em dividir a lista de publicações em partes menores, ordenar essas partes recursivamente e, depois, intercalá-las em uma única lista ordenada.

A complexidade temporal do Merge Sort é **O(n log n)** nos casos melhor, médio e pior, sendo adequado para demonstrar a ordenação de conjuntos de dados maiores.

No ConectaUnB, o algoritmo é utilizado para:

- **Mais recentes:** ordenar as publicações por data e horário, da mais recente para a mais antiga.
- **Mais curtidas:** ordenar as publicações da maior para a menor quantidade de curtidas.

A utilização do Merge Sort permite visualizar como um algoritmo estudado academicamente pode ser aplicado a um problema concreto de organização de dados.

## 🚧 Escopo e limitações

O ConectaUnB é um **protótipo acadêmico desenvolvido para demonstrar o funcionamento da ordenação de publicações**.

A aplicação possui funcionalidades demonstrativas, como a criação de publicações e a ordenação do feed. Entretanto, não implementa todos os recursos de uma rede social completa.

O objetivo principal não é oferecer uma plataforma profissional totalmente funcional, mas apresentar e demonstrar a aplicação do Merge Sort em um sistema web.

## ▶️ Como executar localmente

### 1. Pré-requisitos

- Python 3 instalado.
- Git instalado (opcional, para clonar o repositório).

### 2. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd ConectaUnB
```

Substitua `<URL_DO_REPOSITORIO>` pelo endereço do repositório no GitHub.

### 3. Crie e ative um ambiente virtual

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux ou macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Crie e preencha o banco de dados

Se o banco ainda não existir, execute:

```bash
python criar_banco.py
```

Esse script cria as tabelas e insere os registros de exemplo.

### 6. Execute a aplicação

```bash
python app.py
```

Abra o navegador e acesse:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📂 Estrutura do projeto

```text
ConectaUnB/
├── algoritmo/
│   └── merge_sort.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── app.py
├── criar_banco.py
├── requirements.txt
└── README.md
```

## 👩‍💻 Considerações finais

O desenvolvimento do ConectaUnB possibilitou integrar conceitos de desenvolvimento web, banco de dados e estruturas de dados, utilizando o Merge Sort como elemento central para demonstrar a ordenação de publicações.

O projeto evidencia como conceitos teóricos estudados em sala de aula podem ser aplicados na construção de uma aplicação prática.

---

**Projeto acadêmico — Estrutura de Dados e Algoritmos 2 (EDA2).**
