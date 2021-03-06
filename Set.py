"""
Add ImmutableSet.  This is a nice example of a *protection proxy*.  An
immutable set is a wrapper around an invisible ListSet instance s.  It
protects s from alteration, and removes the services of add and
remove.  It is a proxy for s, because for the set operations (union,
intersection, members, ... ) that it is asked to do, it simply routes
to s.

"""

def new(obj, *args, **kw):      # Factory function
    return type(obj)(*args, **kw)

def iterator(s):
    for x in s.rep:
        yield x

class Set:

    def intersection(self, other): # An example of a template method
        s = new(self)           # Use factory function instead
        for x in self:          
            if x in other:      
                s.add(x)
        return s

    def __iter__(self):
        return iterator(self)

class DictSet(Set):

    def __init__(self, elements=[]):
        rep = self.rep = {}
        for element in elements:
            rep[element] = element

    def add(self, x):           
        self.rep[x] = x

class ListSet(Set):

    def __init__(self, elements=[]):
        rep = self.rep = []
        for element in elements:
            if element not in rep:
                rep.append(element)
    def members(self):
        return tuple(self.rep)

    def add(self, x):
        self.rep.append(x)

class ImmutableSet:

    def __iter__(self):
        return iter(self.members())

    def __init__(self, aList=[]):
        s = ListSet(aList)
        self.members = s.members
        self.intersection = s.intersection


i = ImmutableSet (range(5))
j = ImmutableSet ([3,4,5,6])
k = i.intersection(j)


