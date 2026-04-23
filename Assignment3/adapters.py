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
        
class NBAApiAdapter(DataConverter):
    """Adapts the real NBA API dictionary into our standard PlayerProfile."""
    def standardize_data(self, raw_data: dict) -> PlayerProfile:
        return PlayerProfile(
            name=raw_data.get("full_name"),
            points_history=raw_data.get("points_list", []),
            season_avg=float(raw_data.get("season_avg", 0.0)),
            metadata={"data_source": raw_data.get("source")}
        )