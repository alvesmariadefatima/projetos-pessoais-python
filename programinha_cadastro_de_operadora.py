nome_cliente = input('Nome completo do cliente: ')
prefixo_ddd = int(input('Digite o DDD da sua região: '))
operadora_celular = str(input('Qual operadora você usa: 1 - Tim / 2 - Claro / 3 - Vivo / 4 - Oi'))
telefone_cliente = input('Digite seu número de telefone: ')
data_nascimento = input('Digite a sua data de nascimento: ')
endereco_cliente = input('Digite seu endereço: ')
numero_residencia = input('Número/Complemento: ')
bairro_cliente = input('Digite o bairro: ')
cidade_cliente = input('Digite o município onde mora: ')
estado_cliente = input('Digite o estado onde você mora: ')

print('Por favor, confirme seus dados antes de enviar: ')
print('=================================================')
print('Nome completo do cliente: {}'.format(nome_cliente))
print('Seu prefixo DDD é: {}'.format(prefixo_ddd))
print('Sua operadora de celular selecionada é: {}'.format(operadora_celular))
print('Seu número de telefone é: {}'.format(telefone_cliente))
print('Sua data de nascimento é: {}'.format(data_nascimento))
print('Seu endereço completo é: {}'.format(endereco_cliente))
print('Número/complemento: {}'.format(numero_residencia))
print('Seu bairro é: {}'.format(bairro_cliente))
print('Sua cidade/município onde reside é: {}'.format(cidade_cliente))
print('Seu estado onde mora é: {}'.format(estado_cliente))
print('===================================================')
print('Seus dados foram enviados com sucesso, {} !!!'.format(nome_cliente))