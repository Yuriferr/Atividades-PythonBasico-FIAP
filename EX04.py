minutos_autais = int(input("Por favor digite os minutos atuais: "))
fatorial = 0

if minutos_autais == 1:
    print("A senha necessária para desbloqueio: LIBERDADE1")
elif minutos_autais == 0 or minutos_autais > 1:
    for i in range(1, minutos_autais):
        fatorial = minutos_autais * i
        minutos_autais = fatorial
    print("A senha necessária para desbloqueio: LIBERDADE{}".format(fatorial))
else:
    print("Número negativo, não permitido!!!")

