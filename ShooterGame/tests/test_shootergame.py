import pytest
from shootergame.class_maps import Map
from shootergame.class_objects import Damageable, Objects, Rock, Crate, Building
from shootergame.class_characters import Character, Player, Enemy
from shootergame.class_ammunition import Bullet
from shootergame.class_point import Point





# Point fixture to use in tests
@pytest.fixture
def myTestPoint():
    "Returns a point instance with x == 1 and y == 2"
    return Point(1, 2)

# Point to use in parametrized tests
myPoint1 = Point(1, 2)





# testing Point input and methods
def test_point_values(myTestPoint):
    assert myTestPoint.x == 1
    assert myTestPoint.y == 2

def test_point_no_values():
    myPoint = Point()
    assert myPoint.x == 0
    assert myPoint.y == 0

@pytest.mark.parametrize("x, y", [("10", 20),(10, "20")])
def test_point_values_wrong_type(x, y):
    with pytest.raises(TypeError):
        myPoint = Point(x, y)

@pytest.mark.parametrize("x, y", [(-1, 5), (5, -1)])
def test_point_values_wrong_value(x, y):
    with pytest.raises(ValueError):
        myPoint = Point(x, y)

def test_point_translation(myTestPoint):
    myTestPoint.translation(10, 10, 2)
    assert myTestPoint.x == 21
    assert myTestPoint.y == 22

def test_point_translation_no_values(myTestPoint):
    myTestPoint.translation()
    assert myTestPoint.x == 11
    assert myTestPoint.y == 12

@pytest.mark.parametrize("dX, dY, spd",[("10", 10, 2),(10, "10", 2), (10, 10, "2")])
def test_point_translation_wrong_type(myTestPoint, dX, dY, spd):
    with pytest.raises(TypeError):
        myTestPoint.translation(dX, dY, spd)

@pytest.mark.parametrize("dX, dY, spd", [(-15, 10, 2), (-5, 15, 2), (-5, 10, 7)])
def test_point_translation_wrong_values(myTestPoint, dX, dY, spd):
    with pytest.raises(ValueError):
        myTestPoint.translation(dX, dY, spd)





# testing Objects superclass
def test_object_values(myTestPoint):
    myObject = Objects(myTestPoint, 5, 5)
    assert myObject.x == 1
    assert myObject.y == 2
    assert myObject.size == 25

def test_object_no_values():
    with pytest.raises(Exception):
        myObject = Objects()

@pytest.mark.parametrize("p, h, w",[((1,2), 5, 5),(myPoint1, "5", 5),(myPoint1, 5, "5")])
def test_object_values_wrong_type(p, h ,w):
    with pytest.raises(TypeError):
        myObject = Objects(p, h, w)






# testing Rock input and methods
def test_rock_values(myTestPoint):
    myRock = Rock(myTestPoint, 20, 4)
    assert myRock.height == 20
    assert myRock.width == 4
    assert myRock.x == 1
    assert myRock.y == 2
    assert myRock.size == 80

def test_rock_no_values():
    with pytest.raises(Exception):
        myRock = Rock()

@pytest.mark.parametrize("h, w", [(3, 5),(5, 25)])
def test_rock_values_wrong_value(myTestPoint, h, w):
    with pytest.raises(ValueError):
        myRock = Rock(myTestPoint, h, w)





# testing Damageable subclass
def test_damageable_values(myTestPoint):
    myDamageable = Damageable(myTestPoint, 1, 2, 3)
    assert myDamageable.health == 3
    assert myDamageable.height == 1

def test_damageable_no_values():
    with pytest.raises(Exception):
        myDamageable = Damageable()

@pytest.mark.parametrize("p, h, w, health",[((1,2), 5, 5, 5),(myPoint1, "5", 5, 5),(myPoint1, 5, "5", 5),(myPoint1, 5, 5, "5")])
def test_damageable_values_wrong_type(p, h,w, health):
    with pytest.raises(TypeError):
        myObject = Objects(p, h, w, health)

def test_damaged_by_ammunition():
    pass





# testing Building input and methods
def test_building_values(myTestPoint):
    myBuilding = Building(myTestPoint, 40, 40, 300)
    assert myBuilding.x == 1
    assert myBuilding.y == 2
    assert myBuilding.height == 40
    assert myBuilding.size == 1600
    assert myBuilding.health == 300

def test_building_no_values():
    with pytest.raises(Exception):
        myBuilding = Building()

@pytest.mark.parametrize("h, w, health",[(9, 40, 150),(10, 41, 150),(10, 40, 301)])
def test_building_values_wrong_value(myTestPoint, h, w, health):
    with pytest.raises(ValueError):
        myBuilding = Building(myTestPoint, h, w, health)





# testing Crate input and methods
def test_crate_values(myTestPoint):
    myCrate = Crate(myTestPoint, 10, 10, 50, True)
    assert myCrate.x == 1
    assert myCrate.width == 10
    assert myCrate.size == 100
    assert myCrate.health == 50
    assert myCrate.armourValue == 10

def test_crate_no_values():
    with pytest.raises(Exception):
        myCrate = Crate()

def test_crate_values_wrong_type(myTestPoint):
    with pytest.raises(TypeError):
        myCrate = Crate(myTestPoint, 10, 10, 50, "True")

