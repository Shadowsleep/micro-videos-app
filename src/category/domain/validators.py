
from typing import Any
from __seedwork.domain.validators import DRFValidator
from rest_framework import serializers;


class CategoryRules(serializers.Serializer):
    name=serializers.CharField(max_length=255)
    description=serializers.CharField(required=False,allow_null=True)
    is_active=serializers.BooleanField(required=False)
    created_at=serializers.DateTimeField(required=False)

class CategoryValidator(DRFValidator):
    def Validate(self, data: Any) -> bool:
        rules= CategoryRules(data=data)
        return super().Validate(rules)
    
class CategoryValidatorFactory:
    @staticmethod
    def create():
        return CategoryValidator()