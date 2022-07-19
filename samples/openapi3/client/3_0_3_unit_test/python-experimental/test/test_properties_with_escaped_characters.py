# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.model.properties_with_escaped_characters import PropertiesWithEscapedCharacters
from unit_test_api import configuration


class TestPropertiesWithEscapedCharacters(unittest.TestCase):
    """PropertiesWithEscapedCharacters unit test stubs"""
    _configuration = configuration.Configuration()

    def test_object_with_all_numbers_is_valid_passes(self):
        # object with all numbers is valid
        PropertiesWithEscapedCharacters._from_openapi_data(
            {
                "foo\nbar":
                    1,
                "foo\"bar":
                    1,
                "foo\\bar":
                    1,
                "foo\rbar":
                    1,
                "foo\tbar":
                    1,
                "foo\fbar":
                    1,
            },
            _configuration=self._configuration
        )

    def test_object_with_strings_is_invalid_fails(self):
        # object with strings is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            PropertiesWithEscapedCharacters._from_openapi_data(
                {
                    "foo\nbar":
                        "1",
                    "foo\"bar":
                        "1",
                    "foo\\bar":
                        "1",
                    "foo\rbar":
                        "1",
                    "foo\tbar":
                        "1",
                    "foo\fbar":
                        "1",
                },
                _configuration=self._configuration
            )


if __name__ == '__main__':
    unittest.main()
