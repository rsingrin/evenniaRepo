from commands.command import Command
from evennia import CmdSet
import evennia
import typeclasses.customObjects as customObjects


"""
builder crap
"""

class CreateMyJunk(Command):
    """
    A foolish attempt to never use the py command

    """
    key = "CreateMyJunk"
    locks = "cmd:perm(Builder)"

    def func(self):
        mapping = {"dragon":customObjects.Dragon,
               "sittable":customObjects.Sittable}
        query = self.args.split()
        if len(query) < 2:
            self.caller.msg("usage: CreateMyJunk <type> <name>")
            return
        typeclass = mapping.get(query[0].lower())
        if not typeclass:
            self.caller.msg(f"no object class of type {query[0]} found")
            return

        name = " ".join(query[1:])
        evennia.create_object(typeclass, key=name, location=self.caller.location)
        self.caller.msg(f"created {query[0].lower()} '{name}'")



"""
Chair commands

"""
class Sit(Command):
    """
    a command that checks to see if you can sit on the object mentioned, then does so
    """
    key = "sit"
    def func(self):
        ObjectName = self.args.strip()
        
        if self.caller.db.sitting_on is not None:
            self.caller.msg("you are already sitting!")
            return
        
        if not ObjectName:
            self.caller.msg("sit on what?")
            return

        # only look in the room, not in our inventory
        candidate = self.caller.search(ObjectName, location=self.caller.location)
        if candidate is None:
            # search already told the caller what went wrong
            return

        if not candidate.tags.has("sittable"):
            self.caller.msg("object is not sittable!")
            return

        # see if anyone else in the room is already sitting on it
        for obj in self.caller.location.contents:
            if obj.db.sitting_on == candidate:
                self.caller.msg(f"{obj.key} is already sitting on {candidate}!")
                return

        self.caller.msg(f"you sit on {candidate}")
        self.caller.location.msg_contents(f"{self.caller.key} sits on {candidate}.", exclude=self.caller)
        self.caller.db.sitting_on = candidate
            



class Stand(Command):
    """
    a command that checks to see if you can stand up and then does so
    """
    key = "stand"
    def func(self):
        if self.caller.db.sitting_on is None:
            self.caller.msg("you are already standing!")
            return
        chair = self.caller.db.sitting_on
        self.caller.msg(f"you stand up from {chair}")
        if self.caller.location:
            self.caller.location.msg_contents(f"{self.caller.key} stands up from {chair}.", exclude=self.caller)
        self.caller.db.sitting_on = None





class stats(Command):
    """
    A simple echo command

    Usage:
        display stats

    """
    
    key = "stats"
    def func(self):
        self.caller.msg(self.caller.get_stats())
    
    
class quickfind(Command):
    """
    A search function, looks in the room and inventory

    Usage:
        quickfind <query>

    """
    key = "quickfind"
    def func(self):
        query = self.args
        result = self.caller.search(query)
        if not result:
            return
        self.caller.msg(f"Found match for {query}: {result}")
        
    
class CmdEcho(Command):
    """
    A simple echo command

    Usage:
        echo <something>

    """
    
    key = "echo"
    def func(self):
        self.caller.msg(self.args)
    
    
class CmdHit(Command):
    """
    hittin sumthin
    """
    key = "hit"
    def func(self):
        self.caller.msg("I hit somthing!")
    
    
    
    
class attackCmdSet(CmdSet):
    def at_cmdset_creation(self):
        self.add(CmdHit)
        
class chairCmdSet(CmdSet):
    def at_cmdset_creation(self):
        self.add(Sit)
        self.add(Stand)

class myCmdSet(CmdSet):
    def at_cmdset_creation(self):
        self.add(CmdEcho)
        self.add(stats)
        self.add(quickfind)
        
class builderCrap(CmdSet):
    def at_cmdset_creation(self):
        self.add(CreateMyJunk)
        
