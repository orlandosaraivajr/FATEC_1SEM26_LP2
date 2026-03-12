from abc import ABC, abstractmethod

# Classe abstrata
class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    # Método abstrato: TODA subclasse é obrigada a implementar
    @abstractmethod
    def fazer_som(self):
        pass

    # Método concreto: pode ser herdado normalmente
    def dormir(self):
        return f"{self.nome} está dormindo."


# Subclasse concreta (implementa o método abstrato)
class Cachorro(Animal):
    def fazer_som(self):
        return f"{self.nome} faz: Au Au!"


class Gato(Animal):
    def fazer_som(self):
        return f"{self.nome} faz: Miau!"


class Vaca(Animal):
    def fazer_som(self):
        return f"{self.nome} faz: Muuu!"


# --- Demonstração ---
animais = [
    Cachorro("Rex"),
    Gato("Mimi"),
    Vaca("Mimosa")
]

for a in animais:
    print(a.fazer_som())
    print(a.dormir())
    print("-" * 30)

