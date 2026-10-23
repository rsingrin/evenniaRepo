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

    def func(self):
        mapping = {"Dragon":customObjects.Dragon,
               "Chair":customObjects.Chair}
        query = self.args.split()
        if not query:
            self.caller.msg("no input provided")
            return
        if not mapping.get(query[0]):
            self.caller.msg(f"no object class of type {mapping.get(query[0])} found")
            return
        
        evennia.create_object(f"typeclasses.customObjects.{query[0]}", key =query[1], location=self.caller.location)
    


"""
Chair commands

"""
class Sit(Command):
    """
    a command that checks to see if you can sit on the object mentioned, then does so
    """
    key = "sit"
    def func(self):
        ObjectName = self.args
        candidate = self.caller.search(ObjectName)
            



class Stand(Command):
    """
    a command that checks to see if you can stand up and then does so
    """
    key = "stand"
    def func(self):
        return





class stats(Command):
    """
    A simple echo command

    Usage:
        display stats

    """
    
    key = "stats"
    def func(self):
        self.caller.msg(self.msg(self.caller.get_stats()))
    
    
class quickfind(Command):
    """
    A search function, looks in the room and inventory

    Usage:
        quickfind <query>

    """
    key = "quickfind"
    def func(self):
        print("hi!")
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
        self.caller.msg(self.msg(self.args))
    
    
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
        
