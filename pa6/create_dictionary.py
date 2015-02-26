import json
import sys
import collections

initial_lang = 'es'
target_lang = 'en'

def main():
  f = open('DictionaryTextFile.txt', 'r')
  dictionary = collections.defaultdict(list)
  for line in f:
    wordList = []
    colonSplit = line.split(": ")
    spanishWord = colonSplit[0]
    translations = colonSplit[1]
    while (True):
      commaIndex = str.find(translations, ",")
      if(commaIndex > 0):
        englishWord = translations[0:commaIndex]
        translations = translations[commaIndex+2:]
        wordList.append(englishWord)
      else:
        endIndex = len(translations)-1
        if spanishWord == "y":
          endIndex += 1
        englishWord = translations[0:endIndex]
        wordList.append(englishWord)
        break
    dictionary[spanishWord] = wordList
  with open('translations.json', 'w') as saved_dictionary:
    saved_dictionary.write(json.dumps(dictionary))


if __name__ == '__main__':
  main()