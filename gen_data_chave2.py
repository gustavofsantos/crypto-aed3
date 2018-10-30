import string
from itertools import product

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
  data = digits() + lowerletters() + upperletters()
  perm = list(map(lambda p: "".join(p) + "\n", product(data, repeat=4)))
  return perm

def main():
  combinations = genCombinations()
  file = open('combinations.txt', 'w')
  file.writelines(combinations)
  # print(combinations)

if __name__ == '__main__':
  main()