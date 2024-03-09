import re
import ply.lex as lex

exemplo = "Select id,nome,salario from empregados where salario >= 820;"

tokens = (
    'PR',
    'OP',
    'NOME',
    'ALL',
    'V', 
    'INT',
    'FLOAT',
    'LP',
    'RP',
    'PV', # ;
    'NL'
)

t_PR = r"((?i)select|(?i)from|(?i)where)"
t_OP = r"<=|>=|<|>|="
t_NOME = r"\w+"
t_ALL = r"\*"
t_V = r","
t_LP = r"\("
t_RP = r"\)"
t_PV = r";"

def t_FLOAT(t):
    r'[+-]?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'[+-]?\d+'
    t.value = int(t.value)
    return t

def t_nl(t):
    r'\n'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print("Erro caracter inválido: " + t.value[0])
    t.lexer.skip(1)

t_ignore = '\t '

lexer = lex.lex()
lexer.input(exemplo)

print("TYPE VALUE LINENO LEXPOS")
for t in lexer:
    print(t.type, t.value, t.lineno, t.lexpos)
