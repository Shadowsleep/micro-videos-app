from ast import List
from typing import List
from __seedwork.domain.repositories import InMemorySearchableRepository
from category.domain.entities import Category
from category.domain.repositories import CategoryRepository


class CategoryInMemoryRepository(CategoryRepository, InMemorySearchableRepository):
    sortable_fields: List[str] = ['name', 'is_active', 'created_at']

    def _apply_filter(self, items: List[Category], filter_param: str = None) -> List[Category]:
        if filter_param:
            filter_obj = filter(
                lambda item: 
                    filter_param.lower() in item.name.lower()
                    or
                    filter_param.lower() == str(item.is_active).lower()
                    or
                    filter_param == str(item.created_at)
                ,items
            )
            return list(filter_obj)

        return items

    def _apply_sort(self, items: List[Category], sort: str | None, sort_dir: str | None) -> List[Category]:
        return super()._apply_sort(items, sort, sort_dir) if sort else super()._apply_sort(items, 'created_at', 'desc')
