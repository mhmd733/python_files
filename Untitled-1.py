player ={
     "kira" : "online",
     "bob77" : "offline",
     "anitamaxwin" : "online",
     "west" : "online" 
}
# output => 3
def players_count(player):
    result =[]
    for key, value in player.items():
        if value == "online":
            result.append(key)
    return result
print(len(players_count(player)))