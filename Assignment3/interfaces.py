from abc import ABC, abstractmethod
from models import PlayerProfile

class StatProvider(ABC):
    """Interface for fetching data from any source (API, CSV, Web Scraper)."""
    @abstractmethod
    def fetch_raw_stats(self, player_name: str) -> dict:
        pass

class DataConverter(ABC):
    """Interface for the Adapter pattern to standardize raw data."""
    @abstractmethod
    def standardize_data(self, raw_data: dict) -> PlayerProfile:
        pass

class PredictionStrategy(ABC):
    """Interface for the Strategy pattern to calculate projections."""
    @abstractmethod
    def calculate_projection(self, profile: PlayerProfile) -> float:
        pass