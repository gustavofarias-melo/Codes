usuario = input("Insira seu e-mail: ")
usuario_separar = usuario.split("@")

#v2
email = "gustavo.farias@uol.com.br"
email2 = "empresatest@hotmail.com"
separar = email.split("@")
separar2 = email2.split("@")

#Exercício leitura Email.py
print(f"login: {usuario_separar[0]}")
print(f"provedor: {usuario_separar[1]}")
print("---------------------------")
print(f"login: {separar[0]}")
print(f"provedor: {separar[1]}")
print("---------------------------")
print(f"login2: {separar2[0]}")
print(f"provedor2: {separar2[1]}")

"""
v1
    # Arroba
    i_arroba = email.index("@")

    # Ponto
    i_ponto = email.index(".com")

    usuario = email[:i_arroba]
    print(usuario)
    provedor = email[i_arroba::]
    print(provedor)
"""

