from random import getrandbits
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
                apple.check_cycles()

    def harvesting(self):
        for plant in self.plant_list:
            if plant.check_apple():
                plant.harvest()

    def garden_statistics(self):
        tree_count = 0
        apple_count = 0
        apple_stages = {}

        for plant in self.plant_list:
            tree_count += 1
            for apple in plant.apple_list:
                apple_count += 1
                stage = apple.current_stage
                if stage in apple_stages:
                    apple_stages[stage] += 1
                else:
                    apple_stages[stage] = 1

        return {
            "Количество деревьев": tree_count,
            "Возраст деревьев": self.get_tree_ages(),
            "Количество яблок": apple_count,
            "Стадии яблок": apple_stages
        }

    def get_tree_ages(self):
        tree_ages = []
        for plant in self.plant_list:
            tree_ages.append(plant.age)
        return tree_ages


class Wood:
    def __init__(self, *args):
        self.apple_list = []
        self.age = 1
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

    def increase_age(self):
        self.age += 1
        if self.age >= 10:
            self.apple_list =[]

    def generate_new_apple(self):
        if self.age <= 2:
            return
        elif self.age >= 5 or self.age >= 10:
            return
        else:
            new_apple = Apple(len(self.apple_list))
            self.apple_list.append(new_apple)


class Apple:
    ripening_stage = ['цветение', 'зеленое', 'красное']

    def __init__(self, index, current_stage=ripening_stage[0], cycles=0):
        self.index = index
        self.current_stage = current_stage
        self.cycles = cycles

    def ripening(self):
        stage = self.ripening_stage.index(self.current_stage)
        if not self.check_ripening():
            self.current_stage = self.ripening_stage[stage + 1]

    def check_ripening(self):
        if self.ripening_stage.index(self.current_stage) < 2:
            return False
        else:
            return True

    def check_cycles(self):
        if self.cycles >= 3:
            print('Яблоко умерло...')
        else:
            self.cycles += 1


ap0 = Apple(0)
ap1 = Apple(1)
ap2 = Apple(2)
ap3 = Apple(3)
ap4 = Apple(4)
Yablonya = Wood(ap0, ap1, ap2, ap3, ap4)
gardener = Gardener("1", Yablonya)

while not Yablonya.check_apple():
    gardener.grooming()
    Yablonya.increase_age()
    if bool(getrandbits(1)):
        Yablonya.generate_new_apple()
    print(gardener.garden_statistics())
gardener.harvesting()

garden_stats = gardener.garden_statistics()
print(garden_stats)