def verificar_bissexto(ano):
    # Verifica se o ano é divisível por 4 e não é divisível por 100, exceto se for divisível por 400
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True  # O ano é bissexto
    else:
        return False  # O ano não é bissexto

# Solicita ao usuário que insira o ano desejado
ano = int(input("Digite o ano que você deseja verificar: "))

# Verifica se o ano é bissexto e fornece uma explicação correspondente
if verificar_bissexto(ano):
    print(f"O ano {ano} é bissexto, pois atende às condições estabelecidas.")
    print("Ele possui 366 dias.")
else:
    print(f"O ano {ano} não é bissexto, pois não atende às condições estabelecidas.")
    print("Ele possui 365 dias.")
