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
]