from abc import ABC
from __seedwork.domain.repositories import Repository
from category.domain.entities import Category


class CategoryRepository(Repository[Category],ABC):
    pass