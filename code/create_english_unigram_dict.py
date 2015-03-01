import json
import sys
import collections
import math

def main():
  f = open('count_1w.txt', 'r')
  dictionary = collections.defaultdict(lambda: 0)
  total = 0.0
  for line in f:
  	line = line.split()
  	value = math.log(float(line[1]))
  	dictionary[line[0]] = value
  	total+=value

  for key in dictionary:
  	dictionary[key] = dictionary[key]/total

  with open('unigramdict.json', 'w') as saved_dictionary:
  	saved_dictionary.write(json.dumps(dictionary))





if __name__ == '__main__':
  main()