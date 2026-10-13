class Pessoa:
    def __init__(self, nome, email, idade, id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.idade = idade

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "idade": self.idade,
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            id=dados["id"],
            nome=dados["nome"],
            email=dados["email"],
            idade=dados["idade"],
        )

    def __str__(self):
        return f"{self.id} - {self.nome} ({self.email}), {self.idade} anos"