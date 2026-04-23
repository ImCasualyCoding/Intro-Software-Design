from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
from interfaces import StatProvider

class MockProvider(StatProvider):
    """Provides static mock player statistics for offline testing."""
    def fetch_raw_stats(self, player_name: str) -> dict:
        return {
            "full_name": player_name or "Unknown Player",
            "stats": {
                "last_5_games": [12, 15, 14, 20, 18],
                "avg_points": 15.8
            },
            "status": "mocked"
        }

class NBAApiProvider(StatProvider):
    """Fetches real-time data from the official NBA API."""
    def fetch_raw_stats(self, player_name: str) -> dict:
        # Search for the player by name to get their ID
        search_results = players.find_players_by_full_name(player_name)
        if not search_results:
            raise ValueError(f"Player '{player_name}' not found in NBA database.")
        
        player_id = search_results[0]['id']
        
        # Fetch the game log for the current season
        log = playergamelog.PlayerGameLog(player_id=player_id)
        df = log.get_data_frames()[0]
        
        # We return a dictionary that includes the last 5 games' points
        # and the total season average calculated from the dataframe.
        return {
            "full_name": search_results[0]['full_name'],
            "points_list": df['PTS'].head(5).tolist(),
            "season_avg": df['PTS'].mean(),
            "source": "Official NBA API"
        }

class StatProviderFactory:
    @staticmethod
    def get_provider(source_type: str) -> StatProvider:
        providers = {
            "mock": MockProvider,
            "nba": NBAApiProvider
        }
        try:
            provider_cls = providers[source_type.lower()]
        except KeyError:
            raise ValueError(f"Unknown provider source: {source_type}")

        return provider_cls()
