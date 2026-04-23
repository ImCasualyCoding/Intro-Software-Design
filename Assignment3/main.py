from providers import StatProviderFactory
from adapters import MockDataAdapter
from strategies import SeasonAverageStrategy, RecentTrendStrategy, WeightedRecentStrategy

def run_analysis(player_name: str, source: str):
    # 1. CREATIONAL: Use Factory to get a provider
    factory = StatProviderFactory()
    provider = factory.get_provider(source)
    
    # 2. DATA FETCHING: Get the messy raw data
    raw_data = provider.fetch_raw_stats(player_name)
    
    # 3. STRUCTURAL: Use Adapter to clean the data
    adapter = MockDataAdapter()
    profile = adapter.standardize_data(raw_data)
    
    # 4. BEHAVIORAL: Apply different Strategies
    strategies = [
        SeasonAverageStrategy(),
        RecentTrendStrategy(),
        WeightedRecentStrategy()
    ]
    
    print(f"--- Analysis for {profile.name} ---")
    print(f"Season Avg: {profile.season_avg}")
    print(f"Recent Games: {profile.points_history}")
    print("-" * 30)
    
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
            # We still use our Factory and Strategy patterns exactly the same way!
            run_analysis(player_query, "mock")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()