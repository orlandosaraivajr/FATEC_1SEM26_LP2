import time
from functools import wraps

def medir_tempo(func):
    """Decorator que mede o tempo de execução de uma função."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()  # tempo inicial (mais preciso que time.time)
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()     # tempo final
        duracao = fim - inicio
        print(f"⏱ Função '{func.__name__}' executada em {duracao:.6f} segundos.")
        return resultado
    return wrapper

@medir_tempo
def calcular():
    soma = 0
    for i in range(10_000_000):
        soma += i
    return soma

resultado = calcular()
print("Resultado:", resultado)

