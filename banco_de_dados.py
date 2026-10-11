
import sqlite3

conexao = sqlite3.connect("conectunb.db")
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# Tabela de usuários
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    curso TEXT,
    cargo TEXT,
    email TEXT UNIQUE
)
""")

# Tabela de publicações
cursor.execute("""
CREATE TABLE IF NOT EXISTS publicacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    texto TEXT NOT NULL,
    data TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    curtidas INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)
""")

# Tabela de vagas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vagas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa TEXT NOT NULL,
    cargo TEXT NOT NULL,
    local TEXT,
    modalidade TEXT,
    descricao TEXT
)
""")

# Vários usuários de exemplo
usuarios = [
    ("Ana Silva", "Engenharia de Software", "Estudante", "ana@exemplo.com"),
    ("Pedro Santos", "Ciência da Computação", "Desenvolvedor Python", "pedro@exemplo.com"),
    ("Julia Costa", "Sistemas de Informação", "Analista de Dados", "julia@exemplo.com"),
    ("Lucas Oliveira", "Engenharia de Software", "Estagiário de TI", "lucas@exemplo.com"),
    ("Mariana Souza", "Ciência da Computação", "Desenvolvedora Java", "mariana@exemplo.com"),
    ("Rafael Lima", "Sistemas de Informação", "Analista de Sistemas", "rafael@exemplo.com"),
    ("Beatriz Alves", "Engenharia de Software", "UX Designer", "beatriz@exemplo.com"),
    ("Gabriel Rocha", "Ciência da Computação", "Cientista de Dados", "gabriel@exemplo.com"),
    ("Camila Mendes", "Engenharia de Software", "Desenvolvedora Front-end", "camila@exemplo.com"),
    ("Felipe Martins", "Sistemas de Informação", "Administrador de Banco de Dados", "felipe@exemplo.com")
]

cursor.executemany("""
INSERT OR IGNORE INTO usuarios (nome, curso, cargo, email)
VALUES (?, ?, ?, ?)
""", usuarios)

# Várias publicações com datas e horários diferentes
publicacoes = [
    (1, "Começando um novo projeto de Python!", "2026-10-11 09:15:00", 12),
    (2, "Compartilhando meus estudos de Flask.", "2026-10-11 10:30:00", 28),
    (3, "Concluí um curso de análise de dados!", "2026-10-10 16:45:00", 19),
    (4, "Buscando oportunidades de estágio em TI.", "2026-10-10 11:20:00", 8),
    (5, "Estudando estruturas de dados e algoritmos.", "2026-10-09 14:00:00", 35),
    (6, "Dica: pratiquem SQL todos os dias!", "2026-10-09 08:30:00", 22),
    (7, "Compartilhando meu primeiro protótipo no Figma.", "2026-10-08 17:10:00", 15),
    (8, "Aprendendo machine learning com Python.", "2026-10-08 13:25:00", 41),
    (9, "Meu projeto de desenvolvimento web está evoluindo.", "2026-10-07 12:00:00", 17),
    (10, "Vamos compartilhar conhecimento na comunidade!", "2026-10-06 19:40:00", 50)
]

cursor.executemany("""
INSERT INTO publicacoes (usuario_id, texto, data, curtidas)
SELECT ?, ?, ?, ?
WHERE NOT EXISTS (
    SELECT 1 FROM publicacoes
    WHERE usuario_id = ? AND texto = ?
)
""", [
    (*p, p[0], p[1]) for p in publicacoes
])

# Várias vagas de exemplo
vagas = [
    ("Tech Solutions", "Estágio em Python", "Brasília - DF", "Híbrido", "Desenvolvimento de APIs."),
    ("Inova Tecnologia", "Desenvolvedor Júnior", "Brasil", "Remoto", "Desenvolvimento de aplicações web."),
    ("Data Brasil", "Estágio em Dados", "Brasília - DF", "Presencial", "Análise e tratamento de dados."),
    ("Nuvem Digital", "Desenvolvedor Java", "Brasil", "Remoto", "Desenvolvimento de sistemas."),
    ("Conecta Tech", "Estágio em Front-end", "Brasília - DF", "Híbrido", "HTML, CSS e JavaScript.")
]

cursor.executemany("""
INSERT INTO vagas (empresa, cargo, local, modalidade, descricao)
SELECT ?, ?, ?, ?, ?
WHERE NOT EXISTS (
    SELECT 1 FROM vagas
    WHERE empresa = ? AND cargo = ?
)
""", [
    (*v, v[0], v[1]) for v in vagas
])

conexao.commit()

print("Banco de dados criado!")
print("Usuários:", cursor.execute(
    "SELECT COUNT(*) FROM usuarios"
).fetchone()[0])
print("Publicações:", cursor.execute(
    "SELECT COUNT(*) FROM publicacoes"
).fetchone()[0])
print("Vagas:", cursor.execute(
    "SELECT COUNT(*) FROM vagas"
).fetchone()[0])

conexao.close()
