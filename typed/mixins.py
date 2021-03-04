from .structure import Descriptor


class Positive(Descriptor):
    """."""
    
    def __set__(self, instance, value):
        """."""
        
        if value < 0:
            raise ValueError("Expected number to be greater than 0")
        
        super(Positive, self).__set__(instance, value)


class Negative(Descriptor):
    """."""

    def __set__(self, instance, value):
        """."""

        if value < 0:
            raise ValueError("Expected number to be less than 0")

        super(Negative, self).__set__(instance, value)
