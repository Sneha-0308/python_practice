class Weight:
    def __init__(self, kilos):
        self.kilos = kilos

    def __add__(self, otherWeight):
        return Weight(self.kilos + otherWeight.kilos)


w1 = Weight(50)
w2 = Weight(150)
tot = w1 + w2
print(tot.kilos)