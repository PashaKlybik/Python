__author__ = 'pasha'

class storage:
    stor = set()

    def add(self, arradd):
        for i in arradd:
            self.stor.add(i)
        print (self.stor)

    def remove(self, arrdel):
        for i in arrdel:
            try:
                self.stor.remove(i)
            except KeyError:
                print (i,"- Not found")
        print (self.stor)

    def find(self, arrfind):
        for i in arrfind:
            print(i,"  ",i in self.stor)
#        print (check for i in arrfind check=i in self.stor)

    def print1(self):
        print(self.stor)

def problem3(text):
    list = storage()
    for i in text:
        comnd = i[0:i.find('(')]
        value = i[i.find('(') + 1: i.find(')')].split(',')
        if comnd == "add":
            list.add(value)
        elif comnd == "remove":
            list.remove(value)
        elif comnd == "find":
            list.find(value)
        elif comnd == "list":
            list.print1()
        elif i=='exit':
            break

