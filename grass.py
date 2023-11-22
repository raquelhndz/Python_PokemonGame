import pokemon
import random 
class Grass(pokemon.Pokemon):
  def __init__(self, name):
    super().__init__(name,2)

    
  def get_special_menu(self):
    ''' Prints menu specific to the Grass Type. '''
    
    return "Choose a Move: \n 1. Razor Leaf \n 2. Solar Beam"

  def _special_move(self,opponent, move):
    ''' Choose between two special moves and call correct function.'''
    
    if move == 1:
      attack = self._razor_leaf(opponent)
    if move == 2:
      attack = self._solar_beam(opponent)
    return attack #str

  def _razor_leaf(self, opponent):
    ''' Randomizes damage, looks up the multiplier in 
the battle table based on the two pokemon’s type and calculate the total damage the 
opposing pokemon will take. Returns 
a string description of the move. '''
    
    damage = random.randint(1, 5)
    multiplier = self._battle_table[self._type][opponent._type]
    total_damage = int(damage * multiplier)
    opponent._hp = opponent._take_damage(total_damage)
    if multiplier == 2:
      effective = " It is effective. "
    if multiplier == .5 or multiplier == 1:
      effective = " It is not effective. "
    return "\n"+ self._name + " engulfs " + opponent._name + " in RAZOR LEAF for " + str(total_damage) + " damage. "+ effective

  def _solar_beam(self, opponent):
    ''' Randomizes damage, looks up the multiplier in 
the battle table based on the two pokemon’s type and calculate the total damage the 
opposing pokemon will take. Returns 
a string description of the move. '''
    
    damage = random.randint(3, 4)
    multiplier = self._battle_table[self._type][opponent._type]
    total_damage = int(damage * multiplier)
    opponent._hp = opponent._take_damage(total_damage)
    if multiplier == 2:
      effective = " It is effective. "
    if multiplier == .5 or multiplier == 1:
      effective = " It is not effective. "
    return "\n"+ self._name + " BLASTS " + opponent._name + " with SOLAR BEAM for " + str(total_damage) + " damage. "+ effective
