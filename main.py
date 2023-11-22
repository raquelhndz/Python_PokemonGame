# Raquel Hernandez and Alice Huynh 
# 3/14/2023
# Pokemon Gym Battle
import random 
import fire
import water
import grass
import check_input
def main():
  #generate random type for gym leader
  gym_type = random.randint(0,2)
  if gym_type == 0:
    type_name = 'FIRE'
    gym_pokemon = [fire.Fire('Ninetales'), fire.Fire('Arcanine'), fire.Fire('Flareon')]
  elif gym_type == 1:
    type_name = 'WATER'
    gym_pokemon = [water.Water('Wartortle'), water.Water('Psyduck'), water.Water('Horsea')]
  elif gym_type == 2:
    type_name = 'GRASS'
    gym_pokemon = [grass.Grass('Bulbasaur'), grass.Grass('Ivysaur'), grass.Grass('Venusaur')]

  #make a list for player's pokemon
  player_pokemon = [fire.Fire('Charmander'), water.Water('Squirtle'), grass.Grass('Oddish')]

  #intro to the game
  print("PROF OAK: Hello Trainer! Today you're off to fight your first gym battle of 1 vs. 3 " + type_name + " pokemon.  Select the pokemon that you will fight with. \n1. I choose you, Charmander. \n2. Squirtle!  GO! \n3. We can do it, Oddish!")
  user_pokemon = check_input.get_int_range('Please choose your pokemon: ',1,3) #index for player_pokemon list
  print('\n--GYM BATTLE--') #game loop has to be after this line
  #for index in gym pokemon list? and if hp of users still exist
  #display gym leader's pokemon and player's pokemon
  
  while True:
    if player_pokemon[user_pokemon-1].hp != 0:
        if gym_pokemon[0].hp == 0:
          print("\nGYM LEADER: NOOO! You defeated my pokemon!!\n")
          gym_pokemon.pop(0)
          if len(gym_pokemon) == 0:
            print("You WON !!! ")
            break
        else:
          print('\nGYM LEADER: I choose you:')
          print(gym_pokemon[0])
          
        print()
        print(player_pokemon[user_pokemon-1])
    
    
      #choosing normal or special attack
        attack_type = check_input.get_int_range('Choose an attack type: \n 1. Normal \n 2. Special \nEnter attack type: ',1,2)
        gym_attack_type = random.randint(1, 2)
        gym_move = random.randint(1, 2)
        print ()
        if attack_type == 1: #normal attack
          print(player_pokemon[user_pokemon-1].get_normal_menu())
          moveInput = check_input.get_int_range('Enter move: ',1,2)
          if moveInput == 1:
            message = player_pokemon[user_pokemon-1].attack(gym_pokemon[0],attack_type, moveInput)
            print (message)
                
          if moveInput == 2:
            message = player_pokemon[user_pokemon-1].attack(gym_pokemon[0],attack_type, moveInput)
            print (message)
      
        if attack_type == 2: #special attack
          print(player_pokemon[user_pokemon-1].get_special_menu())
          moveInput = check_input.get_int_range('Enter move: ',1,2)
          if moveInput == 1:
            message = player_pokemon[user_pokemon-1].attack(gym_pokemon[0],attack_type, moveInput)
            print (message)
          if moveInput == 2:
            message = player_pokemon[user_pokemon-1].attack(gym_pokemon[0],attack_type, moveInput)
            print (message)
         #counter move
        if gym_pokemon[0].hp > 0:
            counter_message = gym_pokemon[0].attack(player_pokemon[user_pokemon-1], gym_attack_type, gym_move)
            print(counter_message)
              
    else:
      print('\nYOU LOST. Better Luck Next Time.')
      break
main()


