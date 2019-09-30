import dog

myDog = dog.Dog("rex", "superdog")

myDog.bark()
mySecondDog = dog.Dog("sebastian", "rollingdog")
myThirdDog = dog.Dog("jennifer", "sittingdog")
myFourthDog = dog.Dog("ophelia", "runningdog")

mySecondDog.rollover() #sebastian will roll over
myThirdDog.sit() #jennifer will sit
myFourthDog.run() #ophelia will run

print(" ")

dog.greeting = "woah!"
myDog.bark()
mySecondDog.bark()
myThirdDog.bark()
myFourthDog.bark()

