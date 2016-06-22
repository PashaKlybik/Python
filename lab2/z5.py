__author__ = 'pasha'

class Logger(object):
    log = ""
    def __getattribute__(self, item):
        temp = object.__getattribute__(self,item)

        def cmpfunc(*args):
            result = temp(*args)
            Logger.log += "Func: '{0}', arg: {1}, result {2}\n".format(item, args, result)
            return result

        if callable(temp):
            return cmpfunc
        return temp

    def __str__(self):
        #print(Logger.log)
        return Logger.log

class Test(Logger):
    def __init__(self, name = "Test object"):
        self.name = name

    def bar(self):
        print('bar')

    def mul(self, x, y):
        return x*y

    def sub(self, x, y):
        return x-y

def main():
    a = Test("zxc")
    a.bar()
    a.mul(2,4)
    a.sub(9,6)
    a.mul(6,4)
    print(a)

if __name__ == "__main__":
    main()