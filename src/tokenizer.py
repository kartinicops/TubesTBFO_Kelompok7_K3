import sys 
import re


tokendict = [ 
    (r'\n', 'NEWLINE'),
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
    (r'\.','DOT'),
    (r'\:','COLON'),
    (r'\!','NOT'),
    (r'\&','AND'),
    (r'\|','OR'),
    (r'\>','GREATER'),
    (r'\<','LESS'),
    (r'\>=','GREATEREQUAL'),
    (r'\<=','LESSEQUAL'),
    (r'\=\=','EQUAL'),
    (r'\!\=','NOTEQUAL'),
    (r'\+\+','PLUSPLUS'),
    (r'\-\-','MINUSMINUS'),
    (r'\&\&','ANDAND'),
    (r'\|\|','OROR'),
    (r'\'[^\'\n]*\'',"STRING"),
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',           "INT"),
    (r'\'.*\'','CHAR'),
    (r'\//.*','COMMENT'),
    (r'\_','UNDERSCORE'),
    (r'\+=','PLUSEQUAL'),
    (r'\-=','MINUSEQUAL'),
    (r'\*=','TIMESEQUAL'),
    (r'\/=','DIVEQUAL'),

    (r'\bbreak\b',"BREAK"),
    (r'\bContinue\b',"CONTINUE"),
    (r'\bif\b',"IF"),
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
    
]


multLine1 = r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
multLine2 = r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'

def lex(text, tokendict):
    line = 1            
    pos = 0             
    currPos = 1         
    tokens = []

    while (pos < len(text)):
        if text[pos] == '\n':
            line += 1
            currPos = 1

        flag = None
        for tokenExpr in tokendict:
            pattern, tag = tokenExpr    

            if line == 1:
                if pattern == multLine1:
                    pattern = r'[^\w]*[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
                elif pattern == multLine2:
                    pattern = r'[^\w]*[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'

            regex = re.compile(pattern)
            flag = regex.match(text, pos)

            if flag:
                texts = flag.group(0)
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not flag:
            print(f"\nSYNTAX ERROR\nIllegal character {text[pos]} at line {line} and column {currPos}")
            sys.exit(1)
        else:
            pos = flag.end(0)
        currPos += 1

    return tokens