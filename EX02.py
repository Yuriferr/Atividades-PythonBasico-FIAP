segunda = int(input("Digite a quantidde de votos que segunda-feira recebeu: "))
terca = int(input("Digite a quantidde de votos que terça-feira recebeu: "))
quarta = int(input("Digite a quantidde de votos que quarta-feira recebeu: "))
quinta = int(input("Digite a quantidde de votos que quinta-feira recebeu: "))
sexta = int(input("Digite a quantidde de votos que sexta-feira recebeu: "))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("Segunda-feira ganhou!!!")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("Terça-feira ganhou!!!")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("Quarta-feira ganhou!!!")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("Quinta-feira ganhou!!!")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("Sexta-feira ganhou!!!")
else:
    print("Empate refaça os votos!!!")