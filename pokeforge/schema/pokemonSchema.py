from typing import Dict, Optional, List
from pydantic import BaseModel

class PokemonOut(BaseModel):
    name: str
    types: List[str] 
    baseStats: Optional[Dict[str, int]]
    tier: str

class PokemonIn(BaseModel):
    name: str
    types: List[str] 
    tier: str

class Pokemon:
    name: str 
    baseStats: dict[str, int] 

    def __init__(self, name: str, baseStats: dict[str, int]):
        self.name = name
        self.baseStats = baseStats