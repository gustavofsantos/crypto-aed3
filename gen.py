import string
import os
import sys

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits

chars = lower + upper + digits

initialState = sys.argv[1]
linesPerFile = 2000

def runTest(fileName):
  print('testing file {}...'.format(fileName))
  cmd = 'sh test-sha.sh {}'.format(fileName)
  os.system(cmd)
  print('back to Python')

def initialKey(initialState):
  return list(initialState)

def initialIndexes(initialState):
  vec = list(initialState)
  indexes = []
  for c in vec:
    indexes.append(chars.index(c))

  return indexes

def start(lines=2000000):
  line = 0
  key = initialKey(initialState)
  indexes = initialIndexes(initialState)

  fileName = 'chave2_{}_{}.txt'.format(initialState, lines)
  keys = open(fileName, 'w')

  if len(indexes) == 8:
    for i0 in range(indexes[0] or 0, len(chars)):
      key[0] = chars[i0]
      for i1 in range(indexes[1] or 0,len(chars)):
        key[1] = chars[i1]
        for i2 in range(indexes[2] or 0,len(chars)):
          key[2] = chars[i2]
          for i3 in range(indexes[3] or 0,len(chars)):
            key[3] = chars[i3]
            for i4 in range(indexes[4] or 0,len(chars)):
              key[4] = chars[i4]
              for i5 in range(indexes[5] or 0,len(chars)):
                key[5] = chars[i5]
                for i6 in range(indexes[6] or 0,len(chars)):
                  key[6] = chars[i6]
                  for i7 in range(indexes[7] or 0,len(chars)):
                    key[7] = chars[i7]
                    #print(key)
                    keys.write(''.join(key) + '\n')
                    line += 1
                    if line == lines:
                      keys.close()
                      runTest(fileName)

                      fileName = 'chave2_{}_{}.txt'.format(''.join(key), lines)
                      keys = open(fileName, 'w')

                      line = 0
                  indexes[7] = 0
                indexes[6] = 0
              indexes[5] = 0
            indexes[4] = 0
          indexes[3] = 0
        indexes[2] = 0
      indexes[1] = 0
    indexes[0] = 0
    keys.close()
    runTest(fileName)
  elif len(indexes) == 7:
    for i0 in range(indexes[0] or 0, len(chars)):
      key[0] = chars[i0]
      for i1 in range(indexes[1] or 0,len(chars)):
        key[1] = chars[i1]
        for i2 in range(indexes[2] or 0,len(chars)):
          key[2] = chars[i2]
          for i3 in range(indexes[3] or 0,len(chars)):
            key[3] = chars[i3]
            for i4 in range(indexes[4] or 0,len(chars)):
              key[4] = chars[i4]
              for i5 in range(indexes[5] or 0,len(chars)):
                key[5] = chars[i5]
                for i6 in range(indexes[6] or 0,len(chars)):
                  key[6] = chars[i6]
                  #print(key)
                  keys.write(''.join(key) + '\n')
                  line += 1
                  if line == lines:
                    keys.close()
                    runTest(fileName)
                    fileName = 'chave2_{}_{}.txt'.format(''.join(key), lines)
                    keys = open(fileName, 'w')
                    line = 0

                indexes[6] = 0
              indexes[5] = 0
            indexes[4] = 0
          indexes[3] = 0
        indexes[2] = 0
      indexes[1] = 0
    indexes[0] = 0
    keys.close()
    runTest(fileName)

  elif len(indexes) == 6:
    for i0 in range(indexes[0] or 0, len(chars)):
      key[0] = chars[i0]
      for i1 in range(indexes[1] or 0,len(chars)):
        key[1] = chars[i1]
        for i2 in range(indexes[2] or 0,len(chars)):
          key[2] = chars[i2]
          for i3 in range(indexes[3] or 0,len(chars)):
            key[3] = chars[i3]
            for i4 in range(indexes[4] or 0,len(chars)):
              key[4] = chars[i4]
              for i5 in range(indexes[5] or 0,len(chars)):
                key[5] = chars[i5]
                #print(key)
                keys.write(''.join(key) + '\n')
                line += 1
                if line == lines:
                  keys.close()
                  runTest(fileName)
                  fileName = 'chave2_{}_{}.txt'.format(''.join(key), lines)
                  keys = open(fileName, 'w')
                  line = 0
              indexes[5] = 0
            indexes[4] = 0
          indexes[3] = 0
        indexes[2] = 0
      indexes[1] = 0
    indexes[0] = 0
    keys.close()
    runTest(fileName)

  elif len(indexes) == 5:
    for i0 in range(indexes[0] or 0, len(chars)):
      key[0] = chars[i0]
      for i1 in range(indexes[1] or 0,len(chars)):
        key[1] = chars[i1]
        for i2 in range(indexes[2] or 0,len(chars)):
          key[2] = chars[i2]
          for i3 in range(indexes[3] or 0,len(chars)):
            key[3] = chars[i3]
            for i4 in range(indexes[4] or 0,len(chars)):
              key[4] = chars[i4]
              #print(key)
              keys.write(''.join(key) + '\n')
              line += 1
              if line == lines:
                keys.close()
                runTest(fileName)
                fileName = 'chave2_{}_{}.txt'.format(''.join(key), lines)
                keys = open(fileName, 'w')
                line = 0
            indexes[4] = 0
          indexes[3] = 0
        indexes[2] = 0
      indexes[1] = 0
    indexes[0] = 0
    keys.close()
    runTest(fileName)

  elif len(indexes) == 4:
    for i0 in range(indexes[0] or 0, len(chars)):
      key[0] = chars[i0]
      for i1 in range(indexes[1] or 0,len(chars)):
        key[1] = chars[i1]
        for i2 in range(indexes[2] or 0,len(chars)):
          key[2] = chars[i2]
          for i3 in range(indexes[3] or 0,len(chars)):
            key[3] = chars[i3]
            #print(key)
            keys.write(''.join(key) + '\n')
            line += 1
            if line == lines:
              keys.close()
              runTest(fileName)
              fileName = 'chave2_{}_{}.txt'.format(''.join(key), lines)
              keys = open(fileName, 'w')
              line = 0
          indexes[3] = 0
        indexes[2] = 0
      indexes[1] = 0
    indexes[0] = 0
    keys.close()
    runTest(fileName)

  elif len(indexes) == 3:
    for i0 in range(indexes[0] or 0, len(chars)):
      key[0] = chars[i0]
      for i1 in range(indexes[1] or 0,len(chars)):
        key[1] = chars[i1]
        for i2 in range(indexes[2] or 0,len(chars)):
          key[2] = chars[i2]
          #print(key)
          keys.write(''.join(key) + '\n')
          line += 1
          if line == lines:
            keys.close()
            runTest(fileName)
            fileName = 'chave2_{}_{}.txt'.format(''.join(key), lines)
            keys = open(fileName, 'w')
            line = 0
        indexes[2] = 0
      indexes[1] = 0
    indexes[0] = 0
    keys.close()
    runTest(fileName)

  elif len(indexes) == 2:
    for i0 in range(indexes[0] or 0, len(chars)):
      key[0] = chars[i0]
      for i1 in range(indexes[1] or 0,len(chars)):
        key[1] = chars[i1]
        #print(key)
        keys.write(''.join(key) + '\n')
        line += 1
        if line == lines:
          keys.close()
          runTest(fileName)
          fileName = 'chave2_{}_{}.txt'.format(''.join(key), lines)
          keys = open(fileName, 'w')
          line = 0
      indexes[1] = 0
    indexes[0] = 0
    keys.close()
    runTest(fileName)

  elif len(indexes) == 1:
    for i0 in range(indexes[0] or 0, len(chars)):
      key[0] = chars[i0]
      #print(key)
      keys.write(''.join(key) + '\n')
      line += 1
      if line == lines:
        keys.close()
        runTest(fileName)
        fileName = 'chave2_{}_{}.txt'.format(''.join(key), lines)
        keys = open(fileName, 'w')
        line = 0
    indexes[0] = 0
    keys.close()
    runTest(fileName)

start(linesPerFile)