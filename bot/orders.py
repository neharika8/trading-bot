import logging
from binance.exceptions import BinanceAPIException


class OrderManager:
    def __init__(self, client):
        self.client = client

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logging.info(
                f"Placing order: {symbol}, {side}, {order_type}, Qty={quantity}, Price={price}"
            )

            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            }

            if order_type == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"

            response = self.client.futures_create_order(**params)

            logging.info(f"Response: {response}")

            return response

        except BinanceAPIException as e:
            logging.error(f"Binance API Error: {e}")
            raise

        except Exception as e:
            logging.error(f"Unexpected Error: {e}")
            raise