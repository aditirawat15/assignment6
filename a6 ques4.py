def Pangram(string1):

    start = ord('a')
    end = ord('z')
    #print(start)
    string1 = string1.lower()
    letters = list(map(str,''.join(string1.split())))
    #print(letters)
    for i in range(start, end + 1):
        if  chr(i) in letters: continue
        else: return False
    return True



if(Pangram(input())) : print('Pangram.')
else:print('not a Pangram.')
filter
