"""
Tagstore API Tag Model

This model is coded by hand.
"""
from collections import namedtuple
import pprint
import six


class Tag(object):
    """
    A Tag.
    Part of a Taxonomy.
    Can be applied to entities.
    """
    __slots__ = ('taxonomy_id', 'name', 'path', 'parent')  # Keep memory usage low

    # Metadata required by the rest of the API client code:
    openapi_types = {
        'taxonomy_id': 'str',
        'name': 'str',
        'path': 'str',
        'parent': 'str'
    }
    attribute_map = {
        'taxonomy_id': 'taxonomy_id',
        'name': 'name',
        'path': 'path',
        'parent': 'parent'
    }

    def __init__(self, taxonomy_id=None, name=None, path=None, parent=None):
        """
        Initialize this tag
        """
        self.taxonomy_id=taxonomy_id
        self.name=name
        self.path=path
        self.parent=parent

    @property
    def id(self):
        """
        Convenience method to get the taxonomy_id and name, which together
        uniquely identify this tag.
        """
        return {"taxonomy_id": self.taxonomy_id, "name": self.name}

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}
        # Exclude optional fields that aren't set:
        for key in self.openapi_types.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
