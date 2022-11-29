
print('=' *30)
print('{:^30}' .format('Bem-vindo ao caixa eletrônico do BANCO SANTO ANDRÉ'))
print('=' *30)
dnv = 1


while dnv == 1:

    opcao = int(input('''Escolha uma das opções
Para sacar dinheiro digite  [1] 
Para emprestimo digite      [2] 
Para tirar extrato da conta [3]
Opção: '''))



    if opcao == 1:
        print('=' *30)
        dinheiro = int(input('Qual valor deseja sacar?'))
        ced = 100
        totced = 0
        while True:
           if dinheiro >= ced:
               dinheiro -= ced
               totced += 1
           else:
               if totced > 0:
                    print(f'Total de {totced} cédulas de R${ced}')
               if ced == 100:
                   ced = 50
               elif ced == 50:
                   ced = 20
               elif ced == 20:
                   ced = 10
               elif ced == 10:
                   ced = 5
               elif ced == 5:
                   ced = 1
               totced = 0
               if dinheiro == 0:
                   break

        print('=' *30)
        print('Transação efetuada com sucesso!')

    elif opcao == 2:
        print('=' * 30)
        emprestimo = int(input('Qual valor que você deseja fazer o emprestimo? '))
        parcela = int(input('Em quantas parcelas deseja pagar o empretimo?'))
        valor = emprestimo/parcela
        valor *= 1.1
        print('Transação efetuada com sucesso!')
        print('+' * 30)
        print(f'Você ira pagar R${emprestimo} em {parcela} parcelas de R${valor:.2f}')
        print('O dinheiro vai estar disponível em 5 dias úteis')
        print('O BANCO SANTO ANDRÉ agradeçe a sua preferência')
        print('-' * 30)




    elif opcao == 3:
        print('''Pix enviado de R$35,00 Para Fulano 04/08/2022 
Pix recebido de R$55,00 de Ciclano 03/08/2022
Pagamento de fatura do cartão R$580,00 01/08/2022
Pix enviado de R$5,00 para a pinga no bar do seu Zé 30/07/2022
Pagamento da parcela do emprestimo pro agiota R$350,00 28/07/2022''')


    dnv = int(input('''Deseja fazer outra operação?
1 para Sim
2 para Não
opção: '''))


print('O Banco SANTO ANDRÉ Agradece!')
print('Tenha um Ótimo Dia!')
