from typing import Dict, Optional
from pydantic import BaseModel

class Pokemon(BaseModel):
    name: str
    baseStats: Optional[Dict[str, int]]