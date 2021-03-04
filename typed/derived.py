from .primitive import Integer, Float
from .mixins import Positive, Negative


class PositiveInteger(Integer, Positive):
    """."""

    pass


class NegativeInteger(Integer, Negative):
    """."""

    pass


class PositiveFloat(Float, Positive):
    """."""

    pass


class NegativeFloat(Float, Positive):
    """."""

    pass
