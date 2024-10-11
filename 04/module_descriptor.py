class Base:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype):
        if obj is None:
            return None
        return obj.__dict__[self.name]

    def __set__(self, obj, val):
        self.validate(val)
        obj.__dict__[self.name] = val

    def __delete__(self, obj):
        if obj is None:
            return
        del obj.__dict__[self.name]

    def validate(self, val):
        raise NotImplementedError("subclasses must implement this method")


class Integer(Base):
    def validate(self, val):
        if not isinstance(val, int):
            raise TypeError(f"{self.name} must be an Integer")


class String(Base):
    def validate(self, val):
        if not isinstance(val, str):
            raise TypeError(f"{self.name} must be a String")


class PositiveInteger(Integer):
    def validate(self, val):
        super().validate(val)
        if val <= 0:
            raise TypeError(f"{self.name} must be a PositiveInteger")


class Data:
    num = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self, num, name, price):
        self.num = num
        self.name = name
        self.price = price
