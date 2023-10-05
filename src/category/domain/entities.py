from datetime import datetime
from dataclasses import dataclass,field
from typing import Optional
from __seedwork.domain.entities import Entity

@dataclass(frozen=True,kw_only=True)
class Category (Entity):
   name:str
   description:Optional[str]=None
   is_active:Optional[bool]=True
   created_at: Optional[datetime]=field(default_factory=lambda: datetime.now())