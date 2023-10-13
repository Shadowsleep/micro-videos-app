
import unittest
from __seedwork.domain.exceptions import ValidationException

from __seedwork.domain.validators import ValidatorRules


class TestValidatorsRules(unittest.TestCase):
    def test_values_constructor(self):
        validators= ValidatorRules.values('some value','prop')
        self.assertIsInstance(validators,ValidatorRules)
        self.assertEqual(validators.prop,'prop')
        self.assertEqual(validators.value,'some value')

    def test_error_required_rules(self):
        with self.assertRaises(ValidationException) as assert_error:
            self.assertIsInstance(
                ValidatorRules.values(None,'prop').required(),
                ValidatorRules)
        self.assertEqual(assert_error.exception.args[0],'the prop is required')
        
        with self.assertRaises(ValidationException) as assert_error:
            self.assertIsInstance(
                ValidatorRules.values('','prop').required(),
                ValidatorRules)
        self.assertEqual(assert_error.exception.args[0],'the prop is required')
    
    def test_required_rules(self):
        validators= ValidatorRules.values('some value','prop').required()
        self.assertIsInstance(validators,ValidatorRules)
    
    def test_error_string_rules(self):
        with self.assertRaises(ValidationException) as assert_error:
            self.assertIsInstance(
                ValidatorRules.values(5,'prop').string(),
                ValidatorRules)
        self.assertEqual(assert_error.exception.args[0],'the prop must be a string')
        
        with self.assertRaises(ValidationException) as assert_error:
            self.assertIsInstance(
                ValidatorRules.values({},'prop').string(),
                ValidatorRules)
        self.assertEqual(assert_error.exception.args[0],'the prop must be a string')
    
    def test_string_rules(self):
        validators= ValidatorRules.values('some value','prop').string()
        self.assertIsInstance(validators,ValidatorRules)
        self.assertEqual(validators.prop,'prop')
        self.assertEqual(validators.value,'some value')

        validators= ValidatorRules.values(None,'prop').string()
        self.assertIsInstance(validators,ValidatorRules)

    def test_error_max_lenght_rules(self):
        with self.assertRaises(ValidationException) as assert_error:
            self.assertIsInstance(
                ValidatorRules.values('12345','prop').max_lenght(4),
                ValidatorRules)
        self.assertEqual(assert_error.exception.args[0],'the prop must be less than 4 characters')
        
    
    def test_max_lenght_rules(self):
        validators= ValidatorRules.values('12345','prop').max_lenght(5)
        self.assertIsInstance(validators,ValidatorRules)

    def test_error_boolean_rules(self):
        with self.assertRaises(ValidationException) as assert_error:
            self.assertIsInstance(
                ValidatorRules.values(5,'prop').boolean(),
                ValidatorRules)
        self.assertEqual(assert_error.exception.args[0],'the prop must be a boolean')
        
        with self.assertRaises(ValidationException) as assert_error:
            self.assertIsInstance(
                ValidatorRules.values({},'prop').boolean(),
                ValidatorRules)
        self.assertEqual(assert_error.exception.args[0],'the prop must be a boolean')
    
    def test_boolean_rules(self):
        validators= ValidatorRules.values(True, 'prop').boolean()
        self.assertIsInstance(validators,ValidatorRules)

        validators= ValidatorRules.values(None,'prop').boolean()
        self.assertIsInstance(validators,ValidatorRules)

    