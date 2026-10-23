"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from random import randint
from evennia.objects.objects import DefaultCharacter
from .objects import ObjectParent


class Character(ObjectParent, DefaultCharacter):
    """
    The Character just re-implements some of the Object's methods and hooks
    to represent a Character entity in-game.

    See mygame/typeclasses/objects.py for a list of
    properties and methods available on all Object child classes like this.

    """
    
    def at_object_creation(self):
        """
        Called when object is first created.
        """
        self.db.strength = randint(1, 20)
        self.db.dex = randint(1, 20)
        self.db.wis = randint(1, 20)        
        self.db.isStanding = True
        
    
    
    def get_stats(self):
        return f"Strength: {self.db.strength}, Dexterity: {self.db.dex}, Wisdom: {self.db.wis}"

    pass
