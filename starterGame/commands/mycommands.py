from commands.command import Command
from evennia import CmdSet

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
        
        
class myCmdSet(CmdSet):
    def at_cmdset_creation(self):
        self.add(CmdEcho)
        self.add(stats)
        self.add(quickfind)