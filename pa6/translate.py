
# -*- coding: utf-8 -*-
import json
import nltk
import string
import sys
import collections
import re


file_name = 'Corpus.txt'

def get_translation_dictionary():
  translation_file = open('translations.json', 'r')
  translations = json.load(translation_file)
  return translations

def get_unigram_dictionary():
  unigram_file = open('unigramdict.json', 'r')
  unigrams = json.load(unigram_file)
  return unigrams

def get_bigram_dictionary():
  bigram_file = open('bigramdict.json', 'r')
  bigrams = json.load(bigram_file)
  return bigrams

def get_sentences_from_file():
  sentences = []
  f = open(file_name, 'r')
  for line in f:
    sentence = []
    line = line.decode("utf8")
    line = line.strip('\n')
    words_in_line = line.split(' ')
    for words in words_in_line:
      split_words = re.split('([¿,.()\"?:])', words)
      for word in split_words:
        if word != '':
          sentence.append(word)
    # print sentence
    sentences.append(sentence)
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
  unigramDict = get_unigram_dictionary()
  bigramDict = get_bigram_dictionary()
  translated_sentences = []
  for sentence in sentences_to_translate:
    translated_sentence = []
    for index in xrange(0,len(sentence)):
      word = sentence[index]
      if word in translations:
        to_add = choose_right_word(index, translations, translated_sentence, unigramDict, bigramDict, sentence)
        translated_sentence.append(to_add)
      else:
        translated_sentence.append(word)
    translated_sentences.append(translated_sentence)
  return translated_sentences

def choose_right_word(index, translations, translated_sentence, unigramDict, bigramDict, spanishSentence):
  spanishWord = spanishSentence[index]
  topScore = 0.0
  topWord = ""
  runFullTranslation = True
  firstWord = True
  if index != 0:
    firstWord = False
    previousWord = translated_sentence[index-1]
    phrase = spanishSentence[index-1] + " " + spanishWord
    # print phrase
    comoPattern = re.compile(r"[Cc]ómo se".decode("utf8"))
    if len(comoPattern.findall(phrase)) != 0:
      translated_sentence[index-1] = "how does"
      topWord = "one"
      runFullTranslation = False

    howeverPattern = re.compile(r"[Nn]o obstante".decode("utf8"))
    if len(howeverPattern.findall(phrase)) != 0:
      translated_sentence[index-1] = "however"
      runFullTranslation = False



  if runFullTranslation:
    for word in translations[spanishWord]:
      score = 0.0
      bigramScore = 0.0

      if word in unigramDict:
        unigramScore = unigramDict[word]
        score = unigramScore
        # print unigramScore
        if not firstWord:
          if previousWord in bigramDict:
            if word in bigramDict[previousWord]:
              bigramScore = bigramDict[previousWord][word]
              
          score+=9*bigramScore
              # print bigramScore

      if score >=topScore:
        topScore = score
        topWord = word

  return topWord

def capitalize_first_word(translated_sentences):
  for sentence in translated_sentences:
    sentence[0] = sentence[0].title()

def post_process(translated_sentences):
  capitalize_first_word(translated_sentences)
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