from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, Generic, List, TypeVar
from django.conf import settings
from rest_framework.serializers import Serializer
from __seedwork.domain.exceptions import ValidationException

if not settings.configured:
    settings.configure(USE_I18N=False)

@dataclass(frozen=True, slots=True)
class ValidatorRules:
    value: Any
    prop: str

    @staticmethod
    def values(value:Any, prop:str):
        return ValidatorRules(value=value,prop=prop)
    
    def required(self) -> 'ValidatorRules':
        if self.value is None or self.value== '':
            raise ValidationException(f'the {self.prop} is required')
        return self    

    def string(self) -> 'ValidatorRules':
        if self.value is not None and not isinstance(self.value,str):
            raise ValidationException(f'the {self.prop} must be a string')
        return self
    
    def max_lenght(self,max_lenght:int) -> 'ValidatorRules':
        if self.value is not None and len(self.value) > max_lenght:
            raise ValidationException(f'the {self.prop} must be less than {max_lenght} characters')
        return self
    
    def boolean(self) ->'ValidatorRules':
        if self.value is not None and self.value is not True and self.value is not False:
            raise ValidationException(f'the {self.prop} must be a boolean')
        return self
    

PropsValidated=TypeVar('PropsValidated')
ErrosFields=Dict[str,List[str]]

@dataclass(slots=True)
class ValidatorFieldsAbc(ABC,Generic[PropsValidated]):
    errors:ErrosFields
    validated_data: PropsValidated

    @abstractmethod
    def Validate(self, data:Any) -> bool:
        raise NotImplementedError()
    
class DRFValidator(ValidatorFieldsAbc[PropsValidated]):
    def Validate(self, data: Serializer) -> bool:
        serializer=data
        is_valid=serializer.is_valid()

        if not is_valid:
            self.errors={
                field: [str(_error) for _error in _errors]
                for field,_errors in serializer.errors.items()
            }
          
            return False
        else:
            self.validated_data=serializer.validated_data
            return True
