# -*- coding: utf-8 -*-
import json
import nltk
from nltk.corpus import cess_esp as cess
from nltk import UnigramTagger as ut
import pickle

def main():
  cess_sents = cess.tagged_sents()
  uni_tag = ut(cess_sents)
  with open('unigramTagger.json', 'wb') as output:
    pickle.dump(uni_tag, output, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
  main()