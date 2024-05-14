class Animal:
    def fazer_barulho(self):
        pass

class Cachorro(Animal):
    def fazer_barulho(self):
        return "Au au!"

class Gato(Animal):
    def fazer_barulho(self):
        return "Miau!"

def fazer_som(animal):
    return animal.fazer_barulho()

cachorro = Cachorro()
gato = Gato()

print(fazer_som(cachorro))
print(fazer_som(gato))