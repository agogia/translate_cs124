
# -*- coding: utf-8 -*-
import json
import nltk
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
        translated_sentence.append(translations[word][0])
      else:
        translated_sentence.append(word)
    translated_sentences.append(translated_sentence)
  return translated_sentences


def post_process(translated_sentences):
  split_words_with_spaces(translated_sentences)
  switch_nouns_and_adjectives(translated_sentences)

# Sometimes verbs will be translated into "I ran" and will be treated as one word in post-processing even though they are two
def split_words_with_spaces(translated_sentences):
  for j in xrange(0,len(translated_sentences)):
    sentence = translated_sentences[j]
    newSentence = []
    for i in xrange(0,len(sentence)):
      word = sentence[i]
      word = word.split()
      for aWord in word:
        newSentence.append(aWord)
    translated_sentences[j] = newSentence

def switch_nouns_and_adjectives(translated_sentences):
  nounTags = ["NN", "NNP", "NNPS", "NNS"]
  adjTags = ["JJ", "JJR", "JJS"]

  for sentence in translated_sentences:
    tagged_sentence = nltk.pos_tag(sentence)
    for i in xrange(0,len(tagged_sentence)-1):
      currWordEntry = tagged_sentence[i]
      nextWordEntry = tagged_sentence[i+1]
      if currWordEntry[1] in nounTags and nextWordEntry[1] in adjTags:
        print sentence[i] + " " + sentence[i+1]
        adjective = sentence[i+1]
        sentence[i+1] = sentence[i]
        sentence[i] = adjective

    # print tagged_sentence

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