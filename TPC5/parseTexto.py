# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy
import sys
from spacy import displacy

nlp = spacy.load("pt_core_news_lg")

with open(sys.argv[1]) as file:
    content = file.read()

doc = nlp(content)

# displacy.serve(doc,style="dep")
# https://universaldependencies.org/u/pos/
translate = {"ADJ":"adjetivo",
             "ADP":"proposição",
             "ADV":"advérbio",
             "AUX": "auxiliar",
            "CCONJ": "conjunção coordenativa",
            "DET": "determinante",
            "INTJ": "interjeção",
            "NOUN": "nome",
            "NUM": "número",
            "PART": "particula",
            "PRON": "pronome",
            "PROPN": "nome próprio",
            "PUNCT": "pontuação",
            "SCONJ": "conjunção subordinada",
            "SYM": "simbolo",
            "VERB": "verbo",
            "X": "outro",
            "SPACE": "espaço"
             }


with doc.retokenize() as retokenizer:
    for entity in doc.ents:
        retokenizer.merge(entity)
        

print("| Palavra | Tipo | Lema |Dep|Children|\n|----|--------|----|--------|--------|")
for sentence in doc.sents:
    for token in sentence:
        if token.pos_=="PROPN":
             print("|",token.text,"|", translate[token.pos_],"|",token.ent_type_,"|",token.dep_,"|",list(token.children),"|")
        elif token.pos_!="PUNCT" and token.pos_!="SPACE" :
             print("|",token.text,"|", translate[token.pos_],"|",token.lemma_,"|",token.dep_,"|",list(token.children),"|")
    print("|---- | ----|---- | ---- | ---- |")

    
