
import os

def dividir(a, b):
    return a / b  # possível divisão por zero


def executar(usuario_input):
    return eval(usuario_input)  # vulnerabilidade



print(dividir(10, 0))

print("Hello world")
anapass = "senha"
PASSWORD = "senha"