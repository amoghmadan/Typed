class Descriptor(object):
    """."""

    def __init__(self, name=None):
        """."""

        self.name = name

    def __get__(self, instance, owner):
        """."""

        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        """."""

        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        """."""

        del instance.__dict__[self.name]


class Typed(Descriptor):
    """."""

    _type = object

    def __set__(self, instance, value):
        """."""

        if not isinstance(value, self.__class__._type):
            order = (self.__class__._type.__name__, self.name, value.__class__.__name__)
            raise TypeError("Expected type '%s' for parameter '%s' but got '%s'" % order)
        super(Typed, self).__set__(instance, value)
