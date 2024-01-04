import unittest
from __seedwork.domain.exceptions import EntityValidationException,ValidationException
from category.domain.entities import Category

# class TestCategoryIntegration(unittest.TestCase):
#     def test_invalid_case_for_name_prop(self):
#         with self.assertRaises(EntityValidationException) as assert_error:
#             Category(name='')
#         self.assertEqual('Entity Validation Erros',assert_error.exception.args[0])
#         with self.assertRaises(EntityValidationException) as assert_error:
#             Category(name=None)
#         self.assertEqual('Entity Validation Erros',assert_error.exception.args[0])
#         with self.assertRaises(EntityValidationException) as assert_error:
#             Category(name='t' * 1001)
#         self.assertEqual('Entity Validation Erros',assert_error.exception.args[0])
    
#     def test_invalid_case_for_is_active_prop(self):
#         with self.assertRaises(EntityValidationException) as assert_error:
#             Category(name='teste',is_active=5)
#         self.assertEqual('Entity Validation Erros',assert_error.exception.args[0])




#     def test_invalid_case_for_name_prop(self):
#         with self.assertRaises(ValidationException) as assert_error:
#             Category(name='')
#         self.assertEqual('the name is required',assert_error.exception.args[0])
#         with self.assertRaises(ValidationException) as assert_error:
#             Category(name=None)
#         self.assertEqual('the name is required',assert_error.exception.args[0])
#         with self.assertRaises(ValidationException) as assert_error:
#             Category(name=5)
#         self.assertEqual('the name must be a string',assert_error.exception.args[0])
#         with self.assertRaises(ValidationException) as assert_error:
#             Category(name='t' * 1001)
#         self.assertEqual('the name must be less than 100 characters',assert_error.exception.args[0])
    
#     def test_invalid_case_for_description_prop(self):
#         with self.assertRaises(ValidationException) as assert_error:
#             Category(name='teste',description=5)
#         self.assertEqual('the description must be a string',assert_error.exception.args[0])
    
#     def test_invalid_case_for_is_active_prop(self):
#         with self.assertRaises(ValidationException) as assert_error:
#             Category(name='teste',is_active=5)
#         self.assertEqual('the is_active must be a boolean',assert_error.exception.args[0])