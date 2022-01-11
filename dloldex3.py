team_types = ["fire", "water", "grass", "psychic", "dark"]
super_effective_types = []
print("Your teams types are: " + str(team_types))




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
        super_effective_types.append("water")

        return super_effective_types

    if type == "grass":
        super_effective_types.append("water")
        super_effective_types.append("ground")
        super_effective_types.append("rock")
      
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

    if type == "fightning":
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


#for types in team_types: 
 #   check_supereffective(types, super_effective_types)

check_supereffective(team_types[0], super_effective_types)
check_supereffective(team_types[1], super_effective_types)
check_supereffective(team_types[2], super_effective_types)
check_supereffective(team_types[3], super_effective_types)

print("Your team is super effective against: " + str(check_supereffective(team_types[4], super_effective_types)))

#print("Your team is super effective against: " + str(super_effective_types))