import json
from flask import Flask, render_template
from flask import request
from flask import jsonify
from src.order import Order, OrderType, OrderBook

app = Flask(__name__)

ord1 = Order(OrderType.Buy, 101, 250)
ord2 = Order(OrderType.Sell, 99, 200)
ord3 = Order(OrderType.Buy, 103, 300)
ord4 = Order(OrderType.Sell, 68, 190)

orderbook = OrderBook("APPLE")
orderbook.add_order(ord1)
orderbook.add_order(ord2)
orderbook.add_order(ord3)
orderbook.add_order(ord4)

def build_dict(orders : list):
    order_dict = {}
    for o in orders:
        order_dict[o.order_id] = {"ID": o.order_id, "Date": o.order_date, "Quantity": o.quantity, "Price": o.price}
    return order_dict

@app.route("/")
def home():
    return render_template("main.html", buy_orders=orderbook.buy_orders, sell_orders=orderbook.sell_orders)

@app.route("/buybook")
def buybook():
    buy_dict = build_dict(orderbook.buy_orders)
    return jsonify(buy_dict)

@app.route("/sellbook")
def sellbook():
    sell_dict = build_dict(orderbook.sell_orders) 
    return jsonify(sell_dict)

@app.route("/orderbook")
def market():
    buy_dict = build_dict(orderbook.buy_orders)
    sell_dict = build_dict(orderbook.sell_orders) 
    return jsonify({"Buy Orders": buy_dict, "Sell Orders": sell_dict})

@app.route("/add_order", methods=["POST"])
def add_order():
    data = request.get_json()
    order = Order(OrderType[data["order_type"]], data["quantity"], data["price"])
    orderbook.add_order(order)
    return jsonify({"buy_orders": build_dict(orderbook.buy_orders), "sell_orders": build_dict(orderbook.sell_orders)})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)