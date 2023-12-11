from dataclasses import dataclass
from typing import List, Optional
import unittest
from __seedwork.domain.entities import Entity
from __seedwork.domain.exceptions import NotFoundException
from __seedwork.domain.repositories import ET, Filter, InMemoryRepository, Repository, SearchParams, SearchResult
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
        self.assertEqual(self.repo.items, [])

    def test_insert(self):
        entity = StubEntity(name='test', price=1.2)
        self.repo.insert(entity)
        self.assertEqual(self.repo.items[0], entity)

    def test_throw_exception_in_find_by_id(self):
        with self.assertRaises(NotFoundException) as error:
            self.repo.find_by_id('qualquer coisa')
        self.assertEqual(
            error.exception.args[0], "Entity not found with id 'qualquer coisa'")

        id = UniqueEntityId('d19d9c80-8580-11ee-b9d1-0242ac120002')

        with self.assertRaises(NotFoundException) as error:
            self.repo.find_by_id(id)
        self.assertEqual(
            error.exception.args[0], F"Entity not found with id '{id}'")

    def test_find_by_id(self):
        entity = StubEntity(name='test', price=1.2)
        self.repo.insert(entity)

        entity_found = self.repo.find_by_id(entity_id=entity.id)
        self.assertEqual(entity, entity_found)

        entity_found = self.repo.find_by_id(entity_id=entity.unique_entity_id)
        self.assertEqual(entity, entity_found)


class TestSearchParams(unittest.TestCase):
    def test_props_annotations(self):
        self.assertEqual(SearchParams.__annotations__,
                         {
                             'page': Optional[int],
                             'per_page': Optional[int],
                             'sort': Optional[str],
                             'sort_dir': Optional[str],
                             'filter': Optional[Filter]
                         })

    def test_page_prop(self):
        params = SearchParams()
        self.assertEqual(params.page, 1)

        arrange = [
            {'page': None, 'expected': 1},
            {'page': "None", 'expected': 1},
            {'page': "", 'expected': 1},
            {'page': {}, 'expected': 1},
            {'page': "5", 'expected': 5},
            {'page': 0, 'expected': 1},
            {'page': 1, 'expected': 1},
            {'page': False, 'expected': 1},
            {'page': [], 'expected': 1},
            {'page': 5.5, 'expected': 5},
            {'page': 2, 'expected': 2}
        ]

        for i in arrange:
            params = SearchParams(page=i['page'])
            self.assertEqual(params.page, i['expected'])

    def test_per_page_prop(self):
        params = SearchParams()
        self.assertEqual(params.page, 1)

        arrange = [
            {'per_page': None, 'expected': 15},
            {'per_page': "None", 'expected': 15},
            {'per_page': "", 'expected': 15},
            {'per_page': {}, 'expected': 15},
            {'per_page': "5", 'expected': 5},
            {'per_page': 0, 'expected': 15},
            {'per_page': 1, 'expected': 1},
            {'per_page': False, 'expected': 15},
            {'per_page': [], 'expected': 15},
            {'per_page': 5.5, 'expected': 5},
            {'per_page': 2, 'expected': 2}
        ]

        for i in arrange:
            print(i)
            params = SearchParams(per_page=i['per_page'])
            self.assertEqual(params.per_page, i['expected'])


class TestSearchResult(unittest.TestCase):
    
    def test_props_annotation(self):
        self.assertEqual(SearchResult.__annotations__, {
            'items': List[ET],
            'total': int,
            'current_page': int,
            'per_page': int,
            'last_page': int,
            'sort': Optional[str],
            'sort_dir': Optional[str],
            'filter': Optional[Filter] 
        })

    def test_constructor(self):
        entity=StubEntity(name='teste',price=5)
        result=SearchResult(
            items=[entity,entity],
            total=4,
            current_page=1,
            per_page=2,
        )
        self.assertEqual(result.to_dict(), {
            'items':[entity,entity],
            'total':4,
            'current_page':1,
            'per_page':2,
            'last_page':2,
            'sort':None,
            'sort_dir':None,
            'filter':None
        })

        result=SearchResult(
            items=[entity,entity],
            total=4,
            current_page=1,
            per_page=2,
            sort='name',
            sort_dir='asc'
        )
        self.assertEqual(result.to_dict(), {
            'items':[entity,entity],
            'total':4,
            'current_page':1,
            'per_page':2,
            'last_page':2,
            'sort':'name',
            'sort_dir':'asc',
            'filter':None
        })

    def test_when_per_page_is_greater_than_total(self):
        result=SearchResult(
            items=[],
            total=4,
            current_page=1,
            per_page=20,
        )
        self.assertEqual(result.last_page,1)
    
    def test_when_per_page_is_less_than_total_and_they_not_are_multiples(self):
        result=SearchResult(
            items=[],
            total=101,
            current_page=1,
            per_page=20,
        )
        self.assertEqual(result.last_page,6)
    