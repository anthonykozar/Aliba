from aliba_parser import Lark_StandAlone
from ParseTreeToProgram import ParseTreeToProgram

from sys import argv

if len(argv) < 1:
    f = open("examples/looping-counter.aliba", 'r')
else:
    f = open(argv[1], 'r')
progtxt = f.read()
f.close()

parser = Lark_StandAlone(transformer=ParseTreeToProgram())
program = parser.parse(progtxt)

print(program)
