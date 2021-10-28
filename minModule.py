class MinAlgorithm:

    def __init__(self, cs):
        self.chars = cs
        self.minChar = ''

    def getMinChar(self):
        self.minChar = self.chars[0]

        for c in self.chars:
            if ord(self.minChar) > ord(c):
                self.minChar = c

        return self.minChar