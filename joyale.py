def menu():
    print("___________________MENU_____________________")
    print("➜ [1] Registrar crianças")
    print("➜ [2] Lista de crianças cadastradas")
    print("➜ [3] Informações sobre vacinas")
    print("➜ [x] Sair")
    print("____________________________________________")


"""def cadastroCrianca():
    arquivo = open("CriançasCadastradas.txt" , "w")
    crianca = input("Nome da criança: ")
    maeDaCrianca = input("Nome da mãe: ")
    paiDaCrianca = input("Nome do pai: ")
    endereco = input("Endereço: ")
    numero = input("Número:")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    telefone = int(input("Telefone: "))
    cep = int(input("CEP: "))
    dataNasc = int(input("Data de Nascimento: "))
    comprimento = float(input("Comprimento(cm): "))
    peso = int(input("Peso: "))
    perCefalico = float(input("Perímetro Cefálico(cm): "))
    tipoDeParto = input("Tipo de parto(Normal,Cesariano): ")
    obs = input("Observações: ")
    pacientes = [[crianca,maeDaCrianca,paiDaCrianca,endereco,numero,cidade,estado,telefone,cep,dataNasc,comprimento,peso,perCefalico,tipoDeParto,obs]]
    tamPacientes = len(pacientes)
    for i in range(tamPacientes):
        tamP = len(pacientes[i])
        for k in range(tamP):
            arquivo.write(pacientes[i][k] + ",")
        arquivo.write("\n")
        arquivo.close()"""
        
def validarCpf(cpf):
    tam_cpf = len(cpf)
    if tam_cpf == 11:
        return True
    else:
        return False

def validarCep(cep):
    tam_cep = len(cep)
    if tam_cep == 8:
        return True
    else:
        return False

#def getPacientes(nomearq):
#    arquivo = open(nomearq , "r")
#    linhas = arquivo.readlines()
#    tamLinhas = len(linhas)
#    pacientes = []
#    for i in range(tamLinhas):
#        linha = linhas[cont]
#        paciente = linhas.split(",")
#        pacientes.append(paciente)
#    return pacientes

#def listarPacientes(nomeArq):
#    pacientes = getpacientes(nomeArq)
#    tamPacientes = len(pacientes)
#    indiceNomeCri = 0
#    for i in range(tamPacientes):
#       print(pacientes[i][indiceNomeCri])

def listarPacientes2(nomearq):
    arquivo = open('CriançasCadastradas.txt','r')
    linhas=arquivo.readlines()
    for linha in linhas:
        crianca=linha.split(",")
        print("*"*60)
        print ("NOME DA CRIANÇA: ",crianca[0])
        print ("NOME DA MÃE: ",crianca[1])
        print ("NOME DO PAI: ",crianca[2])
        print ("ENDEREÇO: ",crianca[3])
        print ("NUMERO DA CASA: ",crianca[4])
        print ("CIDADE: ",crianca[5])
        print ("ESTADO: ",crianca[6])
        print ("TELEFONE: ",crianca[7])
        print ("CEP: ",crianca[8])
        print ("DATA NASCIMENTO: ",crianca[9])
        print ("COMPRIMENTO: ",crianca[10])
        print ("PESO: ",crianca[11])
        print ("PERIMETRO CEFALICO: ",crianca[12])
        if crianca[13]=="1":
            parto="PARTO NORMAL"
        else:
            parto="PARTO CESARIO"
        print ("TIPO DE PARTO: ",parto)
        print ("OBSERVAÇÕES: ",crianca[14])
        print("*"*60)
    arquivo.close()
                     
def cadastrar_paciente():
    print("******Cadastro de Crianças******")
    arquivo = open("CriançasCadastradas.txt" , "a") #<- esse "a" para evitar subescrever
    crianca = input("Nome da criança: ")
    while(str.isdigit(crianca)):
        crianca = input("Por favor digite o nome da criança: ")
    maeDaCrianca = input("Nome da mãe: ")
    paiDaCrianca = input("Nome do pai: ")
    endereco = input("Endereço: ")
    numero = input("Número:")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    telefone = input("Telefone: ")
    cep = input("CEP: ")
    verifica_cep=validarCep(cep)
    while(verifica_cep!=True):
        cep = input("Digite novamente o CEP: ")
        verifica_cep = validarCep(cep)
    cpf = input("CPF: ")
    verifica_cpf = validarCpf(cpf)
    while(verifica_cpf!=True):
        cpf = input("Digite novamente o CPF: ")
        verifica_cpf = validarCpf(cpf)
    dataNasc = input("Data de Nascimento: ")
    comprimento = input("Comprimento(cm): ")
    peso = input("Peso: ")
    perCefalico = input("Perímetro Cefálico(cm): ")
    tipoDeParto = input("Tipo de parto(Normal[1] ou Cesariano[2]): ")
    obs = input("Observações: ")
    pacientes = [[crianca,maeDaCrianca,paiDaCrianca,endereco,numero,cidade,estado,telefone,cep,dataNasc,comprimento,peso,perCefalico,tipoDeParto,obs]]
    tamPacientes = len(pacientes)
    for i in range(tamPacientes):
        tamP = len(pacientes[i])
        for k in range(tamP):
            arquivo.write(pacientes[i][k] + ",")
    arquivo.write("\n")
    arquivo.close()
    
