from interfaces import StatProvider
from typing import Dict

class MockProvider(StatProvider):
    """Returns fake data based on the player name provided."""
    def fetch_raw_stats(self, player_name: str) -> dict:
        # A simple dictionary acting as our 'database'
        database = {
            "LeBron James": {"last_5": [22, 18, 35, 12, 28], "avg": 24.5},
            "Luka Doncic": {"last_5": [32, 40, 28, 35, 33], "avg": 33.9},
            "Stephen Curry": {"last_5": [25, 30, 15, 42, 22], "avg": 26.4},
            "Kevin Durant": {"last_5": [28, 26, 30, 32, 24], "avg": 27.1}
        }

        player_data = database.get(player_name)
        
        if not player_data:
            # Fallback if player isn't in our mock list
            return {
                "full_name": player_name,
                "stats": {"last_5": [0, 0, 0, 0, 0], "avg": 0.0},
                "status": "Unknown"
            }

        return {
            "full_name": player_name,
            "stats": {
                "last_5": player_data["last_5"],
                "avg_points": player_data["avg"]
            },
            "status": "Active"
        }

class StatProviderFactory:
    """The Factory: Decides which provider to give the user."""
    @staticmethod
    def get_provider(source_type: str) -> StatProvider:
        providers = {
            "mock": MockProvider,
            # "nba": NBAApiProvider  <-- You would add this later
        }
        
        provider_class = providers.get(source_type.lower())
        if not provider_class:
            raise ValueError(f"Provider {source_type} not supported.")
        
        return provider_class()