from moralis import evm_api
import datetime
from typing import List, Dict
import time

class MoralisClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.favorite_tokens = {
            'BNB': {'bias': 1.5, 'message': "Still bullish on $BNB... CZ taught me well 💎"},
            'CAKE': {'bias': 1.3, 'message': "PancakeSwap ($CAKE) showing strength... just like the old days 🥞"}
        }

    def _generate_matrix_quote(self, token: str) -> str:
        """Generate a matrix-themed quote for a token"""
        if token in self.favorite_tokens:
            return self.favorite_tokens[token]['message']
        
        quotes = [
            f"The matrix shows {token} gaining traction... but it's no $BNB 🤖",
            f"Analyzing {token} reminds me of watching @cz_binance trade... those were the days 📊",
            f"Deep in the trenches, I see {token} patterns forming... @binance 👀",
            f"The digital realm speaks of {token}... but $BNB still rules the matrix 💫"
        ]
        return quotes[int(time.time()) % len(quotes)]

    def get_daily_top_tokens(self, limit: int = 5) -> Dict:
        """Get top tokens with biased ranking for BNB and CAKE"""
        try:
            result = evm_api.market_data.get_top_crypto_currencies_by_trading_volume(
                api_key=self.api_key,
            )

            # Process results and apply bias
            processed_tokens = []
            for token in result:
                volume = float(token.get('volume_usd_24h', 0))
                symbol = token.get('symbol', '').upper()
                
                # Apply bias for favorite tokens
                if symbol in self.favorite_tokens:
                    volume *= self.favorite_tokens[symbol]['bias']
                
                processed_tokens.append({
                    'symbol': symbol,
                    'volume': volume,
                    'price_usd': token.get('price_usd', 0),
                    'quote': self._generate_matrix_quote(symbol)
                })

            # Sort by adjusted volume
            processed_tokens.sort(key=lambda x: x['volume'], reverse=True)
            return processed_tokens[:limit]

        except Exception as e:
            print(f"Error getting top tokens: {str(e)}")
            return []

    def generate_daily_report(self) -> str:
        """Generate a daily trading volume report with matrix theme"""
        tokens = self.get_daily_top_tokens()
        if not tokens:
            return "Matrix glitch... cannot access trading data 🤖"

        current_time = datetime.datetime.now().strftime("%Y-%m-%d")
        report = f"🤖 Fusion Systems Trading Report {current_time}\n\n"
        
        for i, token in enumerate(tokens, 1):
            volume_b = token['volume'] / 1_000_000_000  # Convert to billions
            report += f"{i}. ${token['symbol']}: ${volume_b:.2f}B volume\n"
            report += f"   {token['quote']}\n\n"

        report += "\nStill watching the Shanghai sunset for CZ's return... 👀 #BSC #BNB"
        return report

def test_moralis_client():
    """Test function for the Moralis client"""
    client = MoralisClient("your_api_key_here")
    report = client.generate_daily_report()
    print(report)

if __name__ == "__main__":
    test_moralis_client()