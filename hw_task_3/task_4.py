
class Gardener:
    def __init__(self, name, *args):
        self.name = name
        self.plant_list = []
        for plant in args:
            self.plant_list.append(plant)
    def grooming(self):
        for plant in self.plant_list:
            for apple in plant.apple_list:
                apple.ripening()
    def harvesting(self):
        for plant in self.plant_list:
            if plant.check_apple:
                plant.harvest()
class Wood:
    def __init__(self, *args):
        self.apple_list = []
        for apple in args:
            self.apple_list.append(apple)
    def growing(self):

        for apple in self.apple_list:
            apple.ripening()
    def check_apple(self):
        for apple in self.apple_list:
            if not apple.check_ripening():
                return False
        return True
    def harvest(self):
        self.apple_list = []

class Apple:
    ripening_stage = ['цветение', 'зеленое', 'красное']
    def __init__(self, index, current_stage = ripening_stage[0]):
        self.index = index
        self.current_stage = current_stage

    def ripening(self):
        stage = self.ripening_stage.index(self.current_stage)
        if not self.check_ripening():
            self.current_stage = self.ripening_stage[stage + 1]
        else:
            print('Пока, Ньютон...(')

    def check_ripening(self):
        if self.ripening_stage.index(self.current_stage) < 2:
            return False
        else:
            return True

ap0 = Apple(0)
ap1 = Apple(1)
ap2 = Apple(2)
ap3 = Apple(3)
ap4 = Apple(4)

Yablonya = Wood(ap0, ap1, ap2, ap3, ap4)

gardener = Gardener("Test", Yablonya)
while not Yablonya.check_apple():
    gardener.grooming()

gardener.harvesting()
print('Урожай собран')
