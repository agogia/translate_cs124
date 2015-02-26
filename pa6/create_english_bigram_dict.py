import json
import sys
import collections
import math

def main():
  f = open('count_2w.txt', 'r')
  dictionary = collections.defaultdict(dict)
  total = 0.0
  for line in f:
  	line = line.split()
  	value = math.log(float(line[2]))
  	total+=value
  	dictionary[line[0]][line[1]] = value

  for key in dictionary:
  	for secondKey in dictionary[key]:
  		dictionary[key][secondKey] = dictionary[key][secondKey]/total

  with open('bigramdict.json', 'w') as saved_dictionary:
  	saved_dictionary.write(json.dumps(dictionary))





if __name__ == '__main__':
  main()