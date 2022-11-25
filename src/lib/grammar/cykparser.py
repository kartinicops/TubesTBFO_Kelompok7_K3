def cykParser(token,grammar) :
    length = len(token)
    arr = [[set([]) for j in range(length)] for i in range(length)]
    for i in range(length) :
        for left, rules in grammar.items() :
            for right in rules :
                if(len(right) == 1 and right[0] == token[i]) :
                    arr[i][i].add(left)

        for j in range(i, -1, -1) :
            for k in range(j,i) :
                for left, rule in grammar.items() :
                    for right in rule :
                        if len(right) == 2 and right[0] in arr[j][k] and right[1] in arr[k+1][i] :
                            t[j][i].add(left)

        if 'DIVEQUAL' in arr[0][length - 1] :
            print("Sukses ok")
        else :
            print("Gagal bro")

