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
|1   | água | 50c   |
|2   | bolo | 60c   |
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

