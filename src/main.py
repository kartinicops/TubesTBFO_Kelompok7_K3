import argparse
from tokenizer import *
from lib.grammar.cfgtocnf import mapGrammar
from lib.grammar.cfgtocnf import convertGrammar
from lib.grammar.cfgtocnf import readGrammar
from lib.grammar.cykparser import cykParser



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



parser = argparse.ArgumentParser()
parser.add_argument('file', type = argparse.FileType('r'), help = 'konversi file')
arg  = parser.parse_args()

f = arg.file

for line in f:
  print(line)
    

bannerCompiler()
token = createToken(arg.file.name)
grammarCNF = mapGrammar(convertGrammar(readGrammar(arg.file.name)))
cykParser(token, grammarCNF)