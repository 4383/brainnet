class ParserException(Exception):
    pass


class Parser:
    position = 0
    line = 0
    column = 0

    def __init__(self, script):
        self.script = script

    def next(self):
        character = self.script[self.position + 1]
        if character == "\n":
            self.line += 1
            self.column = 0
        else:
            self.column += 1
        return character

    def peek(self):
        return self.script[self.position]

    def eof(self):
        return self.peek() == ""

    def croak(self, message):
        raise ParserException(message + "(" + self.line + ":" + self.col + ")")
