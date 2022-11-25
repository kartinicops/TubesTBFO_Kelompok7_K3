from tokenizer import *
from lib.grammar.cfgtocnf import *
from lib.cykparser import cykParser



def bannerCompiler() :
  print()
  print("")
  print("")
  print("     _                  ____            _       _   ")
  print("    | | __ ___   ____ _/ ___|  ___ _ __(_)_ __ | |_ ")         
  print(" _  | |/ _` \ \ / / _` \___ \ / __| '__| | '_ \| __|")        
  print("| |_| | (_| |\ V / (_| |___) | (__| |  | | |_) | |_ ")         
  print(" \___/ \__,_| \_/ \__,_|____/ \___|_|  |_| .__/ \__|")         
  print(" / ___|___  _ __ ___  _ __ (_) | ___ _ __|_|        ")                 
  print("| |   / _ \| '_ ` _ \| '_ \| | |/ _ \ '__|          ")                                                                  
  print("| |__| (_) | | | | | | |_) | | |  __/ |             ") 
  print(" \____\___/|_| |_| |_| .__/|_|_|\___|_|             ") 
  print("                     |_|                            ")  
  print()
  print("")




# for line in f:
#   print(line)

writeGrammar(convertGrammar(readGrammarFile("lib/grammar/cfg.txt")))
bannerCompiler()
d = input("Masukkan nama file : ")
print()
print("----------------------------------")
print()
print("compiling...")
print()
print("----------------------------------")
print()

token = createToken("js/" + d)
token = [i.lower() for i in token]

grammarCNF = mapGrammar(convertGrammar((readGrammarFile("lib/grammar/cfg.txt"))))
# print(grammarCNF)
cykParser(token, grammarCNF)
print()
print("----------------------------------")