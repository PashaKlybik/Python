#!/usr/bin/env python

__author__ = 'pasha'
import argparse
import z2, z1, z3, z4

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', "--program", default='string')
    parser.add_argument('-t', "--type", nargs='?', default='repeats')
    parser.add_argument('-s', "--source", default='nums', nargs='?')
    namespase = parser.parse_args()
    if namespase.program == 'text':
        with open(namespase.source, 'r') as f:
            t = f.read()
            z1.average_word(t)
            z1.count_word(t)
            z1.median_word(t)
            n ,k=int(input('input n ')), int(input('\ninput k '))
            print('\n')
            z1.topngram(t,k,n)
    elif namespase.program == 'sort':
        with open(namespase.source, 'r') as f:
            if namespase.type == 'qsort':
                print(z2.qsort([int(i) for i in f.read().split()]))
            elif  namespase.type == 'merge':
                print(z2.merge([int(i) for i in f.read().split()]))
            elif  namespase.type == 'digit':
                print(z2.digitsort([int(i) for i in f.read().split()]))
            else:
                print ('err')
    elif namespase.program == 'storage':
        with open(namespase.source, 'r') as f:
            print('ass')
            z3.problem3(f.read().split())
    elif namespase.program == 'fib':
        with open(namespase.source, 'r') as  f:
            z4.fib(int(f.read()))

if __name__ == '__main__':
    main()