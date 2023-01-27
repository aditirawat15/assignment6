#hyphen-separated sequence after sorting them alphabetically
def order(string1):
    if '-' not in string1 or ' ' in string1:
        print('Enter a valid value:')
        return 
    string1 = string1.split('-')
    string1.sort()
    print('-'.join(map(str,string1)))

order(input('Enter string: '))
