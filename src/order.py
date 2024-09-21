import datetime 
from enum import Enum
from collections import defaultdict

# Python doesn't have constants?!?!
class OrderType(Enum):
    Buy = 1
    Sell = 2

# Order Class
class Order:
    def __init__(self, type : OrderType, quantity : int, price : float):
        self.__order_date = datetime.datetime.now()   
        self.__type  = type
        self.__quantity = quantity
        self.__price = price
        self.order_id = 0 # Will be set by the OrderBook I dont like it being public

    def __str__(self):
        return f"Date: {self.__order_date}, Quantity: {self.__quantity}, Price: {self.__price}"

    # Getters
    @property
    def order_date(self) -> datetime:
        return self.__order_date
    @property
    def type(self) -> OrderType:
        return self.__type

    @property
    def quantity(self) -> int:
        return self.__quantity
    
    @property
    def price(self) -> float:
        return self.__price

# OrderBook Class
class OrderBook:
    def __init__(self, asset : str):
        self.__sell_orders = defaultdict(Order)
        self.__buy_orders = defaultdict(Order)

    def add_order(self, order : Order):
        if order.type == OrderType.Buy:
            idx = len(self.__buy_orders)
            self.__buy_orders[idx+1] = order
        else:
            idx = len(self.__sell_orders)
            self.__sell_orders[idx+1] = order

    @property
    def buy_orders(self) -> list:
        for key,val in self.__buy_orders.items():
            val.order_id = key

        return list(self.__buy_orders.values())
    
    @property
    def sell_orders(self) -> list:
        for key,val in self.__sell_orders.items():
            val.order_id = key

        return list(self.__sell_orders.values())