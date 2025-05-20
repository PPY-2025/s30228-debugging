from main import Character, Warrior, Mage

def test_take_damage():
    c = Character("Test", 50)
    c.take_damage(20)
    assert c.hp is 30

def test_take_damage_warrior():
    c = Character("Test", 50)
    w = Warrior("Test", 50, 10)
    w.attack(c)
    assert c.hp is 35

def test_take_damage_mage():
    c = Character("Test", 50)
    m = Mage("Test", 50, 10)
    m.attack(c)
    assert c.hp is 25
    assert m.mana is 0