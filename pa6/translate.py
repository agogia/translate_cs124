import json
# import nltk
import sys
import collections
# from nltk.corpus import cess_esp
# from nltk import UnigramTagger

def main():
  withChanges = raw_input("Do you want to run the complex version? (type 'yes' or 'no'): ")
  if withChanges== "yes":
    run_translation(True)
  else:
    run_translation(False)
  

def run_translation(withChanges):
  print '-------'
  if withChanges==False:
    translation_file = open('translations.json', 'r')
    translations = json.load(translation_file)
    count = 1
    f = open('Corpus.txt', 'r')
    for line in f:
      line = line.decode("utf8")
      line = line.strip('\n')
      words_in_line = line.split(' ')
      print words_in_line
      translated_sentence = []
      for word in words_in_line:
        if word in translations:
          translated_sentence.append(translations[word][0])
        else:
          translated_sentence.append(word)
      translated_sentence = ' '.join(translated_sentence)
      print str(count) + '. ' + line
      print ' '
      print str(count) + '. ' + translated_sentence
      print '-----------'
      count += 1

  else:
    run_complex_translation()


def run_complex_translation():


if __name__ == '__main__':
  main()