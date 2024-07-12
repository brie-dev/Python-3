#QUESTÃO 02 
print('Bem-vindo a Loja de Gelados da Gabrielle Silva') 
print('-----------------Cardápio-----------------') 
print('--| Tamanho | Cupuaçu (CP) | Açaí (AC) |--') 
print('--|    P    |   R$  9.00   | R$ 11.00  |--') 
print('--|    M    |   R$  14.00  | R$ 16.00  |--') 
print('--|    G    |   R$  18.00  | R$ 20.00  |--') 
print('------------------------------------------') 
total = 0 

#FAZENDO O PEDIDO 
while True: 
    sabor = input('Entre com o sabor desejado (CP/AC): ') 
    if (sabor != 'cp' and sabor != 'ac'): 
        print('Sabor inválido. Tente novamente') 
        continue 
    tamanho = input('Entre com o tamanho desejado (P/M/G): ') 
    if (tamanho != 'p' and tamanho != 'm' and tamanho != 'g'): 
        print('Tamanho inválido. Tente novamente') 
        continue 

#DEFININDO VALORES COM CADA COMBINAÇÃO 
    if (sabor == 'cp'): 
        if tamanho == 'p': 
            valor = 9 
        elif tamanho == 'm': 
            valor = 14 
        elif tamanho == 'g': 
            valor = 18 
    elif (sabor == 'ac'): 
        if tamanho == 'p': 
            valor = 11 
        elif tamanho == 'm': 
            valor = 16 
        elif tamanho == 'g': 
            valor = 20 

#NOMEANDO O QUE FOI PEDIDO 
    if (sabor == 'cp'): 
        tipo_sabor = 'Cupuaçu' 
    else: 
        tipo_sabor = 'Açaí' 
    if (tamanho == 'p'): 
        tipo_tamanho = 'P' 
    elif (tamanho == 'm'): 
        tipo_tamanho = 'M' 
    elif (tamanho == 'g'): 
        tipo_tamanho = 'G' 

#ACUMULANDO O TOTAL DO(S) PEDIDOS 
    total += valor 
    print(f'Você pediu um {tipo_sabor} no tamanho {tipo_tamanho}: R${total:.2f}') 
    aumentar_pedido = input('Deseja pedir mais alguma coisa? (S/N): ') 
    if (aumentar_pedido != 's'): 
        break 
#FINAL 
print(f'O valor total a ser pago: {total:.2f}') 