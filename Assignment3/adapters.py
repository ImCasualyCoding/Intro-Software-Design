from interfaces import DataConverter
from models import PlayerProfile

class MockDataAdapter(DataConverter):
    """Adapts the MockProvider's dictionary into a PlayerProfile object."""
    def standardize_data(self, raw_data: dict) -> PlayerProfile:
        # We 'map' the messy dictionary keys to our clean object
        return PlayerProfile(
            name=raw_data.get("full_name", "Unknown"),
            points_history=raw_data.get("stats", {}).get("last_5_games", []),
            season_avg=raw_data.get("stats", {}).get("avg_points", 0.0),
            metadata={"status": raw_data.get("status")}
        )