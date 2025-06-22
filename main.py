from aliba_parser import Lark_StandAlone
from ParseTreeToProgram import ParseTreeToProgram

f = open("examples/looping-counter.aliba", 'r')
progtxt = f.read()
f.close

parser = Lark_StandAlone(transformer=ParseTreeToProgram())
program = parser.parse(progtxt)

print(program)
