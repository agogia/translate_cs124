import json
# import nltk
import sys
import collections
# from nltk.corpus import cess_esp
# from nltk import UnigramTagger


file_name = 'Corpus.txt'

def get_translation_dictionary():
  translation_file = open('translations.json', 'r')
  translations = json.load(translation_file)
  return translations

def get_sentences_from_file():
  sentences = []
  f = open(file_name, 'r')
  for line in f:
    line = line.decode("utf8")
    line = line.strip('\n')
    words_in_line = line.split(' ')
    sentences.append(words_in_line)
  return sentences

def pre_process(sentences_to_translate):
  return

def translate_sentences(sentences_to_translate, translations):
  translated_sentences = []
  for sentence in sentences_to_translate:
    translated_sentence = []
    for word in sentence:
      if word in translations:
        translated_sentence.append(translations[word][0])
      else:
        translated_sentence.append(word)
    translated_sentences.append(translated_sentence)
  return translated_sentences

def post_process(translated_sentences):
  return

def print_sentences(translated_sentences):
  count = 1
  for sentence in translated_sentences:
    translated_sentence = ' '.join(sentence)
    print str(count) + '. ' + translated_sentence
    count += 1

def main():
  translations = get_translation_dictionary()
  sentences_to_translate = get_sentences_from_file()
  pre_process(sentences_to_translate)
  translated_sentences = translate_sentences(sentences_to_translate, translations)
  post_process(translated_sentences)
  print_sentences(translated_sentences)


if __name__ == '__main__':
  main()