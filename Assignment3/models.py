from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class PlayerProfile:
    """The standard data format used throughout the application."""
    name: str
    points_history: List[float]
    season_avg: float
    metadata: Dict = field(default_factory=dict)  # For extra info like Team or Position