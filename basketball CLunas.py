class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

#tried to define the __init_ using 'for k,v in player_dict.items(), but could not get __repr_ to work or succeed with a printable output
# did get the player dictionary assigned to memory however...will press on figuring out that approach

    def __repr__(self):
        display = f'Player: {self.name}, Age: {self.age}, Position: {self.position}, Team: {self.team}'
        return display

#    @classmethod						#not understanding how to pass an instance to this
#    def add_player(cls,team_list):
#        player_stats = []
#        for dict in team_list:
#            player_stats.append(cls(dict))
#        return player_stats

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    }

jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    }

kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    }

damien = {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    }

joel = {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    }

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)
player_damien = Player(damien)
player_joel = Player(joel)

print(player_kevin)
print(player_jason)
print(player_kyrie)
print(player_damien)
print(player_joel)