""" file:   unmarshal.py (pysiss.vocabulary)
    author: Jess Robertson
            CSIRO Minerals Resources Flagship
    date:   Monday 25 August, 2014

    description: Wrapper functionality for unmarshalling XML elements
"""

from .utilities import xml_namespaces
from .gml import unmarshallers as gml
from .gsml import unmarshallers as gsml
from .erml import unmarshallers as erml

UNMARSHALLERS = {}
UNMARSHALLERS.update(gml.UNMARSHALLERS)
UNMARSHALLERS.update(gsml.UNMARSHALLERS)
UNMARSHALLERS.update(erml.UNMARSHALLERS)


def unmarshal(elem):
    """ Unmarshal an lxml.etree.Element element

        If there is no unmarshalling function available, this just returns the
        lxml.etree element.
    """
    tag = xml_namespaces.shorten_namespace(elem.tag)
    unmarshal = UNMARSHALLERS.get(tag)
    if unmarshal:
        return unmarshal(elem)
    else:
        return None
