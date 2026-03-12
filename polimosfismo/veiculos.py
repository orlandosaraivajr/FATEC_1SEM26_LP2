class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        return f"O {self.marca} {self.modelo} está acelerando..."

    def frear(self):
        return f"O {self.marca} {self.modelo} está freando..."

    def info(self):
        return f"Veículo genérico: {self.marca} {self.modelo}"


# --- Subclasses ---

class Carro(Veiculo):
    def acelerar(self):
        return f"O carro {self.marca} {self.modelo} acelera suavemente!"

    def abrir_porta_malas(self):
        return "O porta-malas foi aberto."


class Moto(Veiculo):
    def acelerar(self):
        return f"A moto {self.marca} {self.modelo} acelera com um ronco esportivo!"

    def empinar(self):
        return "A moto está empinando na estrada!"


class Caminhao(Veiculo):
    def acelerar(self):
        return f"O caminhão {self.marca} {self.modelo} ganha velocidade lentamente."

    def carregar(self):
        return "O caminhão está sendo carregado com mercadorias."


class Onibus(Veiculo):
    def acelerar(self):
        return f"O ônibus {self.marca} {self.modelo} sai devagar do ponto."

    def abrir_portas(self):
        return "As portas do ônibus foram abertas para os passageiros."


# --- Demonstração ---
veiculos = [
    Carro("Toyota", "Corolla"),
    Moto("Honda", "CB 500"),
    Caminhao("Volvo", "FH"),
    Onibus("Mercedes", "BRT")
]

for v in veiculos:
    print(v.info())
    print(v.acelerar())
    print(v.frear())
    # Chamando métodos específicos (se existirem)
    if isinstance(v, Carro):
        print(v.abrir_porta_malas())
    elif isinstance(v, Moto):
        print(v.empinar())
    elif isinstance(v, Caminhao):
        print(v.carregar())
    elif isinstance(v, Onibus):
        print(v.abrir_portas())
    print("-" * 40)
