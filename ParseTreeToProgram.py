# ParseTreeToProgram.py
#
# Subclass of Lark Visitor to convert the parse tree into an Aliba program object.

# Anthony Kozar
# June 22, 2025

from aliba_parser import Transformer_NonRecursive
from program import *

class ParseTreeToProgram(Transformer_NonRecursive):
    def register(self, children):
        #print(children)
        # assert tree.data == "register"
        assert children[0].data == "initial_value"
        assert children[1].data == "offset"
        ival = int(children[0].children[0].value)
        offset = int(children[1].children[0].value)
        return Register(ival, offset)

    def clique(self, children):
        #print(children)
        # assert tree.data == "clique"
        assert children[0].type == "IDENTIFIER"
        name = children[0].value
        targets = []
        registers = []
        for ch in children[1:]:
            if type(ch) == Register:
                registers.append(ch)
            # ch should be a Lark Tree node
            elif ch.data == "pos_target":
                assert ch.children[0].type == "IDENTIFIER"
                targets.append(Target(ch.children[0].value, False))
            elif ch.data == "neg_target":
                assert ch.children[0].type == "IDENTIFIER"
                targets.append(Target(ch.children[0].value, True))
        return Clique(name, targets, registers)

    def start(self, children):
        return Program(children)
