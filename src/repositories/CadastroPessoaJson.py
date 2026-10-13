from src.domain import Pessoa
import json
from pathlib import Path

class CadastroPessoasJson:
    def __init__(self, caminho):
        self.caminho = Path(caminho)

    def carregar(self):
        if not self.caminho.exists():
            return []
        with self.caminho.open("r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return [Pessoa.from_dict(item) for item in dados]

    def get_by_id(self, id):
      pessoas = self.carregar()
      for pessoa in pessoas:
        if pessoa.id == id:
          return pessoa

    def salvar(self, pessoas):
        dados = [pessoa.to_dict() for pessoa in pessoas]
        with self.caminho.open("w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    def proximo_id(self):
        pessoas = self.carregar()
        if not pessoas:
            return 1
        return max(pessoa.id for pessoa in pessoas) + 1

    def adicionar(self, pessoa):
        pessoas = self.carregar()
        pessoa.id = self.proximo_id()
        pessoas.append(pessoa)
        self.salvar(pessoas)
        return pessoa

    def listar(self):
        return self.carregar()