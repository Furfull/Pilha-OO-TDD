from logging import raiseExceptions


class Cliente():

    def __init__(self, cpf: str, nome: str, email: str):
        if cpf == "":
            raise Exception ('CPF VAZIO')
        if nome == "":
            raise Exception ('NOME VAZIO')
        if email == "":
            raise Exception ('EMAIL VAZIO')
        self.cpf = cpf
        self.nome = nome
        self.email = email

