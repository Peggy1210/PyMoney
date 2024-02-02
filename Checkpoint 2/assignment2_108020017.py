def add(R):
    buf1 = input('Add some expense or income records with discription and amount:\n')
    buf2 = buf1.split(', ')
    for i in range(0, len(buf2)):
        buf3 = buf2[i].split()
        if len(buf3)<2: #the string cannot be split into a list of two string(3)
            print('Invalid format of the ', i+1, 'th record.')
            continue
        try:
            R = R+[(buf3[0], int(buf3[1]))]
        except ValueError:  #the second string after splitting cannot be converted to an integer(4)
            print('Invalid format of the', i+1, 'th record.')
    return R

def view(M, R):
    print('Here\'s your expense and income record:')
    print('Record  Description     Amount')
    print('------  --------------  ------')
    for i in range(0, len(R)):
        s = '{:d} \t{:s}      \t{:d}'
        print(s.format(i+1, R[i][0], R[i][1]))
        M = M+R[i][1]
    print('------  --------------  ------')
    #print('Now you have ', M, 'dollars!')

def delete(R):
    buf = input('Which record do you want to delete?    ')
    num = int(buf)
    if num<=len(R) and num>0:   #user's input out of the range(5)(6)
        R = [R[i] for i in range(0, len(R)) if i+1!=num]
    else:
        print('Invalid deletion of record.')
    return R

def save(M, R):
    with open('record.txt', 'w') as fh:
        fh.write(str(M)+'\n')
        w = ''
        for i in range(0, len(R)):
            w = w+R[i][0]+' '+str(R[i][1])+'\n'
        fh.writelines(w)

def mon_input():
    M = input('How much money do you have?  ')
    try:
        M = int(M)
        print('You have ', M, ' dollars')
    except ValueError:  #the user's input cannot be converted to an integer(1)
        print('Input money invalid. Set your current money to 0 dollars.')
        M = 0
    return M

def initialize():
    R = []
    M = 0
    try:
        fh = open('record.txt', 'r')
        try:
            buf = fh.readline()
            M = int(buf)
        except ValueError:  #the first line can not be interpreted as initial amount of money(9)
            print('Invalid format of the input file. Set your money to 0 dollars.')
            M = 0
        buf1 = fh.readlines()
        buf2 = []
        for i in range(0, len(buf1)):
            buf2 = buf1[i].split()
            try:
                R = R+[(buf2[0], int(buf2[1]))]
            except (ValueError, IndexError):  #any of the lines cannot be interpreted as a record(10)
                print('Invalid format of the input record on line', i+2, '. Clear your present record.')
                R = []
        view(M, R)
        fh.close()
    except FileNotFoundError:   #file does not exist(7)
        M = mon_input()
        while True:
            r = input('Reset your money? Yes/No  ')
            if r=='Yes': 
                M = mon_input()
            elif r=='No': break
    return M, R

mon, record = initialize()
while True:
    usr = input('\nWhat do you want to do (Add, View, Delete, Exit)?  ')
    if usr=='Add':
        record = add(record)
    elif usr=='View':
        view(mon, record)
    elif usr=='Delete':
        record = delete(record)
    elif usr=='Exit':
        save(mon, record)
        break
    else:   #user's input is none of the commands above(2)
        print('Invalid command. Re-Enter a command.')
