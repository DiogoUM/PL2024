import ply.lex as lex
import sys
import json
from datetime import date

tokens = (
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR',
    'SALDO',
    'NOVO',
    'STOCK'
)

t_LISTAR = r'(?i:LISTAR)'
t_SAIR = r'(?i:SAIR)'
t_SALDO = r'(?i:SALDO)'


def t_SELECIONAR(t):
    r'(?i:SELECIONAR\s+(\w\d+))'
    t.value = t.value.split()[-1]
    return t

def t_MOEDA(t):
    r'(?i)MOEDA(\s+(2e|1e|50c|20c|10c|5c|2c|1c),)*(\s*(2e|1e|50c|20c|10c|5c|2c|1c)\s*\.)'

    t.value = t.value[6:-1]
    t.value = t.value.split(',')
    l = t.value
    valores = []
    for m in l:
        v = m.strip()
        if v[-1] == "e":
            valor =  v[:-1],0
        else:
            valor = 0,v[:-1]
        valores.append(valor)

    t.value = valores
    return t

#todo def t_NOVO(t):

#todo def t_STOCK(t):

t_ignore = '\t '

def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Carracter desconhecido")
    t.lexer.skip(1)

lexer = lex.lex()

with open('produtos.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    produtos = {}
    for produto in data["stock"]:
        produtos[produto['cod']] = produto

carteira = 0

def listar():
    global produtos

    print('''
maq:
Código | Nome | Quantidade | Preço
    ----------------------------------
    ''')
    for k,v in produtos.items():
        nome = v['nome']
        qt = v['quant']
        pr = v['preco']
        print(f'{k}  | {nome} | {qt} | {pr}')
    print('\n')

def addCarteira(e,c):
    global carteira

    carteira += e*100 + c

def printDinheiro(valor):
    if (valor == 0):
        print('0c', end='', flush=True)
    else:
        euros = valor // 100
        centimos = valor - euros * 100
        if euros > 0:
            print(f'{str(euros)}e', end='', flush=True)
        if centimos > 0:
            print(f'{str(centimos)}c', end='', flush=True)

def saldo(enter = True):
    global carteira
    print(f'maq: Saldo = ', end='', flush=True)
    printDinheiro(carteira)
    if enter: print('\n')

def selecionarProduto(codigo):
    global carteira
    global produtos

    precoPedido = int(produtos[codigo]['preco'] * 100)


    if codigo not in produtos:
        print('maq: Código Inválido')
    elif (produtos[codigo]['quant'] == 0):
        print('maq: produto indisponivel')
    elif (precoPedido > carteira):
        print('maq: Saldo insuficiente para satisfazer o seu pedido')
        saldo(False)
        print('; Pedido = ', end='', flush=True)
        printDinheiro(precoPedido)
        print('\n')
    else:
        print('Pode retirar o produto dispensado ' + produtos[codigo]['nome'])
        produtos[codigo]['quant'] -= 1
        carteira -= precoPedido
        saldo()

def sair():
    with open('produtos.json', 'w', encoding='utf-8') as file:
        p = [{"cod": k, **v} for k, v in produtos.items()]
        dic = {'stock':p}
        json.dump(dic, file)
    global carteira
    # TODO troco
    saldo()
    print('maq: Até à próxima')


data = date.today()
print(f'''
maq: {data}, Stock carregado, Estou atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
''')

print('>> ',end='', flush=True)
fim = False
for linha in sys.stdin:
    lexer.input(linha)

    for token in lexer:
        if token.type == 'MOEDA':
            for e, c in token.value:
                addCarteira(int(e), int(c))
            saldo()
        elif token.type == 'LISTAR':
            listar()
        elif token.type == 'SELECIONAR':
            selecionarProduto(token.value)
        elif token.type == 'SAIR':
            sair()
            fim = True
        elif token.type == 'SALDO':
            saldo()
        else:
            print('Operação não suportada')
    if fim: break
    print('>> ',end='', flush=True)

