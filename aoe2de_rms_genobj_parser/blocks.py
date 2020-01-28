# BlockLine represent all other lines than Command ones
class BlockLine:
    """Represents a line but the `{` and `}` have additional formatting for the file writing"""

    def __init__(self, line):
        self.line = line

    def display(self, cond_list):
        if self.line.startswith("{"):
            formatted = self.line + "\n"
        elif self.line.startswith("}"):
            formatted = self.line + "\n\n"
        else:
            formatted = self.line + "\n"
        return formatted

    def __str__(self):
        return self.line


# _BlockCMD is an Abstract Class that represent the highest form of Command Blocks from GeneratingObjects
class _BlockCMD:
    def __init__(self, precedence):
        self.contentList = []
        self.precedence = precedence

    def display(self, cond_list):
        out = ""
        for elt in self.contentList:
            out += elt.display(cond_list)
        return out


# _BlockCond is also an Abstract Class that represent the Command Blocks with a condition (If, Elseif)
class _BlockCond(_BlockCMD):
    def __init__(self, condition, precedence):
        _BlockCMD.__init__(self, precedence)
        self.condition = condition
        self.counterPart = None

    def display(self, cond_list):
        out = ""
        if self.condition in cond_list:
            for elt in self.contentList:
                out += elt.display(cond_list)
        elif self.counterPart is not None:
            out = self.counterPart.display(cond_list)
        return out


class BlockIf(_BlockCond):
    """Command Block with IF statement, save the condition to be tested afterwards"""
    pass


class BlockElseIf(_BlockCond):
    """Command Block with ELSEIF statement, save the condition to be tested afterwards"""
    pass


class BlockElse(_BlockCMD):
    """Command Block with ELSE statement, no condition associated as its a final statement"""
    pass
