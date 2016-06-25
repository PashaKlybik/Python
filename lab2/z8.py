__author__ = 'pasha'


def cached(func):
    save =dict()
    def decorate_func(a,b):
        if save.get((a,b))==None:
            save[(a,b)] = func(a,b)
        return save[(a,b)]
    return decorate_func

@cached
def rang(start,end):
    print("New range")
    return [x for x in range(start,end)]

def main():
    print(rang(1,3))
    print(rang(2,6))
    print(rang(7,12))
    print(rang(1,3))
    print(rang(2,6))
    print(rang(7,12))
    print(rang(7,23))

if __name__ == '__main__':
    main()