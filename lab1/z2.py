__author__ = 'pasha'

def qsort(mass):
    if (len(mass) < 1):
        return mass
    left = qsort([x for x in mass if x < mass[0]])
    right = qsort([x for x in mass if x > mass[0]])
    return (left+[mass[0]]+right)

def merge(mass):
    if (len(mass) <=1):
        return  mass
    left = merge(mass[0 : len(mass) / 2])
    right = merge(mass[len(mass) / 2:])
    mass = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]>right[j]:
            mass.append(left[i])
            i += 1
        else:
            mass.append(right[j])
            j += 1
    for z in range(i,len(left)):
        mass.append(left[z])
    for z in range(j,len(right)):
        mass.append(right[z])
    return mass

def digitsort(mass):
    ten = 10
    for i in range(len(str(max(mass)))):
        arrdigt = [[] for _ in range(ten)]
        for x in mass:
            arrdigt[(x/(ten**(i)))%ten].append(x)
        print(arrdigt)
        mass = []
        for j in range(ten):
            mass += arrdigt[j]
    return mass


def main():
    a = [1, 3, 5, 6, 7, 3]
    merge(a)


if __name__ == '__main__':
    main()