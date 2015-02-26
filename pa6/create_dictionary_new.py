import math, collections

def main():
<<<<<<< HEAD
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
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
=======
>>>>>>> Stashed changes
=======
>>>>>>> origin/master
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

    print(dictionary["caja"])
  	


  	# translations = {}
  	# words = set()
  	# word_file = sys.argv[1]
  	# with open(word_file, 'r') as f:
   #  	for line in f:
   #    	line = line.strip('\n')
   #    	words.add(line)
  	# for word in words:
   #  	translated = gs.translate(word, target_lang, initial_lang)
   #  	translations[word] = translated
  	# with open('translations.json', 'w') as saved_dictionary:
   #  	saved_dictionary.write(json.dumps(translations))
<<<<<<< HEAD
<<<<<<< Updated upstream
=======
>>>>>>> eric-test
>>>>>>> Stashed changes
=======
>>>>>>> origin/master

if __name__ == '__main__':
  main()