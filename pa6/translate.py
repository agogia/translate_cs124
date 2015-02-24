import json
import nltk
from nltk.corpus import cess_esp
from nltk import UnigramTagger

def main():
  withChanges = raw_input("Do you want to run the complex version? (type 'yes' or 'no'): ")
  if withChanges== "yes":
    run_translation(True)
  else:
    run_translation(False)
  

def run_translation(withChanges):
  if withChanges==False:
    translation_file = open('translations.json', 'r')
    translations = json.load(translation_file)
    count = 1
    f = open('Corpus.txt', 'r')
    for line in f:
      line = line.decode("utf8")
      line = line.strip('\n')
      words_in_line = line.split(' ')
      translated_sentence = []
      print words_in_line
      for word in words_in_line:
        print word
        if word in translations:
          translated_sentence.append(translations[word])
        else:
          translated_sentence.append(word)
      translated_sentence = ' '.join(translated_sentence)
      print str(count) + '. ' + translated_sentence
      count += 1

  else:
    run_complex_translation()


def run_complex_translation():
  translation_file = open('translations.json', 'r')
  translations = json.load(translation_file)
  count = 1
  f = open('Corpus.txt', 'r')
  # This is from the NLTK toolkit
  cess_sents = cess_esp.tagged_sents()
  unigramTagger = UnigramTagger(cess_sents)

  for line in f:

    words_in_line = nltk.word_tokenize(line)
    print words_in_line
    taggedWords = unigramTagger.tag(words_in_line)

    for index in xrange(0,len(taggedWords)):
      currWord = taggedWords[index]
      print currWord[0]
      tag = currWord[1]
      print tag
      if index != len(taggedWords)-1:
        nextWord = taggedWords[index+1]
        if nextWord[0] == "hello":
          pass

    count += 1


if __name__ == '__main__':
  main()