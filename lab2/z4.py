__author__ = 'pasha'

class Vector():
    def __init__(self,n=1):
        self.vec = [0 for _ in range(n)]

    def __len__(self):
        return len(self.vec)

    def __getitem__(self, item):
        if 0<=item<len(self.vec):
            return self.vec[item]
        return None

    def __setitem__(self, key, value):
        if 0<=key<len(self.vec):
            self.vec[key]=value

    def __str__(self):
        return str(self.vec)

    def __eq__(self, other):
        if type(self)==type(other) and (len(self.vec)==len(other.vec)):
            return True
        return False

    def __iadd__(self, other):
        if type(other)==type(self):
            if len(self)==len(other):

                for i in range(len(self)):
                    self.vec[i]+=other.vec[i]
                return self
            else:
                print ("different length vectors")
                return self
        elif type(other)==type(self.vec[0]):
            for i in range(len(self)):
                self.vec[i]+=other
            return self
        else:
            print("Type error")
            return self

    def __add__(self, other):
        if type(other)==type(self):
            if len(self)==len(other):
                temp = Vector(len(self))
                for i in range(len(self)):
                    temp.vec[i]=self.vec[i]+other.vec[i]
                return temp
            else:
                print ("different length vectors")
                return 0
        elif type(other)==type(self.vec[0]):
            temp = Vector(len(self))
            for i in range(len(self)):
                temp.vec[i]=self.vec[i]+other
            return temp
        else:
            print("Type error")
            return 0

    def __isub__(self, other):
        if type(other)==type(self):
            if len(self)==len(other):

                for i in range(len(self)):
                    self.vec[i]-=other.vec[i]
                return self
            else:
                print ("different length vectors")
                return self
        elif type(other)==type(self.vec[0]):
            for i in range(len(self)):
                self.vec[i]-=other
            return self
        else:
            print("Type error")
            return self

    def __sub__(self, other):
        if type(other)==type(self):
            if len(self)==len(other):
                temp = Vector(len(self))
                for i in range(len(self)):
                    temp.vec[i]=self.vec[i]-other.vec[i]
                return temp
            else:
                print ("different length vectors")
                return 0
        elif type(other)==type(self.vec[0]):
            temp = Vector(len(self))
            for i in range(len(self)):
                temp.vec[i]=self.vec[i]-other
            return temp
        else:
            print("Type error")
            return 0

    def __mul__(self, other):
        if type(self)==type(other):
            if len(self)==len(other):
                scalar = 0
                for vec1, vec2 in zip(self.vec, other.vec):
                    scalar += vec1+vec2
                return scalar
            else:
                print("different length vectors")
        elif type(other)==type(self.vec[0]):
            temp = Vector(len(self))

            for i in range(len(temp)):
                temp.vec[i] = self.vec[i]*other
            return temp
        else:
            print("Type error")
            return 0
