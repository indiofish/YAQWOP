# Give a sequence of QWOPs to QWOPPER, and get the result and print
import sys

sys.path.append("../../dist/qwopper.jar")
import com.slowfrog.qwop.ui.Main as TEST

runs = ["+WQO+P+po+qw+PQ++OWpq+Q+P+pqo+POw++W+Q+qo+O++++p+oQwP+W+Oqpw+oQW+OP+po++++qw", "powq+WQO+P+po+qw+PQ++OWpq+Q+P+pqo+POw++W+Q+qo+O++++p+oQwP+W+Oqpw+oQW+OP+po++++qw"]  # list of sequences, given by genetics.py

TEST.main([])  # inits the class
for s in runs:
    info = TEST.playOneGame(s)
    print("results:" + str(info.distance))
    #  do evaluation with results
