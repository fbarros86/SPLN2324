#!/usr/bin/env python3
'''
NAME
   word_freq - Calculate word frequency of a text

SYNOPSIS
   word_freq [options] input_files
   options:
    -m 20 - Shows 20 most frequent words
    -n - Shows words ordered alphabetically
    -i - capitilization by referencial
    -f - Filtrar pela frequência comparada com tabela de ocurrências

Description'

FILES:
    https://www.linguateca.pt/acesso/tokens/formas.cetenfolha.txt -- tabela ocorrências de referência
'''

from jjcli import * 
import re
from collections import Counter
__version__ = "0.1.0"




def tokeniza(texto):
    palavras = re.findall(r"\w+(?:\-\w+)?",texto)
    pontuacao = re.findall(r"[;,.:!?_—]+",texto)
    print(f"Tem {len(palavras)} palavras e {len(pontuacao)} sinais")
    return palavras + pontuacao

#file = sys.argv[1]
#out = sys.argv[2]
def main():
    counter = Counter()

    cl=clfilter("f:inm:", doc=__doc__)     ## option values in cl.opt dictionary
    for txt in cl.text():     ## process one file at the time
        listaPal = tokeniza(txt)
        counter = Counter(listaPal)
        eliminar = []
        if "-i" in cl.opt:
            for elem,count in counter.items():
                if 'A'<=elem[0]<='Z':
                    elem2 = elem.lower()
                    if elem2 in counter:
                        if counter[elem2] > count:
                            counter[elem2]+=count
                            eliminar.append(elem)
                        else:
                            counter[elem]+=counter[elem2]
                            eliminar.append(elem2)
            for elem in eliminar:
                counter.pop(elem)   
        if "-f" in cl.opt:
            eliminar = []
            #ler o ficheiro e por 
            with open("data/wordTablePT.txt") as f:
                frequenciesRatio = {}
                totalFreq = int(f.readline())
                for line in f.readlines():
                    word,frequency  = line.split(" ")
                    frequenciesRatio[word]=int(frequency)/totalFreq
            total_frequency = sum(counter.values())
            for elem,n in counter.items():
                if elem in frequenciesRatio:
                    ratio = (n/total_frequency)/frequenciesRatio[elem]
                    if ratio<2:
                        if elem in frequenciesRatio:
                            eliminar.append(elem)
            for elem in eliminar:
                counter.pop(elem)     
                
        listCounter = list(counter.items())
        if "-n" in cl.opt:  listCounter.sort(key = lambda a: a[0])
        else:  listCounter.sort(key = lambda a: -a[1])
        if "-m" in cl.opt:  
            for word, frequency in listCounter[:int(cl.opt.get("-m"))]:
                if "-n" in cl.opt: print(f"{word}: {frequency}")
                else: print(f"{frequency}: {word}")
        else:
            for word, frequency in listCounter:
                if "-n" in cl.opt: print(f"{word}: {frequency}")
                else: print(f"{frequency}: {word}")

# if __name__ == '__main__':
#     main()