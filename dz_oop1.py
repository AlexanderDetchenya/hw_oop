# Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.

class strochis:
    def __init__(self):
        self.func()

    def dlina(self):
        glas = []
        soglas = []
        dlinsl = []
        cifr = []
        if self.b == 'str':
            sogl = 'цкнгшщзхъфвпрлджчсмтбь'
            gla = 'уеыаоэяию'
            for i in self.a:
                if i in sogl:
                    soglas += i
                elif i in gla:
                    glas += i
            for i in self.a:
                dlinsl += i
            if len(glas)*len(soglas) <= len(dlinsl):
                print(glas)
            if len(glas)*len(soglas) > len(dlinsl):
                print(soglas)

        if self.b == 'chislo':
            chet = 0
            dlinch = []
            rez = 0
            for i in self.a:
                i = int(i)
                if i % 2 == 0:
                    chet += i
            for i in self.a:
                 dlinch.append(i)
            rez = chet*len(dlinch)
            print(rez)





    def func(self):
        self.a = input('Введите строку или число: ')
        self.b = input('Введите тип введенных данных(str/chislo): ')


zadanie = strochis()
zadanie.dlina()



