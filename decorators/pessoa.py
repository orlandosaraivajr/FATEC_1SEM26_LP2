from datetime import date

class Pessoa:
    especie = "Humano"  # atributo de classe (compartilhado entre todas as instâncias)

    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    def idade(self):
        """Método de instância: usa dados específicos do objeto."""
        ano_atual = date.today().year
        return ano_atual - self.ano_nascimento

    @classmethod
    def mudar_especie(cls, nova_especie):
        """Método de classe: acessa e altera atributos da classe."""
        cls.especie = nova_especie
        print(f"A espécie foi alterada para: {cls.especie}")

    @staticmethod
    def eh_maior_de_idade(idade):
        """Método estático: não depende de instância nem da classe."""
        return idade >= 18



# Criando duas pessoas
p1 = Pessoa("Ana", 2000)
p2 = Pessoa("Carlos", 2010)

# Método de instância → depende do objeto
print(f"{p1.nome} tem {p1.idade()} anos.")
print(f"{p2.nome} tem {p2.idade()} anos.")

# Método estático → pode ser chamado sem instanciar
print("Ana é maior de idade?", Pessoa.eh_maior_de_idade(p1.idade()))
print("Carlos é maior de idade?", Pessoa.eh_maior_de_idade(p2.idade()))

# Método de classe → altera o atributo compartilhado
Pessoa.mudar_especie("Ciborgue")

print(p1.especie)
print(p2.especie)
