__author__ = 'pasha'

class MetaClass(type):
    def __new__(cls, name, bases, attrs):
        print("create new class")
        i=input("input file: ")
        with open(i,'r') as file:
            for string in file:
                attrs[string.split(':')[0]] = string.split(':')[1]
        return super(MetaClass,cls).__new__(cls, name, bases, attrs)

class Test(object):
    __metaclass__ = MetaClass

print(Test.c)
print(Test.b)
print(Test.a)