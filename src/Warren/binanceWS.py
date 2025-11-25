import websocket
import json
import time
import threading

latest_orderbook = None

#En gros ça va chercher bid et ask toutes les ms et calcul le mid price si jamais tu veux l'utiliser après

class Binance_OrderBook_WS:
    def __init__(self, symbol):
        self.symbol = symbol.lower()
        self.ws_url = f"wss://stream.binance.com:9443/ws/{self.symbol}@depth5@100ms"
        self.ws = None

    def on_message(self, ws, message):
        global latest_orderbook
        data = json.loads(message)
        latest_orderbook = data  

    def on_error(self, ws, error):
        print("WS Error:", error)

    def on_close(self, ws, close_status_code, close_msg):
        print("WebSocket Closed")

    def on_open(self, ws):
        print("WebSocket Connected")

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.ws_url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.ws.on_open = self.on_open
        self.ws.run_forever()


def loop_every_ms():
    while True:
        if latest_orderbook:
            bids = latest_orderbook["bids"]
            asks = latest_orderbook["asks"]
            mid_price = (float(bids[0][0]) + float(asks[0][0])) / 2
            print("Best Bid :", bids[0])
            print("Best Ask :", asks[0])
            print("Mid Price:", mid_price)

        time.sleep(0.001)


if __name__ == "__main__":
    ws_client = Binance_OrderBook_WS("btcusdt")
    t_ws = threading.Thread(target=ws_client.start)
    t_ws.daemon = True
    t_ws.start()

    # Boucle d'une ms
    loop_every_ms()




