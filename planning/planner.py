from typing import List, Optional, Set
from graphs.transition import Transition
from predicates.guards import Guard
from predicates.state import State


def plan(initial_state: State, transitions: List[Transition], goal: Guard) -> Optional[List[str]]:
    """
    Implement a planning algorithm that can find the shortest path from the 
    initial state to a state where the goal predicate is true. It is not necessary to 
    first create a graph but can instead search using states and transitions.
    The path should be created based on the names of the transitions. 

    If the algorithm does not find a path to the goal, return None.
    """

    raise NotImplementedError