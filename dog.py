class Dog:
    #constructor __init__
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print(self.name + " said woof!")
        
    def sit(self):
        print(self.name + " <> sit")
        
    def rollover(self):
        print(self.name + " <> roll over")
        
    def run(self):
        print(self.name + " <> run")

