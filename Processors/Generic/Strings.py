#------  string manipulations

help(str.encode)  # for the full list, try help(str)

string = 'the fox and the' + ' dog go jumping\n'
string * 2

print('there %s are %d foxes and %g dogs' % ('sometimes',3, 2.2))
print("there {0} are {1} foxes and {2} dogs".format('sometimes',3,2.2))

fred = string.split()
fred
fred[2]     # second word
string.upper()
string[2]      #second character
string[:7]     # up to the 7th element
string[7:]     # 7 and beyond

'fox' in string    # search
'fab' in string    # search

string.find('o')
string.lower().startswith('t')    # make all lowercase before checking
string.strip()  # remove spaces (lstrip or rstrip just do one side)
string[string.find('a'):string.find(' ',10)]    # from a to space after 10

string.count('a',2,25)    # number of as between char 2 and 25
string.endswith('g')
string.isdigit()        # or isalpha() for letters

string.partition(' ')
string.replace('fox','cat')
str(string.find(' ')) + ' and ' + str(string.rfind(' '))

string2 ='''one
two
three'''
string2
string2.splitlines()
string2.split('\n')
