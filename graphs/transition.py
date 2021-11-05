from dataclasses import dataclass
from typing import Optional, Tuple
from predicates.state import State
from predicates.guards import Guard
from predicates.actions import Action
from predicates.errors import NextException

# A Transition class includes a name of the transition, a guard predicate 
# and a list of actions.
# The class should implement both the eval method and the next method
# in the same way as the guards and the actions. Look at the test so the 
# method parameters and return types are correct.
# 
#    
@dataclass(frozen=True, order=True)
class Transition(object):
    name: str
    guard: Guard
    actions: Tuple[Action]


        

