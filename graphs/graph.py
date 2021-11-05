from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Tuple
from predicates.state import State


@dataclass(frozen=True, order=True)
class Vertex(object):
    name: str
    """
    This class represents the vertices (or nodes) in a graph and is just a name that in simple
    cases will be named the same as the state. Later on we may add more things to
    this class if we need to. When creating this and have a state, use Vertex.from_state(state)
    You do not need to change this class
    """

    @classmethod
    def from_state(cls, state: State) -> Vertex:
        return cls(str(state))

@dataclass(frozen=True, order=True)
class Edge(object):
    name: str
    tail: Vertex
    head: Vertex
    """
    This class represents the edges of a graph and connects two vertices defining how 
    it is possible to navigate in the graph. If you have two states, use the 
    Edge.from_states(name, state_tail, state_head) so that the names will be correct
    You do not need to change this class
    """

    @classmethod
    def from_states(cls, name: str, tail: State, head: State) -> Edge:
        return cls(name, Vertex.from_state(tail), Vertex.from_state(head))


# When creating a new graph, you need to decide what fields the constructor should have
# and what you plan to save in the graph. I have added a dataclass decorator so you just add your fields 
# directly after te class name like the other classes. This class is not immutable (frozen) since you may 
# want to create a graph and then add more to it after that. Either you create the full representation of 
# the graph before creating it or you can also create an empty graph and add new vertices and edges to it.
# If you need to add data to it after creation, just add new methods to the graph. Also remember to write 
# tests for it
#  
# You also need to decide how you store the parts of the graph inside this class.
#
# Observe, the graph should not know anything about Transitions, States, Guards and actions!
@dataclass
class Graph(object):
    ## Add your fields here!!

    def outgoing(self, vertex: Vertex) -> list[Edge]:
        """
        This method should return all edges that are outgoing from the given vertex
        """
        raise NotImplementedError

    def incoming(self, vertex: Vertex) -> list[Edge]:
        """
        This method should return all edges that are incoming to the given vertex
        """
        raise NotImplementedError

    def successor(self, vertex: Vertex) -> list[Vertex]:
        """
        This method should return all vertices that are successors to the given vertex
        """
        raise NotImplementedError

    def predecessor(self, vertex: Vertex) -> list[Vertex]:
        """
        This method should return all vertices that are preceding the given vertex
        """
        raise NotImplementedError

    def from_path(self, vertex: Vertex, path: list[str]) -> Optional[Vertex]:
        """
        This method should return the vertex that you will reach if you follow
        the path of edge names from the given vertex, or None if the path 
        does not exists. 
        """
        raise NotImplementedError


    def source_vertices(self) -> list[Vertex]:
        """
        This method should return all vertices that are source vertices
        meaning that they do not have any incoming edges
        """
        raise NotImplementedError

    def sink_vertices(self) -> list[Vertex]:
        """
        This method should return all vertices that are sink vertices
        meaning that they do not have any outgoing edges
        """
        raise NotImplementedError


    # the below methods are already implemented and can be used for easy troubleshooting
    def print_nice(self, vertex: Vertex, depth: int, found = set(), to_print = ""):
        """
        A way to print part of the graph for better troubleshooting. If your methods above
        works, this should print the traces from vertex. You do not need to change it
        """
        if depth <= 0:
            return
        f = found.copy()
        f.add(vertex)
        outgoing = self.outgoing(vertex)
        if len(outgoing) == 0:
            print(to_print + str(vertex))

        for edge in outgoing:
            trace = to_print + f"{vertex} - {edge.name}"
            if edge.head not in f:
                trace = trace + " -> "
                self.print_nice(edge.head, depth - 1, f, trace)
            else:
                print(trace +f" -> {edge.head}")


    def print_from_sources(self, depth: int):
        for s in self.source_vertices():
            self.print_nice(s, depth)





