class Parrot:
    species = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age

blue = Parrot("blu",10)
halo = Parrot("Halo",11)

print("Blu is a {}".format(blue.species))
print("Halo is a {}".format(halo.species))