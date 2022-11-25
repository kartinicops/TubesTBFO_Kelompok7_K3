import keyword
terminal = keyword.kwlist
ruleDict = {}

def readGrammar(file) :
  grammar = []
  with open(file) as f:
    for line in f:
      grammar.append(line.split())
  return grammar

def displayGrammar(grammar) :
  for rule in grammar :
    print(rule[0], " -> ", end = "")
    for i in range(1, len(rule)) :
      print(rule[i], end = "")
      print(" ", end = "")
    print()

def appendRule(rule):
  global ruleDict
  if rule[0] not in ruleDict:
    ruleDict[rule[0]] = []
  ruleDict[rule[0]].append(rule[1:])

def convertGrammar(grammar):
  global ruleDict
  for rule in grammar:
    if len(rule) == 2:
      appendRule(rule)
    else:
      newRule = []
      newRule.append(rule[0])
      for i in range(1, len(rule) - 1):
        newRule.append(rule[i])
        newRule.append(rule[i] + "'")
        appendRule(newRule)
        newRule = []
        newRule.append(rule[i] + "'")
      newRule.append(rule[len(rule) - 1])
      appendRule(newRule)
  return ruleDict 

def mapGrammar(grammar):
    global terminal
    newGrammar = {}
    for rule in grammar:
        if rule[0] not in newGrammar:
            newGrammar[rule[0]] = []
        if rule[1] in terminal:
            newGrammar[rule[0]].append(rule[1])
        else:
            for i in grammar[rule[1]]:
                newGrammar[rule[0]].append(i)
    return newGrammar

def writeGrammar(grammar, file):
    with open(file, 'w') as f:
        for rule in grammar:
            f.write(rule + " -> ")
            for i in range(len(grammar[rule])):
                f.write(grammar[rule][i])
                if i != len(grammar[rule]) - 1:
                    f.write(" | ")
            f.write("\n")

writeGrammar(mapGrammar(convertGrammar(readGrammar("cfg.txt"))), "cnf.txt")