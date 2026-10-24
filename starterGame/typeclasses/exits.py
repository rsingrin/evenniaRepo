"""
Exits

Exits are connectors between Rooms. An exit always has a destination property
set and has a single command defined on itself with the same name as its key,
for allowing Characters to traverse the exit to its destination.

"""

from evennia.objects.objects import DefaultExit

from .objects import ObjectParent


class Exit(ObjectParent, DefaultExit):
    """
    Exits are connectors between rooms. Exits are normal Objects except
    they defines the `destination` property and overrides some hooks
    and methods to represent the exits.

    See mygame/typeclasses/objects.py for a list of
    properties and methods available on all Objects child classes like this.

    """

    def at_failed_traverse(self, traversing_object, **kwargs):
        # Character.at_pre_move blocks seated characters; say why instead
        # of the generic "You cannot go there."
        if traversing_object.db.sitting_on is not None:
            traversing_object.msg("you are sitting!")
            return
        super().at_failed_traverse(traversing_object, **kwargs)
