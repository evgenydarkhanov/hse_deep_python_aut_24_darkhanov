class CustomMeta(type):

    def __new__(mcs, name, bases, classdict):
        new_dict = {}
        for key, value in classdict.items():
            if key.startswith("__") and key.endswith("__"):
                new_dict[key] = value
            else:
                new_dict[f"custom_{key}"] = value

        new_dict["__setattr__"] = mcs.customize_attributes
        return super().__new__(mcs, name, bases, new_dict)

    @staticmethod
    def customize_attributes(obj, name, value):
        if name.startswith("__") and name.endswith("__"):
            obj.__dict__[name] = value
        else:
            obj.__dict__[f"custom_{name}"] = value
