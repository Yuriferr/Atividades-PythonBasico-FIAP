total_impar = 0
total_par = 0

print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
for i in range(1, 51, 2):
    nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(i)))
    total_impar += nota

print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
for i in range(2, 51, 2):
    nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(i)))
    total_par += nota

media_impar = total_impar / 25
media_par = total_par / 25

print("MÉDIA DE NOTA DOS NÚMEROS ÍMPARES: {}".format(media_impar))
print("MÉDIA DE NOTA DOS NÚMEROS PARES: {}".format(media_par))

if total_impar > total_par:
    print("OS NÚMEROS ÍMPARES TIVERAM MAIOR NOTA!!!")
elif total_par / total_impar:
    print("OS NÚMEROS PARES TIVERAM MAIOR NOTA!!!")
else:
    print("EMPATE, AS DUAS METADES TIVERAM A MESMA NOTAS!!!")


