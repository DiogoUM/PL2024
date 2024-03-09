# TPC4
- **Título:** Analisador léxico

## Autor
- **Nome:** Diogo Cardoso Ferreira
- **ID:** a94877

## Descrição
Este TPC tem como objetivo construir um analizador léxico para:
`Select id,nome,salario from empregados where salario >= 820;`

Para a construção deste analisador léxico foi necessário identificar os tokens presentes no exemplo, e além destes, os possíveis tokens que poderiam aparecer em outras "frases".

Os tokens definidos foram os seguintes:

- PR --> palavras reservadas
- OP --> **<=, >=, <, >** (é de notar que a ordem com que estes aparecem no regex é relevante)
- NOME --> identificadores dos atributos e tabelas
- ALL --> **\***
- V --> **,**
- INT --> inteiros
- FLOAT --> floats
- LP --> **\(**
- RP --> **\)**
- PV --> **;**
- NL --> *new line*, isto é, quando aparece o caracter **\n**

Posteriormente foram também definidas as expressões regulares para cada um dos *tokens*.

É também importante referir que a ordem com que a funções `t_FLOAT` e `t_INT` aparecem é relevante para o funcionamento do analizador. A função `t_FLOAT` tem de aparecer primeiro que a função `t_INT`, para que seja possível diferenciar os *float* de *int*.

