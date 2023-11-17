from abc import ABC
import abc
from dataclasses import dataclass, field
from typing import Generic, List, TypeVar
from __seedwork.domain.entities import Entity
from __seedwork.domain.exceptions import NotFoundException

from __seedwork.domain.value_objects import UniqueEntityId

ET = TypeVar('ET', bound=Entity)


class Repository(Generic[ET], ABC):

    @abc.abstractmethod
    def insert(self, entity: ET) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_by_id(self, entity_id: str | UniqueEntityId) -> ET:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_all(self) -> List[ET]:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, entity: ET) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, entity_id: str | UniqueEntityId) -> None:
        raise NotImplementedError()

@dataclass(slots=True)
class InMemoryRepository(Repository[ET], ABC):
    items: List[ET] = field(default_factory=lambda:[])

    def insert(self, entity: ET) -> None:
        self.items.append(entity)

    def find_by_id(self, entity_id: str | UniqueEntityId) -> ET:
        id_str=str(entity_id)
        return self._get(id_str)

    def find_all(self) -> List[ET]:
        return self.items

    def update(self, entity: ET) -> None:
        entity=self._get(entity_id=entity.id)
        index = self.items.index(entity)
        self.items[index]=entity

    def delete(self, entity_id: str | UniqueEntityId) -> None:
        id_str=str(entity_id)
        entity=self._get(id_str)
        self.items.remove(entity)

    def _get(self, entity_id:str):
        try:
            entity=next(filter(lambda i: i.id==entity_id, self.items))
            if not entity:
                raise NotFoundException(f"Entity not found with id '{entity_id}'")
            return entity
        except:
             raise NotFoundException(f"Entity not found with id '{entity_id}'")