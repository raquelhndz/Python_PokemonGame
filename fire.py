import pokemon
import random 
class Fire(pokemon.Pokemon):
  def __init__(self, name):
    super().__init__(name,0)

  def get_special_menu(self):
    ''' Prints menu specific to the Fire Type. '''
    
    return "Choose a Move: \n 1. Ember \n 2. Fire Blast"

  def _special_move(self,opponent, move):
    ''' Choose between two special moves and call correct function.'''
    
    if move == 1:
      attack = self._ember(opponent)
    if move == 2:
      attack = self._fire_blast(opponent)
    return attack #str

  def _ember(self, opponent):
    ''' Randomizes damage, looks up the multiplier in 
the battle table based on the two pokemon’s type and calculate the total damage the 
opposing pokemon will take. Returns 
a string description of the move. '''
    
    damage = random.randint(1, 5)
    multiplier = self._battle_table[self._type][opponent._type]
    total_damage = int(damage * multiplier)
    opponent._hp = opponent._take_damage(total_damage)
    if multiplier == 2:
      effective = " It is SUPER effective. "
    if multiplier == .5 or multiplier == 1: #need to check this
      effective = " It is not very effective. "
    return "\n"+ self._name + " engulfs " + opponent._name + " in EMBERS for " + str(total_damage) + " damage. "+ effective

  def _fire_blast(self, opponent):
    ''' Randomizes damage, looks up the multiplier in 
the battle table based on the two pokemon’s type and calculate the total damage the 
opposing pokemon will take. Returns 
a string description of the move. '''
    
    damage = random.randint(3, 4)
    multiplier = self._battle_table[self._type][opponent._type]
    total_damage = int(damage * multiplier)
    opponent._hp = opponent._take_damage(total_damage)
    if multiplier == 2:
      effective = " It is SUPER effective. "
    if multiplier == .5 or multiplier == 1:
      effective = " It is not very effective. "
    return "\n" + self._name + " BLASTS " + opponent._name + " with FIRE for " + str(total_damage) + " damage. "+ effective
