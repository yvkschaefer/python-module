def world():
  print("Hello, World!")

world()

shark = "Sammy"


class Octopus:
  def __init__(self, name, colour):
    self.colour = colour
    self.name = name

  def tell_me_about_the_octopus(self):
    print("This octopus is " + self.colour + ".")
    print(self.name + " is the octopus' name.")