from .meta import StructureMetaclass


class Structure(metaclass=StructureMetaclass):
    """."""

    def __init__(self, *args, **kwargs):
        """."""

        bound = getattr(self, "__signature__", None).bind(*args, **kwargs)
        for key, value in bound.arguments.items():
            setattr(self, key, value)
