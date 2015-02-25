
# -*- coding: utf-8 -*-
import json
import string
# import nltk
import sys
import collections
import re
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
  fix_numbers(sentences_to_translate)
  fix_punctuation_at_start(sentences_to_translate)

def fix_punctuation_at_start(sentences_to_translate):
  punctuationToRemove = ["¿".decode("utf8"), "¡".decode("utf8")]
  for sentence in sentences_to_translate:
    firstWord = sentence[0]
    if firstWord[0] in punctuationToRemove:
      sentence[0] = firstWord[1:]


def fix_numbers(sentences_to_translate):
  for sentence in sentences_to_translate:
    for i in xrange(0,len(sentence)):
      word = sentence[i]
      numberPattern = re.compile(r"[0-9](\.)[0-9]")
      if len(numberPattern.findall(word)) != 0:
        word = word.replace(".", ",")
        sentence[i] = word
      else:
        otherNumberPattern = re.compile(r"[0-9],[0-9]")
        if len(otherNumberPattern.findall(word)) != 0:
          word = word.replace(",", ".")
          sentence[i] = word


def translate_sentences(sentences_to_translate, translations):
  translated_sentences = []
  for sentence in sentences_to_translate:
    translated_sentence = []
    for word in sentence:
      if word in translations:
        translated_sentence += translations[word][0].split(' ')
      else:
        translated_sentence.append(word)
    translated_sentences.append(translated_sentence)
  return translated_sentences

def capitalize_first_word(translated_sentences):
  for sentence in translated_sentences:
    sentence[0] = sentence[0].title()

def post_process(translated_sentences):
  capitalize_first_word(translated_sentences)
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