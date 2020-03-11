# Implement a class to hold room information. This should have name and
# description attributes.
from direction import Direction

class Room:

    def __init__(self,name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'Room (name: {self.name},description: {self.description})'

    # def check_path(self,direction: Direction):
    #     try:
    #         return getattr(self,Direction[direction].value))
    #     except KeyError as err:
    #         return f'{err} not a valid direction'
    #     except AttributeError as err:
    #         return f'No path found'
        


        