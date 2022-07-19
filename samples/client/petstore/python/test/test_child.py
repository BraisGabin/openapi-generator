# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import
import sys
import unittest

import petstore_api
try:
    from petstore_api.model import child_all_of
except ImportError:
    child_all_of = sys.modules[
        'petstore_api.model.child_all_of']
try:
    from petstore_api.model import parent
except ImportError:
    parent = sys.modules[
        'petstore_api.model.parent']
from petstore_api.model.child import Child


class TestChild(unittest.TestCase):
    """Child unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChild(self):
        """Test Child"""

        # make an instance of Child, a composed schema model
        radio_waves = True
        tele_vision = True
        inter_net = True
        child = Child(
            radio_waves=radio_waves,
            tele_vision=tele_vision,
            inter_net=inter_net
        )

        # check its properties
        self.assertEqual(child.radio_waves, radio_waves)
        self.assertEqual(child.tele_vision, tele_vision)
        self.assertEqual(child.inter_net, inter_net)
        # access them with keys
        self.assertEqual(child['radio_waves'], radio_waves)
        self.assertEqual(child['tele_vision'], tele_vision)
        self.assertEqual(child['inter_net'], inter_net)
        # access them with getattr
        self.assertEqual(getattr(child, 'radio_waves'), radio_waves)
        self.assertEqual(getattr(child, 'tele_vision'), tele_vision)
        self.assertEqual(getattr(child, 'inter_net'), inter_net)

        # check the model's to_dict result
        self.assertEqual(
            child.to_dict(),
            {
                'radio_waves': radio_waves,
                'tele_vision': tele_vision,
                'inter_net': inter_net,
            }
        )

        # with hasattr
        self.assertFalse(hasattr(child, 'invalid_variable'))

        # getting a value that doesn't exist raises an exception
        # with a key
        with self.assertRaises(petstore_api.ApiAttributeError):
            invalid_variable = child['invalid_variable']
        # with getattr
        self.assertEqual(getattr(child, 'invalid_variable', 'some value'), 'some value')

        with self.assertRaises(petstore_api.ApiAttributeError):
            invalid_variable = getattr(child, 'invalid_variable')

        # make sure that the ModelComposed class properties are correct
        # model.composed_schemas() stores the anyOf/allOf/oneOf info
        self.assertEqual(
            child._composed_schemas,
            {
                'anyOf': [],
                'allOf': [
                    child_all_of.ChildAllOf,
                    parent.Parent,
                ],
                'oneOf': [],
            }
        )
        # model._composed_instances is a list of the instances that were
        # made from the anyOf/allOf/OneOf classes in model._composed_schemas()
        for composed_instance in child._composed_instances:
            if composed_instance.__class__ == parent.Parent:
                parent_instance = composed_instance
            elif composed_instance.__class__ == child_all_of.ChildAllOf:
                child_allof_instance = composed_instance
        self.assertEqual(
            child._composed_instances,
            [child_allof_instance, parent_instance]
        )
        # model._var_name_to_model_instances maps the variable name to the
        # model instances which store that variable
        self.assertEqual(
            child._var_name_to_model_instances,
            {
                'radio_waves': [child, parent_instance],
                'tele_vision': [child, parent_instance],
                'inter_net': [child, child_allof_instance]
            }
        )
        # model._additional_properties_model_instances stores a list of
        # models which have the property additional_properties_type != None
        self.assertEqual(
            child._additional_properties_model_instances, [child]
        )

        # setting a value that doesn't exist works
        # with a key
        child['invalid_variable'] = 'a'
        assert child.invalid_variable == 'a'
        # with setattr
        setattr(child, 'invalid_variable', 'b')
        assert child.invalid_variable == 'b'


        # if we modify one of the properties owned by multiple
        # model_instances we get an exception when we try to access that
        # property because the retrieved values are not all the same
        child_allof_instance.inter_net = False
        with self.assertRaises(petstore_api.ApiValueError):
            inter_net = child.inter_net

        # including extra parameters works
        child = Child(
            radio_waves=radio_waves,
            tele_vision=tele_vision,
            inter_net=inter_net,
            unknown_property='some value')
        assert child.unknown_property == 'some value'

if __name__ == '__main__':
    unittest.main()
