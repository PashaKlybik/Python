__author__ = 'pasha'
class Defaultdict():
    def __init__(self):
        self.dic = dict()

    def __get__(self, instance, owner):
        return self.dic

    def __setitem__(self, key, value):
        self.dic[key]=value

    def __getitem__(self, item):
        return Defaultdict.getitem(self,item,0)

    def getitem(self, item,point):
        if not self.dic.get(item):
            self.dic[item]=Defaultdict()
        return self.dic[item]

    def __str__(self):
        a = '{'
        for key in self.dic:
            a+=str(key)+": "+str(self.dic[key])+", "
        return a[:-2]+"}"
