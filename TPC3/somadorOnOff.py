import re
import pdb
def somadorOnOff(file):
    linhas = file.split('\n')
    somaGlobal = 0

    # 0 -> OFF 1 -> ON
    i = 0

    for linha in linhas:
        lista = re.findall(r'on|off|=|[+-]?\d+', linha, re.I)

        for s in lista:
            s = s.lower()
            if "on" == s:
                i = 1
            elif "off" == s:
                i = 0
            elif "=" == s:
                print("soma: " + str(somaGlobal))
            else:
                if i == 1:
                    somaGlobal += int(s)
'''
    lista = re.findall(r'on|off|=|[+-]?\d+', linha, re.I)

    for s in lista:
        s = s.lower()
        if "on" == s:
            i = 1
        elif "off" == s:
            i = 0
        elif "=" == s:
            print("soma: " + str(somaGlobal))
        else:
            if i == 1:
                somaGlobal += int(s)
'''
with open("file.txt", 'r', encoding='utf-8') as file:
    file = file.read()

somadorOnOff(file)

