# TPC2
- **Título:** Conversor de MD para HTML

## Autor
- **Nome:** Diogo Cardoso Ferreira
- **ID:** a94877

## Descrição
Criar em python um conversor de ficheiros MarkDown para ficheiros HTML para alguns elementos como:
 - Cabeçalhos
 - Bold
 - Itálico
 - Listas não ordenadas
 - Listas ordenadas
 - Imagens
 - Links

## Resolução
A realização deste trabalho consistiu principalmente na utilização de expressões regulares.
Começando por tratar cada linha do MD, primeiramente para os cabeçalhos foi identificado se a linha
começa com a marca '#' e usada a função 'split' para indentificar o nível do cabeçalho contando a quantidade de '#'.

Para o Bold, Itálico, Imagens e Links, foi usada a função 'sub' do modulo 're' acompanhada
das expressões regulares para tratar cada caso.

Para as listas além de fazer algo semelhante aos cabeçalhos para a identificação da marca, também
foram usados dois boolenos para ser possivel identificar quando é necessário indicar as **tags**
de abertura e fecho das listas.
