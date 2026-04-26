from providers import StatProviderFactory
from adapters import MockDataAdapter, NBAApiAdapter
from strategies import SeasonAverageStrategy, RecentTrendStrategy, WeightedRecentStrategy

def run_analysis(player_name: str, source: str):
    provider = StatProviderFactory.get_provider(source)
    
    if source == "nba":
        adapter = NBAApiAdapter()
    else:
        adapter = MockDataAdapter()
    
    raw_data = provider.fetch_raw_stats(player_name)
    profile = adapter.standardize_data(raw_data)
   
    strategies = [
        SeasonAverageStrategy(),
        RecentTrendStrategy(),
        WeightedRecentStrategy()
    ]
    
    print(f"\n--- Results for {profile.name} ---")
    for strategy in strategies:
        projection = strategy.calculate_projection(profile)
        print(f"{strategy.__class__.__name__}: {projection}")

def main():
    print("=== Sports Prop Tracker (SOLID Edition) ===")
    
    while True:
        player_query = input("\nEnter player name (or 'exit' to quit): ").strip()
        
        if player_query.lower() == 'exit':
            break
            
        try:
            
            run_analysis(player_query, "nba")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()