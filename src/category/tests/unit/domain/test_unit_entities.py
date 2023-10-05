from dataclasses import FrozenInstanceError, is_dataclass
import unittest
from category.domain.entities import Category

class TestCategoryUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def test_is_imutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object=Category(name='teste')
            value_object.name='teste'
                        