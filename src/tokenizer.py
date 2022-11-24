import sys 
import re
import os


tokendict = [ 
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
    (r'\=(?!\=)','EQUAL'),
    (r'\=\=(?!\=)','ISSTRICTEQ'),
    (r'\=\=\=(?!\=)','IS'),
    (r'\!\=(?!\=)','NOTEQ'),
    # (r'\!\=','NOTEQUAL'),
    (r'\+\+','PLUSPLUS'),
    (r'\-\-','MINUSMINUS'),
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


# multLine1 = r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
# multLine2 = r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'

def lex(text, tokendict):
    line = 1            
    pos = 0             
    currPos = 1         
    tokens = []
    while (pos < len(text)):
        # print("test")
        # print("pos = ", pos)
        # print(len(text))
        if text[pos] == '\n':
            line += 1
            currPos = 1

        flag = None
        # break
        for tokenExpr in tokendict:
            pattern, tag = tokenExpr    
            # if line == 1:
            #     if pattern == multLine1:
            #         pattern = r'[^\w]*[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
            #     elif pattern == multLine2:
            #         pattern = r'[^\w]*[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'

            regex = re.compile(pattern)
            flag = regex.match(text, pos)

            if flag:
                # texts = flag.group(0)
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not flag:
            print(f"\nSYNTAX ERROR\nIllegal character {text[pos]} at line {line} and column {currPos}")
            sys.exit(1)
        else:
            # print("masuk sini gak")
            pos = flag.end(0)
        currPos += 1

    return tokens

def createToken(text):
    # Read file
    file = open(text, encoding="utf8")
    characters = file.read()
    file.close()

    tokens = lex(characters, tokendict)
    tokenResult = []

    for token in tokens:
        tokenResult.append(token)


    # Write file
    path = os.getcwd()
    fileWrite = open(path + "/result/tokenResult.txt", 'w')
    for token in tokenResult:
        fileWrite.write(str(token)+" ")
        # print(token)
    fileWrite.close()

    return tokenResult