__author__ = 'pasha'

class Itrel():
    def __init__(self,arg):
        self.arr=[int(_) for _ in arg]
        self.index = 0
        self.lense = len(self.arr)

    def __iter__(self):
        return self

    def next(self):
        if self.index==self.lense-1:
            self.index=0
            raise StopIteration
        self.index+=1
        return self.arr[self.index]+self.arr[self.index-1]

    def filter(self,f):
        return Itrel((x for x in self.arr if f(x)))
def f(x):
    return x>0

def main():
    a = Itrel((1,-3,67,-37,65,12,-82,93,5))
    for i in a:
        print(i)
    b = a.filter(f)
    for i in b:
        print(i)
    for i in a:
        print(i)

if __name__=="__main__":
    main()