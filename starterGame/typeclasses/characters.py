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
        self.db.sitting_on = None  


    def at_pre_move(self, destination, move_type="move", **kwargs):
        # only block walking through exits; teleports, `home` etc. still work.
        # the exit's at_failed_traverse tells us why
        if self.db.sitting_on is not None and move_type == "traverse":
            return False
        return super().at_pre_move(destination, move_type, **kwargs)

    def at_post_move(self, source_location, move_type="move", **kwargs):
        # if we got moved away from our chair some other way, we're not sitting anymore
        chair = self.db.sitting_on
        if chair is not None and chair.location != self.location:
            self.db.sitting_on = None
        super().at_post_move(source_location, move_type, **kwargs)

    def at_pre_unpuppet(self, **kwargs):
        # we get moved out of the room on logout, so get up first or the
        # chair will look free while we're gone
        self.db.sitting_on = None
        super().at_pre_unpuppet(**kwargs)

    def get_display_desc(self, looker, **kwargs):
        desc = super().get_display_desc(looker, **kwargs)
        if self.db.sitting_on is not None:
            desc += f"\n{self.key} is sitting on {self.db.sitting_on.get_display_name(looker)}."
        return desc

    def get_stats(self):
        return f"Strength: {self.db.strength}, Dexterity: {self.db.dex}, Wiz: {self.db.wis}"
