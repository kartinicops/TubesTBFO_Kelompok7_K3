import keyword

terminal = keyword.kwlist

allRule = {}

def readGrammar(file):
  with open(file) as cfg_file:
    baris = cfg_file.readlines()
    barisConverted = []
    for i in range(len(baris)):
      splitBaris = baris[i].replace("->", "").split()
      barisConverted.append(splitBaris)
  return barisConverted

def makeGrammar(rule):
  global allRule
  
  if rule[0] not in allRule:
    allRule[rule[0]] = []
  allRule[rule[0]].append(rule[1:])

def grammarChange(grammar):
    global allRule
    idx = 0
    unitProductions, res = [], []
    for rule in grammar:
      new_rules = []
      if len(rule) == 2 and not rule[1][0].islower() :
        unitProductions.append(rule)
        makeGrammar(rule)
        continue
      while len(rule) > 3:
        
        new_rules.append([f"{rule[0]}{idx}", rule[1], rule[2]])
        rule = [rule[0]] + [f"{rule[0]}{idx}"] + rule[3:]
        idx += 1
      if rule:
        makeGrammar(rule)
        res.append(rule)
      if new_rules:
        for i in range(len(new_rules)):
          res.append(new_rules[i])

    while unitProductions:
      # print(unitProductions)
      rule = unitProductions.pop() 
      if rule[1] in allRule:
        for item in allRule[rule[1]]:
          new_rule = [rule[0]] + item
          if len(new_rule) > 2 or new_rule[1][0].islower():
            res.append(new_rule)
          else:
            unitProductions.append(new_rule)
          makeGrammar(new_rule)
    return res

def takeCNF(grammar):
  arr = {}
  for rule in grammar :
    arr[str(rule[0])] = []
  for rule in grammar :
    elm = []
    for idxRule in range(1, len(rule)) :
      apd = rule[idxRule]
      elm.append(apd)
    arr[str(rule[0])].append(elm)
  return arr

def makeCNF(grammar):
    cnffile = open('lib\grammar\cnf.txt', 'w')
    for rule in grammar:
        cnffile.write(rule[0])
        cnffile.write(" -> ")
        for i in rule[1:]:
            cnffile.write(i)
            cnffile.write(" ")
        cnffile.write("\n")
    cnffile.close()