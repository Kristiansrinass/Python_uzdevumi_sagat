# python klases veidošanās specifika
class RUDENS:
    def __init__(self, vards, vecums):
        self.vards=vards
        self.vecums=vecums

#definē metodes(funkcijas) tas atrodās iekša klasē
    def araa(self):
        print(self.vards, self.vecums)

# tiek izveidots objekts
p=RUDENS("Gint", 25)

p.araa()
