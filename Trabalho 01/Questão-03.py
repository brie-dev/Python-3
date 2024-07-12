#QUESTÃO 03 
print('-' * 50) 
print('Bem vindo a Copiadora da Gabrielle Silva!') 
print('-' * 50) 
print('Entre com o tipo de serviço desejado:') 
print('DIG - Digitalização') 
print('ICO - Impressão Colorida') 
print('IPB - Impressão Preto e Branco') 
print('FOT - Fotocópia') 

#TIPO DE SERVIÇO 
def escolha_servico(): 
    while True: 
        servico = input('Entre com o tipo de serviço desejado (DIG/ICO/IPB/FOT): ') 
        if (servico == 'dig' or servico == 'ico' or servico == 'ipb' or servico == 'fot'): 
            return servico 
        else: 
            print('Escolha inválida, entre com o tipo do serviço novamente') 

#NUMERO DE PAGINAS COM OU SEM DESCONTO 
def num_pagina(): 
    while True: 
        try: 
            num_pagina = int(input('Entre com o número de páginas: ')) 
            if (num_pagina < 20): 
                return num_pagina 
            elif (num_pagina >= 20 and num_pagina < 200): 
                return num_pagina * 0.85 
            elif (num_pagina >= 200 and num_pagina < 2000): 
                return num_pagina * 0.80 
            elif (num_pagina >= 2000 and num_pagina < 20000): 
                return num_pagina * 0.75 
            else: 
                print('Não aceitamos tantas páginas de uma vez.') 
                print('Por favor, entre com o número de páginas novamente.') 
        except ValueError: 
            print('Por favor, entre com o número válido de páginas.') 

#SERVIÇO ADICIONAL 
def servico_extra(): 
    while True: 
        extra = input('Desejar adicionar algum serviço? 1 - Encadernação Simples - R$ 15.00 | 2 - Encadernação Capa Dura - R$ 40.00 | 0 - Não desejo mais nada | : ') 
        if (extra == '1' or extra == '2' or extra == '0'): 
            return extra 
        else:  
            print('Inválido, escolha entre 1, 2 e 0') 

#CODIGO PRINCIPAL 
def main(): 
    try: 
        servico = escolha_servico() 
        num_paginas = num_pagina() 
 
        if servico == 'dig': 
            valor_pagina = 1.10 
        elif servico == 'ico': 
            valor_pagina = 1.00 
        elif servico == 'ipb': 
            valor_pagina = 0.40 
        else: 
            valor_pagina = 0.20 

#CALCULO DO VALOR FINAL  
        total = valor_pagina * num_paginas 
        extra = servico_extra() 

        if (extra == '1'): 
            total += 15 
        elif (extra == '2'): 
            total += 40 

#EXIBIÇÃO 
        print(f'Total: R$ {total:.2f} (serviço: {servico} * páginas: {num_paginas} + extra: {extra})') 
    except KeyboardInterrupt: 
        exit() 

main() 