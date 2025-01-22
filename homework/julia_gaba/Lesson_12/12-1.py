class Flower():
    def __init__(self, title, color, length, price, day_life):
        self.title = title
        self.color = color
        self.length = length
        self.price = price
        self.day_life = day_life

    def __str__(self):
        return f"Наименование:{self.title}({self.color}, {self.length}cm, {self.price}₽, {self.day_life} дней)"


class Rose(Flower):
    smell = True
    petals_stick = False

    def __init__(self, title, color, length, price, day_life):
        super().__init__(title, color, length, price, day_life)


rose1 = Rose('Роза', 'белая', 50, 210, 19)
rose2 = Rose('Роза', 'красная', 49, 200, 19)
rose3 = Rose('Роза', 'розовая', 51, 190, 19)


class Tulip(Flower):
    spring = True
    petals_stick = False

    def __init__(self, title, color, length, price, day_life):
        super().__init__(title, color, length, price, day_life)


tulip1 = Tulip('Тюльпан', 'желтый', 41, 150, 24)
tulip2 = Tulip('Тюльпан', 'оранжевый', 40, 150, 24)
tulip3 = Tulip('Тюльпан', 'розово-оранжевый', 39, 150, 24)


class Daisy(Flower):
    petals_stick = True
    bud_core = True

    def __init__(self, title, color, length, price, day_life):
        super().__init__(title, color, length, price, day_life)


daisy1 = Daisy('Маргаритка', 'желто-голубой', 35, 90, 30)
daisy2 = Daisy('Маргаритка', 'желто-розовый', 34, 90, 30)
daisy3 = Daisy('Маргаритка', 'желто-красный', 36, 90, 30)


class Bouquet():
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def __str__(self):
        return "\n".join(str(flower) for flower in self.flowers)

    def calc_cost(self):
        return sum(flower.price for flower in self.flowers)

    def avg_life(self):
        total_days = sum(map(lambda flower: flower.day_life, self.flowers))
        avg_day_life = total_days / len(self.flowers)
        return avg_day_life

    def sort_flowers(self, attribute):
        if all(map(lambda flower: hasattr(flower, attribute), self.flowers)):
            self.flowers.sort(key=lambda flower: getattr(flower, attribute))
        else:
            return "Неверный критерий сортировки"

    def search_flower_by_color(self, color):
        result = [flower for flower in self.flowers if flower.color == color]
        return result


bouquet1 = Bouquet()
bouquet1.add_flower(rose1)
bouquet1.add_flower(rose1)
bouquet1.add_flower(rose2)
bouquet1.add_flower(rose3)
bouquet1.add_flower(rose3)

print("Букет 1:")
print(bouquet1)

bouquet2 = Bouquet()
bouquet2.add_flower(tulip1)
bouquet2.add_flower(tulip2)
bouquet2.add_flower(tulip3)

print("Букет 2:")
print(bouquet2)

bouquet3 = Bouquet()
bouquet3.add_flower(rose3)
bouquet3.add_flower(tulip2)
bouquet3.add_flower(daisy1)

print("Букет 3:")
print(bouquet3)

print("\nСтоимость букета 1 в руб.:")
print(bouquet1.calc_cost())

print("\nПредполагаемый срок жизни букета 3 в днях:")
print(round(bouquet3.avg_life()))

bouquet1.sort_flowers('price')
print("\nБукет отсортирован по цене:")
print(bouquet1)

bouquet2.sort_flowers('length')
print("\nБукет отсортирован по длине стебля:")
print(bouquet2)

bouquet3.sort_flowers('day_life')
print("\nБукет отсортирован по сроку предполагаемой жизни:")
print(bouquet3)

yellow_flowers = bouquet2.search_flower_by_color('желтый')
if yellow_flowers:
    print("\nПоиск по желтому цвету:")
    for flower in yellow_flowers:
        print(flower)
else:
    print("\nЦветов с цветом 'желтый' не найдено.")

print("\nИмеет ли роза аромат:")
print(rose2.smell)
