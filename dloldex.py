

team_types = "fire"
super_effective_types = []
print("Your teams types are: " + str(team_types))


for types in team_types: check_supereffective(team_types)

def check_supereffective(types):
    if type == "fire":
        super_effective_types.append("grass")
        super_effective_types.append("bug")
        super_effective_types.append("steel")
        super_effective_types.append("ice")
        #return super_effective_types

    if type == "water":
        super_effective_types.append("rock")
        super_effective_types.append("ground")
        super_effective_types.append("water")

        return super_effective_types

print("Your team is super effective against: "
+ str(check_supereffective(team_types)))
