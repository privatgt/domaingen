#!/usr/bin/python3
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.corpus import wordnet as wn
import json, whois, pickle, atexit, inflect
engine = inflect.engine()
words = list()
def checkl(name):
    try:
        print(name+".com",domain.registrar)
        return False
    except:
        print(name+".com","Free")
        return name+".com"

wordlist=input("company name: ").split(":")
i=0
def exit_handler():
    print(list(set([x for x in words if x is not None])),list(set([x for x in wordlist if x is not None])))
    data=json.dumps(list(set([x for x in words if x is not None])), separators=("\n", "\n"))
    wors=json.dumps(list(set([x for x in wordlist if x is not None])), separators=("\n", "\n"))
    f = open("names.json", "a")
    f.write(data)
    f.close()
    f = open("list.json", "a")
    f.write(wors)
    f.close()
atexit.register(exit_handler)
WN_NOUN = 'n'
WN_VERB = 'v'
WN_ADJECTIVE = 'a'
WN_ADJECTIVE_SATELLITE = 's'
WN_ADVERB = 'r'
j =["a","r","n","v","s"]
def convert(word, from_pos, to_pos):    
    """ Transform words given from/to POS tags """

    synsets = wn.synsets(word, pos=from_pos)

    # Word not found
    if not synsets:
        return []

    # Get all lemmas of the word (consider 'a'and 's' equivalent)
    lemmas = []
    for s in synsets:
        for l in s.lemmas():
            if s.name().split('.')[1] == from_pos or from_pos in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE) and s.name().split('.')[1] in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE):
                lemmas += [l]

    # Get related forms
    derivationally_related_forms = [(l, l.derivationally_related_forms()) for l in lemmas]

    # filter only the desired pos (consider 'a' and 's' equivalent)
    related_noun_lemmas = []

    for drf in derivationally_related_forms:
        for l in drf[1]:
            if l.synset().name().split('.')[1] == to_pos or to_pos in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE) and l.synset().name().split('.')[1] in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE):
                related_noun_lemmas += [l]

    # Extract the words from the lemmas
    words = [l.name() for l in related_noun_lemmas]

    # Build the result in the form of a list containing tuples (word, probability)
    result = words

    # return all the possibilities sorted by probability
    return result

try:
    while True:
        wordlist=[x for x in wordlist if x is not None]
        words=[x for x in words if x is not None]
        for w in wordlist:
            wordlist=[x for x in wordlist if x is not None]
            words=[x for x in words if x is not None]
            if "-" in w:
                i-=1
            elif "_" in w:
                i+=1
            else:
                try:
                    wordlist.append(w+'-'+wordlist[i])
                    i+=1
                    print(i,w)
                except:
                    i-=1
            for synset in wn.synsets(w):
                jk=list(set(synset.lemmas()))
                for lemma in jk:
                    try:
                        if lemma.name() != "":
                            words = list(set(words))
                            print(lemma.name()+".com")
                            domain = whois.query(lemma.name()+".com")
                    except:
                        domain = whois.query("google.com")
                        print(lemma.name()+".com","Free")
                        words.append(lemma.name()+".com")
                        words = list(set(words))
                        wordlist.append(lemma.name())
                    if lemma.antonyms(): 
                        for lemma in lemma.antonyms():
                            check=checkl(lemma.name())
                            if check:  
                                words = list(set(words))
                                words.append(check)  
                                wordlist.append(lemma.name())
                                wordlist.append(lemma.name()+"ly")
                                wordlist.append(lemma.name()+"ny")
                                wordlist.append(lemma.name()+"ator")
                                wordlist.append("anti"+lemma.name())
                                wordlist.append("de"+lemma.name())
                                wordlist.append("un"+lemma.name())
                                for v in j:
                                    for m in reversed(j):
                                        wordlist+=convert(lemma.name(), j, m)
                                wordlist.append(engine.plural(lemma.name()))
                                wordlist.append(wn.morphy(lemma.name(), pos=wn.NOUN))
                                wordlist.append(wn.morphy(lemma.name(), pos=wn.VERB))
                                wordlist.append(lemmatizer.lemmatize(lemma.name(),"v"))
                                wordlist.append(lemmatizer.lemmatize(lemma.name()))
                                wordlist.append(lemmatizer.lemmatize(lemma.name(),pos="a"))
                                wordlist=list(set(wordlist))
                    check=checkl(lemma.name())
                    if check:
                        words = list(set(words))
                        words.append(check)
                        wordlist.append(lemma.name()+"ly")
                        wordlist.append(lemma.name()+"ify")
                        wordlist.append(lemma.name()+"fy")
                        wordlist.append(lemma.name()+"ny")
                        wordlist.append(lemma.name()+"ator")
                        wordlist.append(lemma.name()+"nor")
                        wordlist.append(lemma.name()+"izator")
                        wordlist.append(lemma.name()+"ization")
                        wordlist.append(lemma.name()+"ity")
                        wordlist.append(lemma.name()+"ate")
                        if lemma.name()[-1]=="e":
                            wordlist.append(lemma.name()+"r")
                            wordlist.append(lemma.name()[:-1]+"or")
                        else:
                            wordlist.append(lemma.name()+"er")
                            wordlist.append(lemma.name()+"or")
                        for v in j:
                            for m in reversed(j):
                                print(lemma.name(),m,v,convert(lemma.name(), v, m))
                                wordlist+=convert(lemma.name(), v, m)
                        wordlist.append(engine.plural(lemma.name()))
                        wordlist.append(wn.morphy(lemma.name(), pos=wn.NOUN))
                        wordlist.append(wn.morphy(lemma.name(), pos=wn.VERB))
                        wordlist.append(lemmatizer.lemmatize(lemma.name(),"v"))
                        wordlist.append(lemmatizer.lemmatize(lemma.name()))
                        wordlist.append(lemmatizer.lemmatize(lemma.name(),pos="a"))
                        wordlist.append(lemma.name())
                        wordlist=list(set(wordlist))
            check=checkl(w)
            if check:  
                domain = whois.query(w+".com")
                words.append(check)
                wordlist.append(w)
            wordlist = list(set(wordlist))
            words=[x for x in words if x is not None]
        words = list(set(words))
except KeyboardInterrupt:
    print('interrupted!')
