import textwrap


def menu():
    menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova Conta
[lc] Listar Conta
[nu] Novo Usuário
[q] Sair

=> """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato,/):
    if valor == 0:
        saldo == valor_extrato == f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação não realizada! O valor informado é inválido. @@@")
        
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor> saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação não realizada! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n @@@ Operação não realizada! O valor do saque excede o limite diário ou em conta. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação não realizado! Número máximo de saques excedido. @@@")
    elif valor > 0:
        saldo -= valor 
        extrato += f"Saque:\t\t R${valor:.2f}\n"
        numero_saques +=1
        print("\n === Saque realizado com sucesso! ===")
        
    else:
        print("\n@@@ Operação não realizada! o valor informado é inválido. @@@")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n === EXTRATO ===")
    print(" Não foram realizadas movimentações em sua conta. " if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("===============")
    

def criar_usuario(usuarios):
    cpf = input("Informe o cpf (Somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ Já existe um usuário com esse cpf cadastrado! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Inform o endereço (logradouro, nro - bairro- cidade/sigla estado): ")
    usuarios.append({"nome":nome, "data_nascimento":data_nascimento,"cpf":cpf, "endereco":endereco })
    
    print("=== Seu cadastro foi realizado com sucesso! ===")


def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] ==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta,usuarios):
    cpf = input("Informe o seu cpf: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n ===    Conta Criada com sucesso! ====")
        return {"agencia": agencia, "numero_conta":numero_conta, "usuario": usuario}
    print("\n @@@Usuário não encontrado, fluxo de criação de conta encerrado @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\{conta['agencia']}
            c/c:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0023"


    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:
        opcao = menu()
       
        if opcao =="d":
            valor = float(input("Informe o valor do depósito a ser realizado: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao =="s":
            valor =float(input("Informe o valor desejado para o saque: "))
            
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao =="e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao =="nu":
            criar_usuario(usuarios)
        elif opcao =="nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
           
            if contas:
                contas.append(conta)
        elif opcao =="lc":
            listar_contas(contas)
        elif opcao =="q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada ou vá até uma agência bancaria.")
main()
