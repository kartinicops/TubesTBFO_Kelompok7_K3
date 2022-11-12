import keyword

terminal = keyword.kwlist

ruleDict = {}

#Read txt
def readGrammarFile(file):
  with open(file) as cfg_file:
    baris = cfg_file.readlines()
    barisConverted = []
    for i in range(len(baris)):
      splitBaris = baris[i].replace("->", "").split()
      barisConverted.append(splitBaris)
  return barisConverted

#Convert to CNF
def convertToCNF(barisConverted):
  for i in range(len(barisConverted)):
    if len(barisConverted[i]) == 2:
      ruleDict[barisConverted[i][0]] = barisConverted[i][1]
    elif len(barisConverted[i]) == 3:
      ruleDict[barisConverted[i][0]] = barisConverted[i][1] + " " + barisConverted[i][2]
    elif len(barisConverted[i]) == 4:
      ruleDict[barisConverted[i][0]] = barisConverted[i][1] + " " + barisConverted[i][2]
      ruleDict[barisConverted[i][0] + "'"] = barisConverted[i][3] + " " + barisConverted[i][0] + "'"
    elif len(barisConverted[i]) == 5:
      ruleDict[barisConverted[i][0]] = barisConverted[i][1] + " " + barisConverted[i][2]
      ruleDict[barisConverted[i][0] + "'"] = barisConverted[i][3] + " " + barisConverted[i][0] + "'"
      ruleDict[barisConverted[i][0] + "''"] = barisConverted[i][4] + " " + barisConverted[i][0] + "''"
    else:
      print("Error")
  return ruleDict

#Write to txt
def writeGrammarFile(file, ruleDict):
  with open(file, "w") as cfg_file:
    for key, value in ruleDict.items():
      cfg_file.write(key + " -> " + value + " ")

writeGrammarFile("cnf.txt", convertToCNF(readGrammarFile("cfg.txt")))