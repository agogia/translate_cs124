import json

def main():
  withChanges = raw_input("Do you want to run the complex version? (type 'yes' or 'no'): ")
  if withChanges== "yes":
    pass
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
      for word in words_in_line:
        if word in translations:
          translated_sentence.append(translations[word])
        else:
          translated_sentence.append(word)
      translated_sentence = ' '.join(translated_sentence)
      print str(count) + '. ' + translated_sentence
      count += 1


if __name__ == '__main__':
  main()