@pytest.mark.parametrize("h, w, health",[(9, 10, 45),(10, 9, 45),(10, 10, 55)])
def test_crate_values_wrong_value(myTestPoint, h, w, health):
    with pytest.raises(ValueError):
        myCrate = Crate(myTestPoint, h, w, health, False)

def test_crate_powerup_dropped():
    pass





# testing Map input and methods
def test_map_values():
    myMap = Map(1000, 5000)
    assert myMap.height == 1000
    assert myMap.size == 5000000

def test_map_no_values():
    with pytest.raises(Exception):
        myMap = Map()

@pytest.mark.parametrize("h, w",[("1000", 5000), (1000, "5000")])
def test_map_values_wrong_type(h, w):
    with pytest.raises(TypeError):
        myMap = Map(h, w)





# testing Character superclass
def test_character_values(myTestPoint):
    myCharacter = Character(myTestPoint, 5, 10, 80, 20, 2)
    assert myCharacter.x == 1
    assert myCharacter.width == 5
    assert myCharacter.size == 50
    assert myCharacter.health == 80
    assert myCharacter.firepower == 20
    assert myCharacter.speed == 2

def test_character_no_values():
    with pytest.raises(Exception):
        myCharacter = Character()

@pytest.mark.parametrize("point, h, w, health, fire, spd",[
    ("myPoint1", 5, 10, 80, 20, 2),
    (myPoint1, "5", 10, 80, 20, 2),
    (myPoint1, 5, "10", 80, 20, 2),
    (myPoint1, 5, 10, "80", 20, 2),
    (myPoint1, 5, 10, 80, "20", 2),
    (myPoint1, 5, 10, 80, 20, "2")
    ])
def test_character_values_wrong_type(point, h, w, health, fire, spd):
    with pytest.raises(TypeError):
        myCharacter = Character(point, h, w, health, fire, spd)





# testing Player input and methods
def test_player_values(myTestPoint):
    myPlayer = Player(myTestPoint, 5, 10, 80, 20, 2, True)
    assert myPlayer.x == 1
    assert myPlayer.width == 5
    assert myPlayer.size == 50
    assert myPlayer.health == 80
    assert myPlayer.firepower == 20
    assert myPlayer.speed == 2
    assert myPlayer.armourValue == 20

def test_player_no_value():
    with pytest.raises(Exception):
        myPlayer = Player()

def test_player_values_wrong_type(myTestPoint):
    with pytest.raises(TypeError):
        myPlayer = Player(myTestPoint, 5, 10, 80, 20, 2, "True")

@pytest.mark.parametrize("h, w, health, fire, spd", [
    (1, 10, 80, 20, 2),
    (5, 20, 80, 20, 2),
    (5, 10, 10, 20, 2),
    (5, 10, 80, 80, 2),
    (5, 10, 80, 20, 9)
])
def test_player_values_wrong_value(myTestPoint, h, w, health, fire, spd):
    with pytest.raises(ValueError):
        myPlayer = Player(myTestPoint, h, w, health, fire, spd, False)

def test_player_movement(myTestPoint):
    myPlayer = Player(myTestPoint, 5, 10, 80, 20, 2, False)
    myPlayer.point.translation(10, 0, myPlayer.speed)
    assert myPlayer.x == 21
    assert myPlayer.y == 2

def test_player_shoot():
    pass

def test_player_edge_reached():
    pass

def test_player_rotation():
    pass

def test_player_health_increased():
    pass

def test_player_armour_increased():
    pass

def test_player_firepower_increased():
    pass





# testing Enemy input and methods
def test_enemy_values(myTestPoint):
    myEnemy = Enemy(myTestPoint, 5, 10, 80, 20, 2)
    assert myEnemy.x == 1
    assert myEnemy.width == 5
    assert myEnemy.size == 50
    assert myEnemy.health == 80
    assert myEnemy.firepower == 20
    assert myEnemy.speed == 2

def test_enemy_no_value():
    with pytest.raises(Exception):
        myEnemy = Enemy()

@pytest.mark.parametrize("h, w, health, fire, spd", [
    (1, 10, 80, 20, 2),
    (5, 20, 80, 20, 2),
    (5, 10, 10, 20, 2),
    (5, 10, 80, 80, 2),
    (5, 10, 80, 20, 9)
])
def test_enemy_values_wrong_value(myTestPoint, h, w, health, fire, spd):
    with pytest.raises(ValueError):
        myEnemy = Enemy(myTestPoint, h, w, health, fire, spd)

def test_enemy_movement(myTestPoint):
    myEnemy = Enemy(myTestPoint, 5, 10, 80, 20, 2)
    myEnemy.point.translation(10, 0, Enemy.speed)
    assert myEnemy.x == 21
    assert myEnemy.y == 2

def test_enemy_shoot():
    pass

def test_enemy_edge_reached():
    pass

def test_enemy_rotation():
    pass





# testing bullet input and methods
def test_bullet_values():
    pass

def test_bullet_no_values():
    pass

def test_bullet_values_wrong_type():
    pass

def test_bullet_values_wrong_value():
    pass

def test_bullet_movement():
    pass

def test_bullet_edge_reached():
    pass

def test_bullet_impact():
    pass