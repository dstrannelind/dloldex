#team_types = ["fire", "water", "grass", "psychic", "dark", "ground", "flying", "rock", "fightning", "steel", "ice"]
team_types = ["rock", "dark", "ghost", "poison", "fire", "fighting", "flying", "fairy", "dragon", "ground", "grass", "poison"]
#team_types = ["grass", "water"]
all_types = ["fire", "water", "grass", "steel", "poison", "ground", "rock", "electric", "dark", "fairy", "flying", "fighting", "ghost", "bug", "dragon", "ice", "psychic", "normal"]
super_effective_types = []



def check_supereffective(type, super_effective_types):

    
    if type == "fire":
        super_effective_types.append("grass")
        super_effective_types.append("bug")
        super_effective_types.append("steel")
        super_effective_types.append("ice")

        return super_effective_types

    if type == "water":
        super_effective_types.append("rock")
        
        super_effective_types.append("ground")
        super_effective_types.append("fire")
        #vfire += 1

        return super_effective_types

    if type == "grass":
        super_effective_types.append("water")
        #vwater += 1
        super_effective_types.append("ground")
        super_effective_types.append("rock")
        #vrock += 1
        return super_effective_types

    if type == "electric":
        super_effective_types.append("water")
        super_effective_types.append("flying")
              
        return super_effective_types

    if type == "ice":
        super_effective_types.append("grass")
        super_effective_types.append("ground")
        super_effective_types.append("flying")
        super_effective_types.append("dragon")

        return super_effective_types

    if type == "fighting":
        super_effective_types.append("normal")
        super_effective_types.append("ice")
        super_effective_types.append("rock")
        super_effective_types.append("dark")
        super_effective_types.append("steel")

        return super_effective_types

    if type == "poison":
        super_effective_types.append("grass")
        super_effective_types.append("fairy")
              
        return super_effective_types

    if type == "ground":
        super_effective_types.append("fire")
        super_effective_types.append("electric")
        super_effective_types.append("poison")
        super_effective_types.append("rock")
        super_effective_types.append("steel")
              
        return super_effective_types

    if type == "flying":
        super_effective_types.append("grass")
        super_effective_types.append("bug")
        super_effective_types.append("fighting")

        return super_effective_types

    if type == "psychic":
        super_effective_types.append("fightning")
        super_effective_types.append("poison")

        return super_effective_types

    if type == "bug":
        super_effective_types.append("grass")
        super_effective_types.append("psychic")
        super_effective_types.append("dark")
      
        return super_effective_types

    if type == "rock":
        super_effective_types.append("fire")
        super_effective_types.append("flying")
        super_effective_types.append("ice")
        super_effective_types.append("bug")
              
        return super_effective_types

    if type == "ghost":
        super_effective_types.append("psychic")
        super_effective_types.append("ghost")

        return super_effective_types

    if type == "dragon":
        super_effective_types.append("dragon")
       
        return super_effective_types

    if type == "dark":
        super_effective_types.append("psychic")
        super_effective_types.append("ghost")
              
        return super_effective_types

    if type == "steel":
        super_effective_types.append("ice")
        super_effective_types.append("rock")
        super_effective_types.append("fairy")
              
        return super_effective_types

    if type == "fairy":
        super_effective_types.append("fighting")
        super_effective_types.append("dragon")
        super_effective_types.append("dark")
              
        return super_effective_types


for types in team_types: 
   check_supereffective(types, super_effective_types)

#def rensa_lista(super_effective_types):
 #   rensad_lista = []
  #  rensad_lista = list(dict.fromkeys(rensad_lista))
   # return rensad_lista


rensad_lista = list(dict.fromkeys(super_effective_types))
missed_pokes = list(set(all_types) - set(rensad_lista))


print("Your teams types are: " + str(team_types))
print("Your team is super effective against: " + str(rensad_lista))
if missed_pokes == []:
    print("Congratulations, your team is super effective against ALL types! ggwp ")
else:
    print("You do NOT have super effective against: " + str(missed_pokes))

