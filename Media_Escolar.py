aluno = input("Informe o nome do aluno: ")
print("*** Agora informe as 4 notas do aluno, separando por espaços.")
print()
usuario = input(f"Informe as notas do {aluno} (por espaço): ")
notas = usuario.split(" ")
resultado = float(notas[0]) + float(notas[1])  + float(notas[2])  + float(notas[3])

total = resultado / 4
print(f"Notas informadas: {notas[0]} | {notas[1]} | {notas[2]} | {notas[3]}")
print(f"Nota FINAL:{total}")