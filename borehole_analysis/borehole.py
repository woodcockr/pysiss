#!/usr/bin/env python
"""Classes to represent a borehole.

Borehole has point features and domains on which properties are defined. A
property can be defined on multiple domains. Features and domains are
containers for the properties defined on them.

A Feature is analogous to a spatial point feature. It has a depth and
properties but it makes no sense to perform any interpolation on these.

An IntervalDomain is is a sequence of borehole segments each having a single
value for each property; this value is taken to be the same across the entire
length of the interval. IntervalDomains can be merged to form a new
IntervalDomain that has the intervals whose boundaries are the union of the
boundaries of the source IntervalDomains. An IntervalDomain can be
interpolated onto a SamplingDomain.

A SamplingDomain is a sequence of depths at which continuous properties are
sampled. Analogous to a coverage. One SamplingDomain can be interpolated onto
another.

Depths are measured in metres down-hole from the borehole collar; depth
sequences must be in monotonically increasing order.

Property units are expressed as Unified Code for Units of Measure (UCUM):
http://unitsofmeasure.org/ucum.html
"""

from borehole_analysis.domains import SamplingDomain, IntervalDomain, \
    Property
from borehole_analysis.wavelets import WaveletDomain

class Borehole(object):

    """ Borehole model.

        Properties:
            features - dict mapping feature name to Feature
            interval_domains - dict mapping interval domain name to
                IntervalDomain
            sampling_domains - dict mapping sampling domain name to
                SamplingDomain
            wavelet_domains - dict mapping wavelet domain names to
                WaveletDomain instances

        Arguments to constructor:
            name - identifier (string)
    """

    def __init__(self, name):
        self.name = name
        self.collar_location = None
        self.survey = None
        self.features = dict()
        self.interval_domains = dict()
        self.sampling_domains = dict()
        self.wavelet_domains = dict()

    def __repr__(self):
        """ String representation
        """
        info_str = (
            'Borehole {0}: {1}/{2} interval/sampling domains & {3} '
            + 'features'
            + '\nIDs: '
            + '\n     '.join(map(str, self.interval_domains.values()))
            + '\nSDs: '
            + '\n     '.join(map(str, self.sampling_domains.values()))
            + '\nWDs: '
            + '\n     '.join(map(str, self.wavelet_domains.values()))
        )
        return info_str.format(self.name,
            len(self.interval_domains), len(self.sampling_domains),
            len(self.features))

    def add_feature(self, name, depth):
        """Add and return a new Feature.

            Arguments:
                name - identifier (string)
                depth - down-hole depth in metres from collar (numeric)

            Returns: the new Feature instance
        """
        self.features[name] = Feature(name, depth)
        return self.features[name]

    def add_interval_domain(self, name, from_depth, to_depths):
        """ Add and return a new IntervalDomain

            Arguments:
                name - identifier (string)
                from_depths - interval start point down-hole depths in metres
                    from collar (any sequence, could be a list or numpy array)
                to_depths - interval end point down-hole depths in metres from
                    collar (any sequence, could be a list or numpy array)

            Returns: the new IntervalDomain instance.
        """
        self.interval_domains[name] = \
            IntervalDomain(name, from_depth, to_depths)
        return self.interval_domains[name]

    def add_sampling_domain(self, name, depths):
        """ Add and return a new SamplingDomain.

            Arguments:
                name - the name of the SamplingDomain
                depths - sampling point down-hole depths in metres from collar
                    (any sequence, could be a list or numpy array)

            Returns: the new SamplingDomain instance
        """
        self.sampling_domains[name] = SamplingDomain(name, depths)
        return self.sampling_domains[name]

    def add_wavelet_domain(self, name, sampling_domain,
        wavelet=None, wav_properties=None):
        """ Add and return a new WaveletDomain.
        """
        self.wavelet_domains[name] = WaveletDomain(name, sampling_domain,
            wavelet, wav_properties)
        return self.wavelet_domains[name]

    def desurvey(self, depths, crs):
        """ Return the depths as three-dimensional points in the given
            coordinate reference system
        """
        raise NotImplementedError

    def add_merged_interval_domain(self, name, source_name_a, source_name_b):
        """ Add a new merged interval domain from the two sources
        """
        raise NotImplementedError


class Feature(object):

    """A point feature with properties but no spatial extent.

        Properties:
            depth - down-hole depth in metres
            properties - dict mapping property name to Property

        Arguments to constructor:
            name - identifier (string)
            depth - the depth of the feature
    """

    def __init__(self, name, depth):
        self.name = name
        self.depth = depth
        self.properties = dict()

    def __repr__(self):
        """ String representation
        """
        info = 'Feature {0}: at {1} depth with {2} properties'
        return info.format(self.name, len(self.depth), len(self.properties))

    def add_property(self, property_type, values):
        """ Add a property to this feature.

            values - a single value or multiple values for a multivalued
                property
        """
        self.properties[property_type.name] = Property(property_type, values)

    def get_property_names(self):
        """ Return the names of the available properties for this feature
        """
        return self.properties.keys()

class CoordinateReferenceSystem(object):

    """System for describing a spatial location as a tuple of real numbers."""

    def  __init__(self):
        raise NotImplementedError


class Survey(object):

    """ The spatial shape of the borehole path in three dimensions from the
        collar.

        Used to convert a sequence of down-hole depths into a sequence of
        three-dimensional points in some coordinate reference system.
    """

    def __init__(self):
        raise NotImplementedError
