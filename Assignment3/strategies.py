from interfaces import PredictionStrategy
from models import PlayerProfile

class SeasonAverageStrategy(PredictionStrategy):
    """Predicts performance based strictly on the season average."""
    def calculate_projection(self, profile: PlayerProfile) -> float:
        return profile.season_avg

class RecentTrendStrategy(PredictionStrategy):
    """Predicts performance based on the average of the last 5 games."""
    def calculate_projection(self, profile: PlayerProfile) -> float:
        if not profile.points_history:
            return profile.season_avg
        
        return sum(profile.points_history) / len(profile.points_history)

class WeightedRecentStrategy(PredictionStrategy):
    """
    Advanced Strategy: Gives 70% weight to recent games 
    and 30% to the season average.
    """
    def calculate_projection(self, profile: PlayerProfile) -> float:
        recent_avg = sum(profile.points_history) / len(profile.points_history)
        # Weighted calculation
        projection = (recent_avg * 0.7) + (profile.season_avg * 0.3)
        return round(projection, 2)