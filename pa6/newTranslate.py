import collections

def main():
  dictionary = createDictionary()
  f = open('Corpus.txt', 'r')
  count = 1
  for line in f:
    line = line.decode("utf8")
    line = line.strip('\n')
    words_in_line = line.split(' ')
    translated_sentence = []
    for word in words_in_line:
      if word in dictionary:
        translated_sentence.append(dictionary[word][0])
      else:
        translated_sentence.append(word)
    translated_sentence = ' '.join(translated_sentence)
    print str(count) + '. ' + translated_sentence
    count += 1
  
def createDictionary():
  f = open('DictionaryTextFile.txt', 'r')
  count = 0
  dictionary = collections.defaultdict(list)
  for line in f:
    wordList = []
    colonIndex = str.find(line, ":")
    foreignWord = line[0:colonIndex]
    line = line[colonIndex+2:]
    while (True):
      commaIndex = str.find(line, ",")
      if(commaIndex > 0):
        englishWord = line[0:commaIndex]
        line = line[commaIndex+2:]
        wordList.append(englishWord)
      else:
        englishWord = line[0:len(line)-1]
        wordList.append(englishWord)
        break
    dictionary[foreignWord] = wordList

  return dictionary


if __name__ == '__main__':
  main()