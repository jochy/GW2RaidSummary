from utils import parser
from utils import description
from utils import plotter

if __name__ == "__main__":
    # Parameters :
    player_list = "players.txt"
    logs_folder = "logs"

    # Reading the participating player file
    with open(player_list) as f:
        players_names = f.readlines()
    players_names = [x.strip() for x in players_names]

    # Instantiating the player objects in a player list
    players = []
    for i in players_names:
        players.append(description.Player(i))

    # Instantiating the different profession objects
    professions = description.init_professions()

    # Reading and parsing the logs
    fights, debug_variable = parser.parse(logs_folder, players, professions)

    # Display of the graphs
    plotter.plot_all(players, fights)

    # Debug for further console testing
    p = debug_variable['players']
    p = p[0]
    phases = debug_variable["phases"][0]
    dmg = phases["dmgStats"]
