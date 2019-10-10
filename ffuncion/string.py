class IgualdadNumericString:
    def __init__(self, meta):
        self.meta = meta

    def aplicar(self, cromosoma):
        return sum(str(cromosoma[i]) == self.meta[i] for i in range(len(self.meta)))

class IgualdadString:
    def __init__(self, meta):
        self.meta = meta

    def aplicar(self, cromosoma):
        return sum(chr(cromosoma[i]) == self.meta[i] for i in range(len(self.meta)))