# program.py
#
# Classes representing the parts of an Aliba program.

# Anthony Kozar
# June 22, 2025

class Register(object):
    def __init__(self, initial_value, offset):
        self.initial_value = initial_value
        self.offset = offset
        self.current_value = initial_value

    def addOffset(self, offset):
        self.current_value += offset

    def __str__(self):
        return "(" + str(self.current_value) + "," + str(self.offset) + ")"

class Clique(object):
    def __init__(self, name, targets, registers):
        self.name = name
        self.targets = targets
        self.registers = registers

    # add up the offsets of all registers that trigger
    def addTriggeredOffsets(self):
        total = 0
        for reg in self.registers:
            if reg.current_value >= 0:
                total += reg.offset
        return total

    def __str__(self):
        regstr = " ".join(map(str, self.registers))
        targstr = " ".join(map(str, self.targets))
        return self.name + ": " + targstr + " {" + regstr + "}"

class Target(object):
    def __init__(self, targetname, isnegative):
        self.name = targetname
        self.clique = None  # set later to the actual Clique object
        self.negative = isnegative

    def __str__(self):
        if self.negative:
            return "-" + self.name
        else:
            return "+" + self.name

class Program(object):
    def __init__(self, cliques):
        self.cliques = cliques

    def __str__(self):
        return "\n".join((map(str, self.cliques)))
