import sys

class Record:
    """Represent a record."""
    def __init__(self, category='expense', discription='None', amount=0):
        """class Record has three parameters: _category, _discription, _amount"""
        """the default value of each parameter is:"""
        """_category = 'expense', _discription = 'None', _amount = 0"""
        self._category = category
        self._discription = discription
        self._amount = amount
    @property
    def print_record(self):
        """print the record (in the chart)"""
        print(f'{self._category:14s}  {self._discription:14s}  {self._amount:6d}')
class Records:
    """Maintain a list of all the Recors's and the initial amount of money."""
    def __init__(self, C):
        """class Records has two parameters: _record, _money"""
        """the default value of each parameter is:"""
        """_record = [], _money = 0"""
        self._record = []
        self._money = 0
        try:
            fh = open('record.txt', 'r')
            try:
                buf = fh.readline()
                self._money = int(buf)
            except ValueError:  #the first line cannot be intepreted as initial amount of money(9)
                sys.stderr.write('Invalid format of the input file. Set your money to 0 dollars\n')
            else:
                buf = fh.readline()
                cat = buf.split(' ')
                cat = [i for i in cat if i!='\n']
                if cat!=None:
                    C.add_new_category(cat)
                buf1 = fh.readlines()
                buf2 = []
                for i in range(0, len(buf1)):
                    buf2 = buf1[i].split()
                    try:
                        self._record += [Record(buf2[0], buf2[1], int(buf2[2]))]
                    except (ValueError, IndexError): #any of the lines cannot be intepreted as a record(10)
                        print('invalid format of the input record on line', i+2, 'Clear your present record')
                        self._record = []
                        break
                self.view()
                fh.close()
        except FileNotFoundError:   #file does not exist(7)
            self._mon_input()
            while True:
                r = input('Reset your money? (Yes/No)\t')
                if r=='Yes':
                    self._mon_input()
                elif r=='No': break
    
    def _mon_input(self):
        """money input function"""
        """with recursively asking the user whether to reset the input money"""
        buf = input('How much money do you have?\t')
        try:
            self._money = int(buf)
            print('You have ', self._money, ' dollars')
        except ValueError: #the user's input cannot be converted to an integer(1)
            sys.stderr.write('Input money invalid. Set your current money to 0 dollars.\n')
            self._money = 0

    def add(self, record, C):
        """add the record"""
        """record = input record (with multiple datas)"""
        """C = category reference"""
        buf1 = record.split(', ')
        for i in range(0, len(buf1)):
            buf2 = buf1[i].split()
            if len(buf2)<3: #the string cannot be split into a list of two string(3)
                print('Invalid format of the ', i+1, 'th record. Failed to add the record.')
                continue
            elif not C.is_category_valid(buf2[0]):
                print('The specified category in the ', i+1, 'th record is not found. Failed to add the record.')
                new = input('You can check the category by command "Categories", or add a new category? (Yes/No)\t')
                if new=='Yes':
                    C.add_new_category(buf2[0])
                else:
                    continue
            try:
                self._record += [Record(buf2[0], buf2[1], int(buf2[2]))]
                self._money += int(buf2[2])
            except ValueError:  #the second string after splitting cannot be converted to an integer(4)
                print('The expense or income of the ', i+1, 'th record is supposed to be an integer.'\
                        +' Failed to add the record.')

    def find(self, found):
        """find record with the specified category and its subcategories"""
        """found = given reference categories"""
        if found==[]:
            sys.stderr.write('The specified category does not exist.\n')
        else:
            total = 0
            print('Here\'s your expense and income records under category "', find, '":')
            print('Record  Category        Description     Amount')
            print('------  --------------  --------------  ------')
            for i in range(0, len(self._record)):
                if self._record[i]._category in found:
                    print(str(i+1)+' \t', end='')
                    self._record[i].print_record
                    total += self._record[i]._amount
            print('------  --------------  --------------  ------')
            print(f'                                        {total:6d}')

    def view(self):
        """view the whole records"""
        print('Here\'s your expense and income record:')
        print('Record  Category        Description     Amount')
        print('------  --------------  --------------  ------')
        for i in range(0, len(self._record)):
            print(str(i+1)+' \t', end='')
            self._record[i].print_record
        print('------  --------------  --------------  ------')
        print('Now you have ', self._money, ' dollars!')

    def delete(self, num):
        """delete the specified record of number 'num'"""
        """num = the record to be deleted"""
        if num<=len(self._record) and num>0:
            self._money -= self._record[num-1]._amount
            self._record = [self._record[i] for i in range(0, len(self._record)) if i+1!=num]
        else:   #user's input out of the range of record(5)(6)
            sys.stderr.write('Invalid deletion of record.\n')

    def save(self, categories):
        """save the record and the money into 'record.txt'"""
        with open('record.txt', 'w') as fh:
            fh.write(str(self._money)+'\n')
            if categories._categories[5]!=None:
                for i in range(0, len(categories._categories[5])):
                    #print(categories._categories[5][i])
                    fh.write(categories._categories[5][i]+' ')
            fh.write('\n')
            w = ''
            for i in range(0, len(self._record)):
                w += self._record[i]._category+' '+self._record[i]._discription+' '+str(self._record[i]._amount)+'\n'
            fh.writelines(w)

