from dataclasses import dataclass
import unittest
from __seedwork.domain.entities import Entity
from __seedwork.domain.exceptions import NotFoundException
from __seedwork.domain.repositories import InMemoryRepository, Repository
from __seedwork.domain.value_objects import UniqueEntityId


class TestRespository(unittest.TestCase):

    def test_throw_error_when_methods_not_implemented(self):
        with self.assertRaises(TypeError) as assert_error:
            Repository()
        self.assertEqual(assert_error.exception.args[0],
                         "Can't instantiate abstract class Repository with abstract methods delete, find_all, find_by_id, insert, update"
                         )


@dataclass(frozen=True, kw_only=True, slots=True)
class StubEntity(Entity):
    name: str
    price: float


class StubInMemoryRepository(InMemoryRepository[StubEntity]):
    pass


class TestInMemoryRepository(unittest.TestCase):
    repo: StubInMemoryRepository

    def setUp(self) -> None:
        self.repo = StubInMemoryRepository()

    def test_items_prop_is_empty_on_init(self):
        self.assertEqual(self.repo.items,[])

    def test_insert(self):
        entity=StubEntity(name='test',price=1.2)
        self.repo.insert(entity)
        self.assertEqual(self.repo.items[0],entity)

    def test_throw_exception_in_find_by_id(self):
        with self.assertRaises(NotFoundException) as error:
            self.repo.find_by_id('qualquer coisa')
        self.assertEqual(error.exception.args[0],"Entity not found with id 'qualquer coisa'")
        
        id=UniqueEntityId('d19d9c80-8580-11ee-b9d1-0242ac120002')

        with self.assertRaises(NotFoundException) as error:
            self.repo.find_by_id(id)
        self.assertEqual(error.exception.args[0],F"Entity not found with id '{id}'")
    
    def test_find_by_id(self):
        entity=StubEntity(name='test',price=1.2)
        self.repo.insert(entity)
       
        entity_found=self.repo.find_by_id(entity_id=entity.id)
        self.assertEqual(entity,entity_found)
       
        entity_found=self.repo.find_by_id(entity_id=entity.unique_entity_id)
        self.assertEqual(entity,entity_found)