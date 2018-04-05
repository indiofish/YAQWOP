#!usr/bin/python3

import sys
sys.path.append("../../src/communication")
from communication import Communicator
runs = ["+WQO+P+po+qw+PQ++OWpq+Q+P+pqo+POw++W+Q+qo+O++++p+oQwP+W+Oqpw+oQW+OP+po++++qw", "powq+WQO+P+po+qw+PQ++OWpq+Q+P+pqo+POw++W+Q+qo+O++++p+oQwP+W+Oqpw+oQW+OP+po++++qw"]  # list of sequences, given by genetics.py

def main():
    comm = Communicator()
    comm.run(runs)

if __name__ == '__main__':
    main()
