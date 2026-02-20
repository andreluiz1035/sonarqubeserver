import os

def dividir(a, b):
    return a / b  # possível divisão por zero


def executar(usuario_input):
    return eval(usuario_input)  # vulnerabilidade


senha = "123456"  # hardcoded credential

print(dividir(10, 0))