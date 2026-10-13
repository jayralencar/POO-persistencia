from .Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, email, idade, cargo, salario, id=None):
        super().__init__(nome, email, idade, id)
        self.cargo = cargo
        self.salario = salario

    def to_dict(self):
        dados = super().to_dict()
        dados.update({
            "cargo": self.cargo,
            "salario": self.salario,
        })
        return dados

    @classmethod
    def from_dict(cls, dados):
        pessoa = super().from_dict(dados)
        return cls(
            id=pessoa.id,
            nome=pessoa.nome,
            email=pessoa.email,
            idade=pessoa.idade,
            cargo=dados["cargo"],
            salario=dados["salario"],
        )

    def __str__(self):
        return f"{super().__str__()}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}"