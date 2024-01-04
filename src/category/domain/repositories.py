from abc import ABC
from __seedwork.domain.repositories import SearchParams, SearchResult, SearchableRepository
from category.domain.entities import Category


# acesso privado para criar classes aninhadas
class _SearchParams(SearchParams):
    pass


class _SearchResult(SearchResult):
    pass


class CategoryRepository(SearchableRepository[Category, _SearchParams, _SearchResult], ABC):
    SearchParams = _SearchParams
    SearchResult = _SearchResult
