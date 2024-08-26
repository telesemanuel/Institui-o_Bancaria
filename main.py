import os
from modulo import * 

# Programa principal
if __name__ == '__main__':
    # Lista de dicionários
    correntistas = [
        {
            'Nome': 'Admin',
            'Saldo': 1000
        }
    ]

    # Entra no programa
    while True:
        exibir_menu()
        opcao = input('Opção desejada: ')
        os.system('cls')  # Limpa a tela (no Windows)

        if opcao == '1':
            # Cria um dicionário
            correntista = {
                'Nome': '',
                'Saldo': 0
            }
            correntista['Nome'] = input('Informe o nome a ser cadastrado: ')
            correntistas.append(correntista)
            print(f'{correntista["Nome"]} cadastrado com sucesso.')

        elif opcao == '2':
            titular = input('Informe o nome do titular: ')
            encontrado = False

            # Pesquisa pelo correntista
            for i in range(len(correntistas)):
                if titular in correntistas[i]['Nome']:
                    nome = correntistas[i]['Nome']
                    saldo = correntistas[i]['Saldo']
                    encontrado = True

                    # Exibe as operações
                    while True:
                        exibir_dados(nome, i, saldo)
                        exibir_operacoes()

                        operacao = input('Operação desejada: ')
                        os.system('cls')  # Limpa a tela

                        # Verifica a operação escolhida
                        match operacao:
                            case '1':
                                print(f'Saldo: R$ {saldo:,.2f}')
                            case '2':
                                valor = input('Valor do depósito: R$ ')
                                valor = float(valor.replace(',', '.'))
                                saldo = depositar_valor(saldo, valor)
                                correntistas[i]['Saldo'] = saldo
                                print(f'Depósito efetuado com sucesso. Saldo atual: R$ {saldo:,.2f}')
                            case '3':
                                valor = input('Valor do saque: R$ ')
                                valor = float(valor.replace(',', '.'))

                                if valor <= saldo:
                                    saldo = sacar_valor(saldo, valor)
                                    correntistas[i]['Saldo'] = saldo
                                    print(f'Saque efetuado com sucesso. Saldo atual: R$ {saldo:,.2f}')
                                else:
                                    print('Não foi possível efetuar o saque. Saldo insuficiente.')
                            case '4':
                                break
                            case _:
                                print('Operação inválida. Tente novamente.')
                        continue

            if not encontrado:
                print(f'{titular} não encontrado.')

        elif opcao == '3':
            print('Correntistas cadastrados:')
            for i, correntista in enumerate(correntistas):
                exibir_dados(correntista['Nome'], i, correntista['Saldo'])

        elif opcao == '4':
            titular = input('Informe o nome do titular da conta a ser excluída: ')
            encontrado = False

            for i in range(len(correntistas)):
                if titular in correntistas[i]['Nome']:
                    del correntistas[i]
                    print(f'{titular} excluído com sucesso.')
                    encontrado = True
                    break

            if not encontrado:
                print(f'{titular} não encontrado.')

        elif opcao == '5':
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")