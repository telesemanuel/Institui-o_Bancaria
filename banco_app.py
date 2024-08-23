
banco_de_dados = {}

def criar_conta():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in banco_de_dados:
        print("Conta já existe.")
        return

    nome = input("Digite o nome do titular: ")
    saldo = float(input("Digite o saldo inicial: "))
    
    banco_de_dados[numero_conta] = {
        'nome': nome,
        'saldo': saldo
    }
    print("Conta criada com sucesso!")

def consultar_dados_pessoais():
    numero_conta = input("Digite o número da conta: ")
    conta = banco_de_dados.get(numero_conta)
    if conta:
        print(f"Nome: {conta['nome']}")
        print(f"Saldo: {conta['saldo']:.2f}")
    else:
        print("Conta não encontrada.")

def alterar_dados_pessoais():
    numero_conta = input("Digite o número da conta: ")
    conta = banco_de_dados.get(numero_conta)
    if conta:
        novo_nome = input("Digite o novo nome do titular: ")
        banco_de_dados[numero_conta]['nome'] = novo_nome
        print("Dados alterados com sucesso!")
    else:
        print("Conta não encontrada.")

def excluir_conta():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in banco_de_dados:
        del banco_de_dados[numero_conta]
        print("Conta excluída com sucesso!")
    else:
        print("Conta não encontrada.")

def consultar_saldo():
    numero_conta = input("Digite o número da conta: ")
    conta = banco_de_dados.get(numero_conta)
    if conta:
        print(f"Saldo: {conta['saldo']:.2f}")
    else:
        print("Conta não encontrada.")

def depositar_valor():
    numero_conta = input("Digite o número da conta: ")
    conta = banco_de_dados.get(numero_conta)
    if conta:
        valor = float(input("Digite o valor a ser depositado: "))
        banco_de_dados[numero_conta]['saldo'] += valor
        print("Depósito realizado com sucesso!")
    else:
        print("Conta não encontrada.")

def sacar_valor():
    numero_conta = input("Digite o número da conta: ")
    conta = banco_de_dados.get(numero_conta)
    if conta:
        valor = float(input("Digite o valor a ser sacado: "))
        if valor <= conta['saldo']:
            banco_de_dados[numero_conta]['saldo'] -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente.")
    else:
        print("Conta não encontrada.")

def menu_principal():
    while True:
        print(f"\n{"$"*10} Menu Principal {"$"*10}\n")
        print("1. Criar Conta")
        print("2. Consultar Dados Pessoais")
        print("3. Alterar Dados Pessoais")
        print("4. Excluir Conta")
        print("5. Consultar Saldo")
        print("6. Depositar Valor")
        print("7. Sacar Valor")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                criar_conta()
            case '2':
                consultar_dados_pessoais()
            case '3':
                alterar_dados_pessoais()
            case '4':
                excluir_conta()
            case '5':
                consultar_saldo()
            case '6':
                depositar_valor()
            case '7':
                sacar_valor()
            case '8':
                print("App encerrado.")
                break
            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    menu_principal()
