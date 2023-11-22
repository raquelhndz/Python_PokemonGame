import abc
import random 

class Pokemon(abc.ABC):
  def __init__(self, name , type):
    ''' Sets the _name, and _type using the parameters, assigns the _battle_table and sets _hp to 25. '''
    
    self._name = name
    self._type = type
    self._battle_table = [[1, .5, 2], [2, 1, .5], [.5, 2, 1]] # Fire(opponent strength (f w g)) Water Grass
    self._hp = 25

  @property
  def hp(self):
    ''' Get the value of _hp. '''
    return self._hp


  def _normal_move(self, opponent, move):
    ''' Uses the move parameter to choose to call either 
slam or tackle method, returns the string returned from those methods. '''
    
    if move == 1:
      attackMessage = self._slam(opponent)
    if move == 2:
      attackMessage = self._tackle(opponent)
    return attackMessage

    
  def get_normal_menu(self):
    ''' Returns the menu. '''
    
    return "Choose a Move: \n 1. Slam \n 2. Tackle"

  def _slam(self, opponent):
    ''' Randomizes some damage, calls move on the opponent and return a string description of the move 
using both pokemons names, the type of move, and the amount of damage taken. '''
    
    damage = random.randint(1, 8)
    opponent._hp = opponent._take_damage(damage)
    return "\n"+ self._name + " SLAMS " + opponent._name + " for " + str(damage) + " damage"

  def _tackle(self, opponent):
    ''' Randomizes some damage, calls move on the opponent and return a string description of the move 
using both pokemons names, the type of move, and the amount of damage taken. '''
    
    damage = random.randint(3, 6)
    opponent._hp = opponent._take_damage(damage)
    return "\n"+ self._name + " TACKLES " + opponent._name + " for " + str(damage) + " damage"


  @abc.abstractmethod
  def get_special_menu(self):
    ''' Abstract menu to be overriden in other classes. '''
    pass
    
  @abc.abstractmethod
  def _special_move(self, opponent, move):
    ''' Abstract moves to be overriden in other classes. '''
    pass

  def attack(self, opponent, type, move):
    ''' Uses the type parameter to choose to call either 
_normal_move or _special_move. '''
    
    if type == 1:
      attackMessage = self._normal_move(opponent, move)
    if type == 2:
      attackMessage = self._special_move(opponent, move)
    return attackMessage

  def __str__(self):
    ''' Returns string of name and hp. '''
    
    return self._name + " HP: " + str(self.hp) + "/25"

  def _take_damage(self, dmg):
    ''' Calculate hp. '''
    self._hp = (self._hp) - dmg
    if self._hp < 0:
      self._hp = 0
    return self._hp
    
    
    
  
  