# Zadanie 1

def factorial(n):
    if n == 0:
        return 1 # nie 0, a 1
    return n * factorial(n - 1)

# Zadanie 2

def get_grades():
    return [5, 4, "3", 2, 1] # zmienne typu string nie są policzalne

def calculate_average(grades):
    if all(type(x) == type(grades[0]) for x in grades):
        return sum(grades) / len(grades)
    else: raise TypeError

def to_word_grade(avg):
    if avg >= 4.5:
        return "bardzo dobry"
    elif avg >= 3.5:
        return "dobry"
    elif avg >= 2.5:
        return "dostateczny"
    else:
        return "niedostateczny"

def show_result():
    grades = get_grades()
    try:
        avg = calculate_average(grades)
        word = to_word_grade(avg)
        print(f"Średnia: {avg:.2f}, Ocena: {word}")
    except TypeError:
        print('All variables of the list must have numeric type.')

show_result()

# Zadanie 3

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        damage = int(round(amount)) # konwertacja w int dla spójności typów
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

class Warrior(Character):
    def __init__(self, name, hp, strength):
        super().__init__(name, hp)
        self.strength = strength

    def attack(self, target):
        damage = self.strength * 1.5
        target.take_damage(damage)

class Mage(Character):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def attack(self, target):
        if self.mana >= 10:
            target.take_damage(25)
            self.mana -= 10
        else:
            print("Not enough mana!")

def simulate_battle():
    w = Warrior("Thorgal", 100, 10)
    m = Mage("Merlin", 60, 20)

    print("Start:", w.hp, m.hp)
    w.attack(m)
    m.attack(w)
    m.attack(w)
    m.attack(w)
    m.attack(w)
    print("End:", w.hp, m.hp)

    assert w.hp == 50, f"Thorgal should have 50 HP, got {w.hp}"
    assert m.hp == 45, f"Merlin should have 45 HP, got {m.hp}"
    assert m.mana == 0, f"Merlin should have 0 mana, got {m.mana}"

simulate_battle()