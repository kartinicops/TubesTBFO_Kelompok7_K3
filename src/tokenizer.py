import sys 
import re
import os


dictionary = [ 
    (r'[ ]+', None),
    (r'[\t]+', None),
    (r'//[^\n]*', None),
    (r'\n', 'NEWLINE'),

    (r'\bbreak\b',"BREAK"),
    (r'\bcontinue\b',"CONTINUE"),
    (r'\bif\b',"IF"),
    (r'\bclass\b',"CLASS"),
    (r'\bconst\b',"CONST"),
    (r'\bcase\b',"CASE"),
    (r'\bcatch\b',"CATCH"),
    (r'\bdefault\b',"DEFAULT"),
    (r'\bdelete\b',"DELETE"),
    (r'\belse\b',"ELSE"),
    (r'\bfalse\b',"FALSE"),
    (r'\bfor\b',"FOR"),
    (r'\blet\b',"LET"),
    (r'\breturn\b',"RETURN"),
    (r'\bnull\b',"NULL"),
    (r'\bswitch\b',"SWITCH"),
    (r'\bvar\b',"VAR"),
    (r'\btrue\b',"TRUE"),
    (r'\bwhile\b',"WHILE"),
    (r'\bfunction\b',"FUNCTION"),
    (r'\btry\b',"TRY"),
    (r'\bthrow\b',"THROW"),
    (r'\bundefined\b',"UNDEFINED"),
    (r'\bimport\b', "IMPORT"),
    (r'\bfrom\b', "FROM"),
    (r'\bas\b', "AS"),
    

    (r'\+\+','PLUSPLUS'),
    (r'\-\-','MINUSMINUS'),
    (r'\+','PLUS'),
    (r'\-','MINUS'),
    (r'\*','TIMES'),
    (r'\/','DIVIDE'),
    (r'\%','MOD'),
    (r'\(','LBRACKET'),
    (r'\)','RBRACKET'),
    (r'\{','LCURLY'),
    (r'\}','RCURLY'),
    (r'\[','LSQUARE'),
    (r'\]','RSQUARE'),
    (r'\;','SEMICOLON'),
    (r'\,','COMMA'),
    (r'[.]+\w',"DOTBETWEEN"),
    (r'\.','DOT'),
    (r'\:','COLON'),
    (r'\!\=(?!\=)','NOTEQ'),
    (r'\!','NOT'),
    (r'\&','AND'),
    (r'\|','OR'),
    (r'\>','GREATER'),
    (r'\<','LESS'),
    (r'\=>', 'ARROW'),
    (r'\>=','GREATEREQUAL'),
    (r'\<=','LESSEQUAL'),
    (r'\=(?!\=)','EQUAL'),
    (r'\=\=(?!\=)','ISEQ'),
    (r'\=\=\=(?!\=)','ISSTRICTEQ'),
    # (r'\!\=','NOTEQUAL'),
    (r'\&\&','ANDAND'),
    (r'\|\|','OROR'),
    (r'\'[^\'\n]*\'',"STRING"),
    (r'\"[^\"\n]*\"',"STRING"),
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',           "INT"),
    (r'\'.*\'','CHAR'),
    (r'\//.*','COMMENT'),
    # (r'\_','UNDERSCORE'),
    (r'\+=','PLUSEQUAL'),
    (r'\-=','MINUSEQUAL'),
    (r'\*=','TIMESEQUAL'),
    (r'\/=','DIVEQUAL'),
    
    
    (r'[a-zA-Z_][a-zA-Z0-9_]*', "VAR"),
]

def read(text, dict):
    line = 1            
    cp = 1
    position = 0             
    lengthteks = len(text)         
    arrans = []
    while (position < lengthteks):
        if text[position] == '\n':
            line += 1
            cp = 1
        cek = None
        for tokenExpr in dict:
            pattern, tag = tokenExpr    
            regex = re.compile(pattern)
            cek = regex.match(text, position)
            if cek:
                if tag:
                    token = tag
                    arrans.append(token)
                break

        if not cek:
            print(f"\nERROR!!!\nkarakter ilegal '{text[position]}'. baris {line} kolom {cp}")
            sys.exit(1)
        else:
            position = cek.end(0)
        cp += 1
    return arrans

def makeToken(text):
    f = open(text, encoding="utf8")
    word = f.read()
    f.close()
    varr = read(word, dictionary)
    res = []
    for i in varr:
        res.append(i)
    
    a = os.getcwd()
    resultFile = open(a + "/result/Result.txt", 'w')
    for token in res:
        resultFile.write(str(token)+" ")
    resultFile.close()
    return res