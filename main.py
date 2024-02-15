from Car import *

# EV Car class example

prius = EVCar("Prius")
prius.set_color("Red")

print(prius.get_color())
prius.start()
prius.make_noise()

# Gas Car class example

lexus = GasCar("Lexus")
lexus.set_color("White")

print(lexus.get_color())
lexus.start()
lexus.make_noise()