class Categories:
    def __init__(self, categories=None):
        """set the categories by default categories when first run the program"""
        self._categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']],\
                            'income', ['salary', 'bonus'], 'others', []]

    def view(self):
        """view the category"""
        self._view_category(self._categories)

    @classmethod
    def _view_category(cls, C, level=0):
        """recursively called the function to print the category and its subcategories"""
        for i in C:
            if type(i)==list:
                cls._view_category(i, level+1)
            else:
                if i!=None:
                    print('  '*level+'-'+i)

    def is_category_valid(self, data):
        """check if the data is in the categories given"""
        """data = the category the function needs to find in the category list"""
        return True if self._valid(data, self._categories) else False
    
    @classmethod
    def _valid(cls, data, C):
        """recursively call the function to search whether the given data is in the categories"""
        """return true if the data is in the categories"""
        """return false, otherwise"""
        for i in C:
            if type(i)==list:
                if cls._valid(data, i): return True
            else:
                if data==i: return True
        return False

    def find_subcategories(self, find):
        """return the flatten list of category and its subcategories"""
        """find = the given category (and the subcategories) the user want to find"""
        def find_subcategories_gen(category, categories, found=False):
            if type(categories)==list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child==category and index+1<len(categories) and type(categories[index+1])==list:
                        yield from find_subcategories_gen(category, categories[index+1], found=True)
            else:
                if categories==category or found==True:
                    yield categories
        return find_subcategories_gen(find, self._categories)
    def add_new_category(self, category):
        """add categories under others"""
        if type(category)==list:
            self._categories[5] += category
        else:
            self._categories[5] += [category]

categories = Categories()
records = Records(categories)
while True:
    usr = input('\nWhat do you want to do (Add, View, Delete, Categories, Find, Exit)?  ')
    if usr=='Add':
        buf = input('Add some expense or income records with category, discription, and amount:\n')
        records.add(buf, categories)
    elif usr=='View':
        records.view()
    elif usr=='Delete':
        buf = input('Which record do you want to delete?\t')
        try:
            num = int(buf)
            records.delete(num)
        except ValueError:  #user's input cannot be converted into integer
            sys.stderr.write('Invalid deletion of record.\n')
    elif usr=='Categories':
        categories.view()
    elif usr=='Find':
        find = input('Which category do you want to find?\t')
        target_categories = [i for i in categories.find_subcategories(find)]
        records.find(target_categories)
    elif usr=='Exit':
        records.save(categories)
        break
    else:   #user's input is none of the commands above(2)
        sys.stderr.write('Invalid command. Re-Enter a command.\n')
