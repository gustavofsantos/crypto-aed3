import string
from itertools import permutations

def totalOfCombinations():
    comb = (10 + 2*26)**8
    return comb

def numberChunksByChunkSize(chunkSize):
    comb = totalOfCombinations();
    numberChunks = comb / chunkSize
    return numberChunks

def digits():
  return string.digits

def lowerletters():
  return string.ascii_lowercase

def upperletters():
  return string.ascii_uppercase

def genCombinations():
  data = list(digits() + lowerletters() + upperletters())
  combinations = list(permutations(data, 8))
  return combinations

def main():
  combinations = genCombinations()
  file = open('combinations.txt', 'w')
  print(combinations)

if __name__ == '__main__':
  main()