# Give a sequence of QWOPs to QWOPPER, and get the result and print
import sys
sys.path.append("../../dist/qwopper.jar")
import com.slowfrog.qwop.ui.Main as qwopper


class Communicator(object):
    def __init__(self):
        qwopper.main([])

    def run(self, sequence):
        info = qwopper.playOneGame(sequence)

        return (info.distance, info.duration)
