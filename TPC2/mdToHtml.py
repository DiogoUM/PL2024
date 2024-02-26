import re


def markdown_para_html(texto_md):
    linhas = texto_md.split('\n')
    html = ''

    dentro_lista = False
    dentro_lista_ordenada = False
    for linha in linhas:
        # Cabeçalhos
        if linha.startswith('#'):
            titulo = linha.split()
            cardinais = titulo[0]
            nivel = len(cardinais)
            tag = f'h{nivel}'
            conteudo = linha[nivel + 1:]
            html += f'<{tag}>{conteudo}</{tag}>\n'
        else:
            # Imagens
            linha = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', linha)

            # Links
            linha = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', linha)

            # Negrito e itálico
            linha = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', linha)  # Negrito
            linha = re.sub(r'\*(.*?)\*', r'<i>\1</i>', linha)  # Itálico

            # Lista não ordenada
            if linha.startswith('- '):
                if not dentro_lista:
                    html += '<ul>\n'
                    dentro_lista = True
                linha = re.sub(r'^- (.*)', r'<li>\1</li>', linha)

            # Lista ordenada
            elif re.match(r'^\d+\. .*', linha):
                if not dentro_lista_ordenada:
                    html += '<ol>\n'
                    dentro_lista_ordenada = True
                linha = re.sub(r'^\d+\.\s+(.*)', r'<li>\1</li>', linha)

            # Verifica se a lista não continua na próxima linha
            elif dentro_lista or dentro_lista_ordenada:
                if dentro_lista:
                    html += '</ul>\n'
                    dentro_lista = False
                if dentro_lista_ordenada:
                    html += '</ol>\n'
                    dentro_lista_ordenada = False

            html += linha + '\n'

    # Verifica se alguma lista não foi fechada no final do texto
    if dentro_lista:
        html += '</ul>\n'
    if dentro_lista_ordenada:
        html += '</ol>\n'

    return html


# Lê o arquivo Markdown
with open("file.md", 'r', encoding='utf-8') as md:
    texto_md = md.read()

# Converte Markdown para HTML
html_resultante = markdown_para_html(texto_md)

# Escreve o HTML resultante em um arquivo HTML
with open("file.html", 'w', encoding='utf-8') as file:
    file.write(html_resultante)

# Exibe o HTML resultante
print(html_resultante)
