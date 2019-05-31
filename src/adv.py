from room import Room
from player import Player
from items import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Create Items

item = {
    'dust':  Item('Dust',
                  'You have no need to use dust at this time.')
}

# Items in rooms

room['foyer'].items = item['dust']

# Main

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


player = Player(input('Enter your name here: '), room['outside'], [])
player.display_room()
action = input(
    'Move North(n), South(s), East(e), or West(w) \nItem Action(i) \nQuit Game(q)\n\n')
player.action_input(action)

while True:
    if action == 'q':
        break
    elif player.current_room is not None:
        player.display_room()
        player.if_player_sees_item()
        action = input(
            'Move North(n), South(s), East(e), or West(w) \nItem Action(i) \nQuit Game(q)\n\n')
        player.action_input(action)
        continue
    else:
        print('No room exists here. Please choose another direction.')
