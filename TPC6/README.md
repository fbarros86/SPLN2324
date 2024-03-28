# Script para encontrar o melhor(es) amigo(s) de cada personagem

## Autor
Francisca Quintas Monteiro de Barros

## UC
SPLN

## Resumo


Script para analisar as várias entidades presentes num texto e identificar os seus melhores amigos.

Para tal usa a biblioteca `Spacy`, que permite identificar as entidades. Para cada frase, se existirem 2 ou mais entidades, a relação entre elas é guardada.

Existe um dicionário que relaciona todas as entidades a um respetivo Counter cuja chhave é outra entidade e o valor o número de vezes que as duas aparecem numa mesma frase.



## Execução

Para poder executar esta script, primeiramente é necessário correr os seugintes comandos:
```bash 

pip install -U spacy
python -m spacy download pt_core_news_lg

```



Finalmente, apenas é necessário correr o comando:
```bash
python3 findBesties.py > HP.txt
```