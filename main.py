from aliba_parser import Lark_StandAlone
from ParseTreeToProgram import ParseTreeToProgram
from program import AlibaSyntaxError

import sys

if len(sys.argv) < 1:
    f = open("examples/looping-counter.aliba", 'r')
else:
    f = open(sys.argv[1], 'r')
progtxt = f.read()
f.close()

parser = Lark_StandAlone(transformer=ParseTreeToProgram())
try:
    program = parser.parse(progtxt)
except AlibaSyntaxError as err:
    print("Syntax error:", err)
    sys.exit(1)

print(program)
