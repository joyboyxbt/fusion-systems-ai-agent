# test_moralis.py
from src.clients.moralis_client import MoralisClient
from dotenv import load_dotenv
import os

def test_moralis():
    try:
        # Load environment variables
        load_dotenv()
        
        # Get and print API key (first 10 chars)
        api_key = os.getenv('MORALIS_API_KEY')
        print(f"API Key found: {api_key[:10]}...")
        
        # Create client
        print("Creating Moralis client...")
        client = MoralisClient(api_key)
        
        # Generate report
        print("\nGenerating daily report...")
        report = client.generate_daily_report()
        print(report)
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    test_moralis()