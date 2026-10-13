from src.domain import Pessoa
import sqlite3
from pathlib import Path

class CadastroPessoasSQLite:
    def __init__(self, caminho):
        self.caminho = Path(caminho)
        self.criar_tabela()

    def conectar(self):
        conexao = sqlite3.connect(self.caminho)
        conexao.row_factory = sqlite3.Row
        return conexao

    def criar_tabela(self):
        with self.conectar() as conexao:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS pessoas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    idade INTEGER NOT NULL
                )
            """)

    def limpar(self):
        with self.conectar() as conexao:
            conexao.execute("DELETE FROM pessoas")

    def adicionar(self, pessoa):
        with self.conectar() as conexao:
            cursor = conexao.execute(
                "INSERT INTO pessoas (nome, email, idade) VALUES (?, ?, ?)",
                (pessoa.nome, pessoa.email, pessoa.idade),
            )
            pessoa.id = cursor.lastrowid
            return pessoa

    def carregar(self):
        with self.conectar() as conexao:
            cursor = conexao.execute(
                "SELECT id, nome, email, idade FROM pessoas ORDER BY nome"
            )
            return [Pessoa.from_dict(linha) for linha in cursor.fetchall()]