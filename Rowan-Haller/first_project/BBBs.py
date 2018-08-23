class bowling_ball:

    def __init__(self, dab, dabber):
        self.raidus = dab
        self.weight = dabber
    def bowl (self, rull):
        return (rull - self.weight)

dab = 6
dabber = 18
poopdiscoop = 9000
ok = bowling_ball(dab, dabber)
print(ok.bowl(poopdiscoop))
