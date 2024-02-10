modalidades = []
naptos = 0
totalClientes = 0
escaloes = {}
#_id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado <- estrutura dos clientes no CSV
# abre o ficheiro CSV em forma de leitura e com encoding UTF-8
with open("TPC1\emd.csv", "r", encoding="utf-8") as f:
    # cria um itrerador para ignorar a primeira linha
    iterador = iter(f)
    next(iterador)
    # percorre as restantes linhas do ficheiro
    for linha in iterador:
        # transforma a linha em uma lista dos atributos do cliente
        cliente = linha.split(',')

        modalidade = cliente[8].lower()
        apto = cliente[-1]
        idade = cliente[5]
        # adiciona a modalidade a uma lista caso esta ainda não esteja na lista
        if modalidade not in modalidades:
            modalidades.append(modalidade)
        # se um cliente for apto incremente a quantidade de aptos
        if apto == 'true\n':
            naptos += 1
        # determina o escalão usando o valor inteiro da divisão por 5
        escalao = int(int(idade)/5)
        # caso o escalão ainda não exista será criado no dicionário de escaslões, caso exista é incrementado o número de clientes daquele escalão
        if escalao not in escaloes:
            escaloes[escalao] = 1
        else:
            escaloes[escalao] += 1
        #incrementa o número total de clientes
        totalClientes += 1

# ordena e mostra a modalidades existentes por ordem alfabética
print("Modalidades: ")
modalidades.sort()
for m in modalidades:
    print("- " + m)

# calcula a porcentagem de aptos
pAptos = naptos/totalClientes*100
# mostra a porcentagem de aptos e inaptos
print(f"\nAptos: {pAptos:.1f}%    Inaptos: {100-pAptos:.1f}%\n")

# ordena o dicionário por escalões e mostra quantos clientes pertencem a cada escalão
valores = list(escaloes.items())
valores.sort()
escaloesOrd = dict(valores)

for c,v in escaloesOrd.items():
    n = c*5
    print(f"[{n}-{n+4}] -> {v}")
