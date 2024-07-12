#QUESTÃO 01 
print("Bem-vindo a Loja da Gabrielle Silva!") 

#VALOR UNITÁRIO 
valor = int(input('Informe o valor do produto: ')) 

#QUANTIDADE DO PRODUTO 
quantidade = int(input('Informe a quantidade do produto: ')) 
res = valor * quantidade 

#SEM DESCONTO 
sem_desconto = print(f"Valor SEM o desconto: R${res}") 

#REQUISITOS DE DESCONTO 
preco_total = 0 
preco_final = 0 

if (res < 2500): 
    desconto = 0 #DESCONTO DE 0% 
elif (res >= 2500 and res < 6000): 
    desconto = 4 #DESCONTO DE 4% 
elif (res >= 6000 and res < 10000): 
    desconto = 7 #DESCONTO DE 7% 
else:  
    desconto = 11 #DESCONTO DE 11% 

#COM DESCONTO 
preco_total = res * (desconto/100) 
preco_final = res - preco_total 
com_desconto = print(f"Valor COM o desconto: R${preco_final}") 