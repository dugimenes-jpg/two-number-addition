    #Primeiro declarar as variáveis em formato de 'String'
n1_str = input('Primeiro número ')
n2_str = input('Segundo número ')

    #Agora fazer com que essas strings sejam lidas como números para que ocorra a soma deles
n1_int = int(n1_str) #Converte string em número inteiro
n2_int = int(n2_str) #idem ao anterior

    #Calcular a soma entre eles
soma = n1_int + n2_int

print('A soma é: ', soma)
