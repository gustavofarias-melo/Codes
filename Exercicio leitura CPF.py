"""
 Exercício CPF 
- Captura os números antes e depois do hífen, exercício básico

"""

cpf = input("Informe seu CPF (utilizando pontos): ")
# Antes do hífen
antes_hifen = cpf.index("-")
cpf_antes = cpf[:antes_hifen]
# Depois do hífen
depois_hifen = cpf.index("-")
cpf_depois = cpf[depois_hifen+1::]

print(f"CPF: {cpf}")
print(f"CPF (sem hifen): {cpf_antes}")
print(f"CPF (somente hifen): {cpf_depois}")