print("ADIVINHE O VALOR!!! (Você tem 5 chances) [0-99]")
num_secreto = 42
chance = 1
chute = 0

while chute != num_secreto and chance < 6:
    chance = chance + 1
    chute = int(input("Digite um valor: "))    
    if chute == num_secreto:
        print("VOCÊ ACERTOU!")
    elif chance == 5:
        print(f"PENSE BEM, ESTA E A ULTIMA CHANCE [{chance}/5]")
    elif chance == 6:
        print("ESTA FOI SUA ULTIMA CHANCE!")
    elif chute > num_secreto:
        print(f"Numero esta ACIMA do informado! Você tem [{chance}/5]")
    elif chute < num_secreto:
        print(f"Numero esta ABAIXO do informado! Você tem [{chance}/5]")

