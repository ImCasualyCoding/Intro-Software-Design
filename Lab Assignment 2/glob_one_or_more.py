
class OneOrMore:
    def __init__(self, rest=None):
        self.rest = rest

    def match(self, text, start=0):
        if start >= len(text):
            return False
            
        if self.rest is None:
            return True

        for i in range(start + 1, len(text) + 1):
            if self.rest.match(text, i):
                return True
                
        return False