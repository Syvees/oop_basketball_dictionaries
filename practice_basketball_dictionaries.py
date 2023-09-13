class Player:
        def __init__(self,person): #Challenge 1: Update the Constructor
                self.name = person["name"]
                self.age = person["age"]
                self.position = person["position"]
                self.team = person["team"]
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

#Challenge 2: Create instances using individual player dictionaries
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

#print(player_kevin.name, player_kevin.age, player_kevin.position, player_kevin.team)
# print(player_kyrie.age)
# print(player_jason.team)

players = [
        {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
        },
        {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
        },
        {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
        },
        {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
        },
        {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
        },
        {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
        }
        ]

#Challenge 3: Make a list of Player instances from a list of dictionaries
new_team = []
for member in players:
        team_member = Player(member)
        new_team.append(team_member)
print(new_team)