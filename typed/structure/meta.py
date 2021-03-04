from collections import OrderedDict
from inspect import Signature, Parameter

from .descriptor import Descriptor


class StructureMetaclass(type):
    """."""

    @classmethod
    def __prepare__(mcls, name, bases):
        """."""

        return OrderedDict()

    def __new__(mcls, class_name, bases, attrs):
        """."""

        fields = [key for key, value in attrs.items() if isinstance(value, Descriptor)]
        for name in fields:
            if not hasattr(attrs[name], "name"):
                attrs[name].name = name

        new_class = super(StructureMetaclass, mcls).__new__(mcls, class_name, bases, dict(attrs))

        new_signature = Signature([Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in fields])
        setattr(new_class, "__signature__", new_signature)

        return new_class
