
from abc import ABC
from dataclasses import dataclass, field, fields
import uuid
import json
from __seedwork.domain.exceptions import InvalidUuidException

@dataclass(frozen=True)
class ValueObject(ABC):
    def __str__(self) -> str:
        fields_name = [field.name for field in fields(self)]
        return str(getattr(self,fields_name[0])) \
            if len (fields_name)==1 \
            else \
                json.dumps({getattr(self,field_names) for field_names in fields_name})
    
@dataclass(frozen=True)
class UniqueEntityId(ValueObject):
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def __post_init__(self):
        id_value=str(self.id) if isinstance(self.id, uuid.UUID) else self.id
        object.__setattr__(self,'id',id_value)
        self.__validate()

    def __validate(self):
        try:
            uuid.UUID(self.id)
        except ValueError as ex:
            raise InvalidUuidException() from ex
    
    def __str__(self):
        return f"{self.id}"