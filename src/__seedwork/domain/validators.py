from dataclasses import dataclass
from typing import Any

from __seedwork.domain.exceptions import ValidationException


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
