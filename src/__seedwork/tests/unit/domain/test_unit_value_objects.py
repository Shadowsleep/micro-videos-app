from abc import ABC
from dataclasses import FrozenInstanceError, is_dataclass
import unittest
from unittest.mock import patch
import uuid
from __seedwork.domain.exceptions import InvalidUuidException
from __seedwork.domain.value_objects import UniqueEntityId, ValueObject

class TestUniqueEntityIdUnit(unittest.TestCase):
    
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_throw_exception_when_uuid_is_invalid(self):
       with patch.object(
          UniqueEntityId,
          '_UniqueEntityId__validate',
          autospec=True,
          side_effect=UniqueEntityId._UniqueEntityId__validate
       )as mock_validate:
            with self.assertRaises(InvalidUuidException): 
                UniqueEntityId('fake id')
            mock_validate.assert_called_once()   
    
    def test_accept_uuid_passed_in_constructor(self):
        uuid_value=uuid.uuid4()
        value_object_string_passed=UniqueEntityId(str(uuid_value))
        value_object_uuid_passed=UniqueEntityId(str(uuid_value))
        self.assertEqual(value_object_string_passed.id,str(uuid_value))
        self.assertEqual(value_object_uuid_passed.id,str(uuid_value))

    def test_is_imutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object=UniqueEntityId()
            value_object.id='teste'

class TestValueObjectUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(ValueObject))
    
    def test_if_is_a_ABC(self):
        self.assertIsInstance(ValueObject(),ABC)