import goslate
import json
import sys

gs = goslate.Goslate()
initial_lang = 'es'
target_lang = 'en'

def main():
  translations = {}
  words = set()
  word_file = sys.argv[1]
  with open(word_file, 'r') as f:
    for line in f:
      line = line.strip('\n')
      words.add(line)
  for word in words:
    translated = gs.translate(word, target_lang, initial_lang)
    translations[word] = translated
  with open('translations.json', 'w') as saved_dictionary:
    saved_dictionary.write(json.dumps(translations))


if __name__ == '__main__':
  main()