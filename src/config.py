from dataclasses import dataclass

@dataclass
class Config:
    H_INTERNAL: int = 0
    H_EXTERNAL: int = 0
    V_INTERNAL: int = 0
