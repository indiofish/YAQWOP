#!/usr/bin/jython
import sys
sys.path.append("../../src/genetic")
import genetic


def main():
    ret = genetic.solve()
    print(ret)

if __name__ == '__main__':
    main()
