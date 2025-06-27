# program.py
#
# Classes representing the parts of an Aliba program.

# Anthony Kozar
# June 22, 2025

class AlibaSyntaxError(Exception):
    pass

class Register(object):
    def __init__(self, initial_value, offset):
        self.initial_value = initial_value
        self.offset = offset
        self.current_value = initial_value

    def addOffset(self, offset):
        self.current_value += offset

    def __str__(self):
        return "(" + str(self.current_value) + "," + str(self.offset) + ")"

# Pass 'None' for nextv or end if the source code had no value for one of them.
# The Interval object will provide the proper interpretation.
class Interval(object):
    def __init__(self, start, nextv, end):
        self.start = start
        if nextv == None:
            if start < end:
                self.incr = 1
            elif start == end:
                self.incr = 0
                self.count = 1
            else:
                self.incr = -1
        else:
            self.incr = nextv - start
        self.end = end
        if end != None and incr != 0:
            self.count = (end - start + 1)/incr
            if count < 1:
                raise AlibaSyntaxError("Interval [%d, %d..%d] contains less than 1 values." % (start, nextv, end))
        elif end == None:
            

class RegisterArray(object):
    def __init__(self, ):
        pass

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
        self.cliquemap = {cl.name:cl for cl in self.cliques}
        self._setTargetCliques()
    
    def _setTargetCliques(self):
        for cl in self.cliques:
            for t in cl.targets:
                try:
                    t.clique = self.cliquemap[t.name]
                except KeyError:
                    raise AlibaSyntaxError("Target '%s' in clique '%s' does not exist." % (t.name, cl.name))
    
    def __str__(self):
        return "\n".join((map(str, self.cliques)))
