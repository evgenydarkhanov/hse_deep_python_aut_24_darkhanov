import weakref


class AnimalField:
    """ type for attributes """
    def __init__(self, value):
        self.value = value


class Tiger:
    """ default class """
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Lion:
    """ class with __slots__ """
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Bear:
    """ class with weakref.ref """
    def __init__(self, name, age):
        self.name = weakref.ref(name)
        self.age = weakref.ref(age)
