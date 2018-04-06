#!usr/bin/python3
import sys
sys.path.append("../../src/communication")
from communication import Communicator

runs = ["ABDEAFCFEGHIABNOPABCONM", "ABDEAFCFEGHIABNOPABCONM"]
# list of sequences, actually given by genetics.py


def main():
    comm = Communicator()
    comm.run(runs)

if __name__ == '__main__':
    main()
