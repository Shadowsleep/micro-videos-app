# from dataclasses import FrozenInstanceError, is_dataclass
# import unittest
# from unittest.mock import patch
# from category.domain.entities import Category

#class TestCategoryUnit(unittest.TestCase):
    # def test_if_is_a_dataclass(self):
    #     self.assertTrue(is_dataclass(Category))

    # def test_is_imutable(self):
    #     with self.assertRaises(FrozenInstanceError):
    #         value_object=Category(name='teste')
    #         value_object.name='teste'
                        
    # def test_update(self):
    #     with patch.object(Category,'validate') as mock_validate:
    #         value_object=Category(name='teste')
    #         value_object.update('teste1', 'teste2')
    #         self.assertEqual(value_object.name,'teste1')
    #         self.assertEqual(value_object.description,'teste2')
    #         mock_validate.assert_called_once()

    # def test_is_active(self):
    #     value_object=Category(name='teste',is_active=False)
    #     value_object.activate()
    #     self.assertTrue(value_object.is_active)
    
    # def test_is_deactive(self):
    #     value_object=Category(name='teste')
    #     value_object.deactivate()
    #     self.assertFalse(value_object.is_active)
    
