import argparse
from colorama import init, Fore
from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logger

# Initialize colorama
init(autoreset=True)


def main():
    setup_logger()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", required=False, help="Price for LIMIT orders")

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price)

        if order_type == "LIMIT" and price is None:
            raise ValueError("Price is required for LIMIT orders")

        print(Fore.CYAN + "\nORDER REQUEST SUMMARY")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")

        if price:
            print(f"Price: {price}")

        client = BinanceClient().get_client()
        order_manager = OrderManager(client)

        response = order_manager.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print(Fore.YELLOW + "\nORDER RESPONSE")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")

        print(Fore.GREEN + "\nSUCCESS: Order placed successfully")

    except Exception as e:
        print(Fore.RED + f"\nFAILED: {str(e)}")


if __name__ == "__main__":
    main()