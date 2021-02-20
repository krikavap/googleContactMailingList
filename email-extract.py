import re
import sys, os

vystup = ""     # iniciace proměnné
os.remove('contacts-output.csv')      # vymazání starého výstupního souboru

regex = r"([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})"     # regulární výraz vyhledávající platnou e-mailovou adresu

with open('contacts.csv', encoding='utf-8') as b_file:          # otevře vstupní soubor
    for b_line in b_file:                                       # čte řádku po řádce
        matches = re.finditer(regex, b_line)                    # hledá řetězec, vyhovující regulárnímu výrazu pro platnou e-mailovou adresu
        for matchNum, match in enumerate(matches, start=1):
            
            ou_line = ("{match};".format(match = match.group()))        # adresu uloží do ou_line a na konec přidá středník ;
            vystup = vystup + ou_line                                   # ou_line přidá do vystupu
    print(vystup)                   # kontrolní tisk výstupu na terminál
    with open('contacts-output.csv', mode = 'a', encoding='utf-8') as a_output:       # a zapíše řádek vystup na konec souboru
        a_output.write(vystup)   
    