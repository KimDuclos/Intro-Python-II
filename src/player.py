# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return str(self.__dict__)

    def action_input(self, decision):
        error = '\nNo room exists here. Try another direction.\n'
        if decision == 'n':
            if self.current_room.n_to is not None:
                self.current_room = self.current_room.n_to
            else:
                print(error)
        elif decision == 's':
            if self.current_room.s_to is not None:
                self.current_room = self.current_room.s_to
            else:
                print(error)
        elif decision == 'e':
            if self.current_room.e_to is not None:
                self.current_room = self.current_room.e_to
            else:
                print(error)
        elif decision == 'w':
            if self.current_room.w_to is not None:
                self.current_room = self.current_room.w_to
            else:
                print(error)
        elif decision == 'i':
            if self.inventory is not None:
                self.drop_item()
            else:
                print('Your inventory currently contains no items.')
        # else:
        #     print('error')

    def if_player_sees_item(self):
        if self.current_room.items:
            pick_up = input(
                f'There is an item in this location. ***{self.current_room.items.name}*** Would you like to pick it up? (Type y/n)')
            current_item = self.current_room.items
            self.pick_up_item(pick_up)

    def pick_up_item(self, decision):
        if decision == 'y':
            # add the item to inventory of player
            self.inventory.append(self.current_room.items)
            # remove item from room
            print(
                f'{self.name}, You have picked up {self.current_room.items.name}')
            self.current_room.items = None
            for i, item in enumerate(self.inventory):
                print(f'{item.name}, {item.description}')

        elif decision == 'n':
            print('Continue')

    def drop_item(self):
        for i, item in enumerate(self.inventory):
            print(f'{item.name} -- {item.description}')
        drop = input(
            'Would you like to store any items in your inventory? Type name of item to store.')

        for i, item in enumerate(self.inventory):
            print(f'{item.name}')
            if item.name == drop:
                del self.inventory[i]

    def display_room(self):
        print(
            f'Current Room: {self.current_room.name}\n \n{self.current_room.description}\n\n')
        if len(self.inventory) > 0:
            for i, item in enumerate(self.inventory):
                print(f'Inventory: {item.name}')
