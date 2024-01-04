from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from category.application.dto import CategoryOutput
from category.domain.repositories import CategoryRepository
from category.domain.entities import Category

@dataclass()
class CreateCategoryUseCase:

    category_repo = CategoryRepository

    def execute(self, input: 'Input') -> 'Output':
        category = Category(
            name=input.name,
            description=input.description,
            is_active=input.is_active
        )
        self.category_repo.insert(category)
        return self.Output(
            id=category.id,
            created_at=category.created_at,
            description=category.description,
            is_active=category.is_active,
            name=category.name
        )

    @dataclass(slots=True, frozen=True)
    class Input:
        name: str
        description: Optional[str] = None
        is_active: Optional[bool] = True

    @dataclass(slots=True, frozen=True)
    class Output(CategoryOutput):
        pass

@dataclass()
class GetCategoryUseCase:

    category_repo = CategoryRepository

    def execute(self, input: 'Input') -> 'Output':
        category = self.category_repo.find_by_id(input.id)
        return self.Output(
            id=category.id,
            created_at=category.created_at,
            description=category.description,
            is_active=category.is_active,
            name=category.name
        )

    @dataclass(slots=True, frozen=True)
    class Input:
        id: str

    @dataclass(slots=True, frozen=True)
    class Output(CategoryOutput):
        pass