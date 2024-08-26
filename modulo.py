from datetime import date 

#função exibir o o menu
def exibir_menu():
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year

    print(f"\n{"#"*20} Money Bank {"#"*20}\n")
    print(f" {dia:02d}/{mes:02d}/{ano}")
    print("1 - Criar conta")
    print("2 - Entrar na conta")
    print("3 - Exiber correntistas")
    print("4 - Excluir conta")
    print("5 - Encerrar Programa")

#Função exibir operações
def exibir_operacoes():
    print("\nOPERAÇÕES\n")
    print("Consultar saldo")
    print("Depositor valor")
    print("Sacar Valor")
    print("Voltar")
    
#Função exibir dados dos correntitas
def exibir_dados(nome, i, saldo):
    print(f"ID: {i}")
    print(f"Nome: {nome}")
    print(f"Agência: {i}")
    print(f"Saldo: {saldo}")

#Função de déposito
def depositar_valor(saldo, valor):
    #Adiciona um valor ao saldo atual.

    if valor > 0:
        saldo += valor
    else:
        print("O valor do depósito deve ser positivo.")
    return saldo

# Função para sacar valor
def sacar_valor(saldo, valor):
    #Subtrai um valor do saldo atual.
   
    if valor > 0:
        if valor <= saldo:
            saldo -= valor
        else:
            print("Saldo insuficiente.")
    else:
        print("O valor do saque deve ser positivo.")
    return saldo