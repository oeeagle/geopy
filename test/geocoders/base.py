
import unittest

from geopy.point import Point
from geopy.geocoders.base import Geocoder, DEFAULT_TIMEOUT


class GeocoderTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.geocoder = Geocoder()
        cls.coordinates = (40.74113, -73.989656)
        cls.coordinates_str = u"40.74113,-73.989656"
        cls.coordinates_address = u"175 5th Avenue, NYC, USA"

    def test_init(self):
        """
        Geocoder()
        """
        format_string = '%s Los Angeles, CA USA'
        scheme = 'http'
        timeout = DEFAULT_TIMEOUT + 1
        proxies = {'https': '192.0.2.0'}
        geocoder = Geocoder(
            format_string=format_string,
            scheme=scheme,
            timeout=timeout,
            proxies=proxies
        )
        for attr in ('format_string', 'scheme', 'timeout', 'proxies'):
            self.assertEqual(locals()[attr], getattr(geocoder, attr))

    def test_point_coercion_point(self):
        """
        Geocoder._coerce_point_to_string Point
        """
        self.assertEqual(
            self.geocoder._coerce_point_to_string(Point(*self.coordinates)),
            self.coordinates_str
        )

    def test_point_coercion_floats(self):
        """
        Geocoder._coerce_point_to_string tuple of coordinates
        """
        self.assertEqual(
            self.geocoder._coerce_point_to_string(self.coordinates),
            self.coordinates_str
        )

    def test_point_coercion_string(self):
        """
        Geocoder._coerce_point_to_string string of coordinates
        """
        self.assertEqual(
            self.geocoder._coerce_point_to_string(self.coordinates_str),
            self.coordinates_str
        )

    def test_point_coercion_address(self):
        """
        Geocoder._coerce_point_to_string address string
        """
        self.assertEqual(
            self.geocoder._coerce_point_to_string(self.coordinates_address),
            self.coordinates_address
        )
