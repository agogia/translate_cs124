import collections

def main():
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

if __name__ == '__main__':
  main()