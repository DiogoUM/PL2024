# TPC5
- **Título:** Máquina de Vending

## Autor
- **Nome:** Diogo Cardoso Ferreira
- **ID:** a94877

## Descrição
Criar em python um simulador de uma máquina de vending.
Existe um ficheiro onde está guardada uma lista de produtos como por exemplo:

| id | Nome | Preço |
|----|------|-------|
|A23 | água |   0.7 |
...


Comandos como exemplos:

>**>>** LISTAR   
maq:    
cod | nome      | quantidade  |preço    
\---------------------------------------------------   
A23 | água 0.5L  | 8           | 0.7   
...


>**>>** MOEDA 1e,10c,20c  
maq: Saldo = 1e,30c

>**>>** SELECIONAR A23  
maq: Pode retirar o produto dispensado "água 0.5L"  
maq: Saldo = 60c

>**>>** SELECIONAR A23  
maq: Saldo insufuciente para satisfazer o seu pedido    
maq: Saldo = 60c; Pedido = 70c

>**>>** SAIR  
maq: Pode retirar o troco: 1x 50c, 1x 20c e 2x 2c.  
maq: Até à próxima


Para a resolução deste problema foraam primeiramente identificados os tokens necessários para a construção do analisador léxico.

Posteriormente foram desenvolvidas as expressões regulares para a deteção de cada token.

Foi também criado e desenvolvido um ficheiro "produtos.json" para efeitos de demenstração e teste, que contém os produtos referentes a uma máquina de vending.

Por último foram desenvolvidas as funções necessárias para que o programa tenha um comportamento idêntico ao descrito.