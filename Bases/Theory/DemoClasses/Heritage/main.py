from Bases.Theory.DemoClasses.Heritage.Animal import Animal
from Bases.Theory.DemoClasses.Heritage.Bird import Bird
from Bases.Theory.DemoClasses.Heritage.Cat import Cat

if __name__ == '__main__':
    a1 = Animal()
    b1 = Bird('Titi')
    c1 = Cat('Gros minet')

    # print(type(a1) == Animal)
    # print(type(c1) == Animal)
    #
    # print(isinstance(a1, Animal))
    # print(isinstance(c1, Animal))
    # print(isinstance(c1, object))

    print(b1.can_fly)
    # print(a1.can_fly) # Invalid!

