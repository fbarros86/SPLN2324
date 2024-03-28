# Contador de Ocorrências de Palavras

## Autor
Francisca Quintas Monteiro de Barros

## UC
SPLN

## Resumo

Esta script calcula a frequência de palavras num texto. A script calcula a frequência de palavras num texto, escrevendo o resultado para o terminal, de acordo com as flags. Por default, ele imprime todas as palavras com a respetiva ocorrência, por ordem descrescente de ocorrências.

## Flags

O programa possui várias flags possíveis:

- `-m 20`: Mostra as 20 palavras mais frequentes.
- `-n`: Mostra as palavras ordenadas alfabeticamente.
- `-i`: Realiza a capitalização preferencial.
- `-f`: Filtra as palavras pela frequência comparada com uma tabela de ocorrências.

## Exemplos

Aqui estão alguns exemplos de como utilizar o programa:

```bash
# Contar as 20 palavras mais frequentes no arquivo texto.txt
wfreq -m 20 texto.txt

# Mostrar as palavras em ordem alfabética no arquivo texto.txt
wfreq -n texto.txt

# Executar o programa com capitalização por referência no arquivo texto.txt
wfreq -i texto.txt

# Filtrar as palavras no arquivo texto.txt pela frequência comparada com uma tabela de ocorrências
wfreq -f texto.txt

```

## Instalação


Para instalar o programa wfreq, apenas é necessário correr o comando:
```shell
pip install .
``````
