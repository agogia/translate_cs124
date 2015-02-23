#Eric test comment



import json

def main():
  translation_file = open('translations.json', 'r')
  translations = json.load(translation_file)
  count = 1
  f = open('Corpus.txt', 'r')
  for line in f:
    line = line.decode("utf8")
    line = line.strip('\n')
    words_in_line = line.split(' ')
    translated_sentence = []
    for word in words_in_line:
      if word in translations:
        translated_sentence.append(translations[word])
      else:
        translated_sentence.append(word)
    translated_sentence = ' '.join(translated_sentence)
    print str(count) + '. ' + translated_sentence
    count += 1

    dummyVar = 27



if __name__ == '__main__':
  main()