# Give a sequence of QWOPs to QWOPPER, and get the result and print
import sys

sys.path.append("../../dist/qwopper.jar")
import com.slowfrog.qwop.ui.Main as TEST



class Communicator(object):
    def __init__(self):
        TEST.main([])

    def run(self, sequences):
        ret = []
        for s in sequences:
            info = TEST.playOneGame(s)
            ret.append((info.distance, info.duration))

        return ret
