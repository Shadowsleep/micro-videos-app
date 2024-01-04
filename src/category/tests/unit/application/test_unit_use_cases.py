
import unittest
from unittest.mock import patch

from category.application.use_cases import CreateCategoryUseCase, GetCategoryUseCase
from category.domain.entities import Category
from category.infra.repositories import CategoryInMemoryRepository


class TestCreateCategoryUseCaseUnit(unittest.TestCase):

    use_case: CreateCategoryUseCase
    category_repo: CategoryInMemoryRepository

    def setUp(self) -> None:
        self.category_repo = CategoryInMemoryRepository()
        self.use_case = CreateCategoryUseCase()

    def test_execute(self):
        self.use_case.category_repo=self.category_repo
        with patch.object(self.category_repo, 'insert', wraps=self.category_repo.insert) as spy_insert:
            input_params = self.use_case.Input(name='Movie')
            output = self.use_case.execute(input_params)
            spy_insert.assert_called_once()
            self.assertEqual(output, self.use_case.Output(
                id=self.category_repo.items[0].id,
                description=self.category_repo.items[0].description,
                name=self.category_repo.items[0].name,
                is_active=self.category_repo.items[0].is_active,
                created_at=self.category_repo.items[0].created_at
            ))


class TestGetCategoryUseCaseUnit(unittest.TestCase):

    use_case: GetCategoryUseCase
    category_repo: CategoryInMemoryRepository

    def setUp(self) -> None:
        self.category_repo = CategoryInMemoryRepository()
        self.use_case = GetCategoryUseCase()

    def test_execute(self):
        category = Category(name='Movie')
        self.category_repo.items = [category]
        self.use_case.category_repo=self.category_repo

        with patch.object(self.category_repo, 'find_by_id', wraps=self.category_repo.find_by_id) as spy_insert:
            input_params = self.use_case.Input(category.id)
            output = self.use_case.execute(input_params)
            spy_insert.assert_called_once()
            self.assertEqual(output, self.use_case.Output(
             id=self.category_repo.items[0].id,
                description=self.category_repo.items[0].description,
                name=self.category_repo.items[0].name,
                is_active=self.category_repo.items[0].is_active,
                created_at=self.category_repo.items[0].created_at
            ))
