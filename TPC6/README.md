# TPC6
- **Título:** GIC LL(1)

## Autor
- **Nome:** Diogo Cardoso Ferreira
- **ID:** a94877

## Descrição
Para o desenvolvimento deste TPC foi pedido o desenvolvimento de uma GIC (Gramática Independente de Contexto) LL(1) para o seguinte exemplo:
```
? a
b = a * 3 / ( 27 - 3 )
! a + b
c = a * b / ( a / b )
```
Onde o caracter de '?' representa uma operação de *input* e o '!' representa uma operação de *print*.   
É necessário para esta gramática garantir a prioridade dos operadores, garantir a propriedade LL(1) e ainda calcular os "Look ahead" de cada produção.


## Resolução
```
Produções                           "Look ahead" de cada produção


PROGRAMA -> LINHA PROGRAMA          {'?',VAR,'!'}    
          | &                       {$}

LINHA -> '?' VAR                    {'?'}    
       | VAR '=' EXP                {VAR}    
       | '!' EXP                    {'!'}    

EXP -> TERMO SSop                   {'(',NUM,VAR}

SSop -> '+' EXP                     {'+'}    
      | '-' EXP                     {'-'}    
      | &                           {')'}    

TERMO -> FATOR MDop                 {'(',NUM,VAR}    

MDop -> '*' TERMO                   {'\*'}    
      | '/' TERMO                   {'/'}    
      | &                           {')'}    

FATOR -> '(' EXP ')'                {'('}    
       | NUM                        {NUM}    
       | VAR                        {VAR}
```
