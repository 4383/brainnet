import re


class TokenStream:
    current = None
    keywords = [
        'if', 'else', 'or', 'and', 'elif', 'func',
    ]
    operators = ['+', '-', '*', '/', '%', '=', '<', '>', '!']
    punctuations = [',', ';', '(', ')', '[', ']', '{', '}']
    whitespaces = [' ', '\t', '\n']

    def __init__(self, parser):
        self.parser = parser

    def is_keyword(self, word):
        return word in self.keywords

    def is_digit(self, character):
        re.match("[0-9]", character)

    def is_operator(self, character):
        return character in self.operators

    def is_punctuation(self, character):
        return character in self.punctuations

    def is_whitespace(self, character):
        return character in self.whitespaces

    def read_while(self, predicate):
        string = ""
        while not self.parser.eof() and predicate(self.parser.peek()):
            string += self.parser.next()
        return string

    def read_number(self):
        has_dot = False

        def predicate(character):
            if character == '.':
                if has_dot:
                    return False
                has_dot = True
                return True
            return self.is_digit(character)

        number = self.read_while(predicate(character))
        return {'type': 'num', 'value': float(number)}

