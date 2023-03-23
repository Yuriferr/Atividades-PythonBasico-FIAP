assinatura = input("Assinatura: ")

valor_bonus = 0

if assinatura.upper() == "BASIC":
    faturamento_anual = int(input("Por favor digite seu faturamento anual: "))
    valor_bonus = faturamento_anual * 0.3
    print("O valor a pagar é R${}".format(valor_bonus))
elif assinatura.upper() == "SILVER":
    faturamento_anual = int(input("Por favor digite seu faturamento anual: "))
    valor_bonus = faturamento_anual * 0.2
    print("O valor a pagar é R${}".format(valor_bonus))
elif assinatura.upper() == "GOLD":
    faturamento_anual = int(input("Por favor digite seu faturamento anual: "))
    valor_bonus = faturamento_anual * 0.1
    print("O valor a pagar é R${}".format(valor_bonus))
elif assinatura.upper() == "PLATINUM":
    faturamento_anual = int(input("Por favor digite seu faturamento anual: "))
    valor_bonus = faturamento_anual * 0.05
    print("O valor a pagar é R${}".format(valor_bonus))
else:
    print("Assinatura inexistente!!!")

