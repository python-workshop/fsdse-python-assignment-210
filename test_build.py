import sys
from build import find_max_profit
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

a = [8, 5, 3, 2, 1]
test(find_max_profit(a) == -1)
a = [5, 3, 7, 4, 2, 6, 9]
test(find_max_profit(a) == 7)
