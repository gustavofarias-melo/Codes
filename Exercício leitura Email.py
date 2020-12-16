"""
Exercício Email
- Captura o provedor de e-mail que o usuário informar
"""
# Emails
email = "gustavoblk1@hotmail.com"
segundoEmail = "gustavofarias14@outlook.com"

# email
indice_arroba = email.index("@")
indice_ponto = email.index(".com")
pontoemail = email[indice_arroba+1:indice_ponto]

# segundoEmail
indice_arrobA = segundoEmail.index("@")
indice_pontO = segundoEmail.index(".")
pontoemail2 = segundoEmail[indice_arrobA+1:indice_pontO]

print(pontoemail)
print(pontoemail2)

"""
Exercício Email
- Captura o usuário antes do @ 
"""

conta = "gustavofarias14@outlook.com"
arroba = conta.index("@") # index - serve para pegar o indice dentro do e-mail até o caracter
user = conta[0:arroba] # arroba = 15º indice
print(user)