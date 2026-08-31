from dataclasses import asdict, dataclass
import json
from typing import List


@dataclass
class Buyer:
    username: str
    allowed_products: List[str]


@dataclass
class Merchant:
    username: str
    name: str
    product: str


@dataclass
class Order:
    merchant_username: str
    buyer_username: str
    price: float
    product: str
    description: str


class ApplicationException(Exception):
    pass

class EntityNotFound(ApplicationException):
    def __init__(self, entity: str, username: str) -> None:
        super().__init__(f"{entity} entity with username {username} not found")

class ProductNotAllowed(ApplicationException):
    def __init__(self, product: str, buyer_username: str) -> None:
        super().__init__(f"Product {product} is not allowed for buyer {buyer_username}")

class ProductMismatch(ApplicationException):
    def __init__(self, product: str, merchant_product: str) -> None:
        super().__init__(f"Product {product} does not match merchant's product {merchant_product}")


def read_json_file(file_path: str) -> List[dict]:
    with open(file_path, "r") as file:
        return json.load(file)
    
def write_json_file(file_path: str, data: List[dict]) -> None:
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4, separators=(',', ': '))


def find_merchant_by_username(username: str) -> Merchant:
    merchants = read_json_file("merchants.json")
    merchant_json = next(merchant for merchant in merchants if merchant["username"] == username)
    return Merchant(**merchant_json)

def find_buyer_by_username(username: str) -> Buyer:
    buyers = read_json_file("buyers.json")
    buyer_json = next(buyer for buyer in buyers if buyer["username"] == username)
    return Buyer(**buyer_json)


def get_merchant_by_username(username: str) -> Merchant:
    try:
        return find_merchant_by_username(username)
    except StopIteration:
        raise EntityNotFound("merchant", username)

def get_buyer_by_username(username: str) -> Buyer:
    try:
        return find_buyer_by_username(username)
    except StopIteration:
        raise EntityNotFound("buyer", username)

def validate_order(order: Order, merchant: Merchant, buyer: Buyer) -> None:

    if order.product != merchant.product:
        raise ProductMismatch(order.product, merchant.product)

    if order.product not in buyer.allowed_products:
        raise ProductNotAllowed(order.product, buyer.username)

    


def create_order(order: Order) -> None:

    merchant = get_merchant_by_username(order.merchant_username)
    buyer = get_buyer_by_username(order.buyer_username)

    validate_order(order, merchant, buyer)

    existing_orders = read_json_file("orders.json")
    existing_orders.append(asdict(order))

    write_json_file("orders.json", existing_orders)


if __name__ == '__main__':
    '''Order("eggo", "Eleven", "Eggo", 12, "some description")'''
    order = Order(merchant_username="eggo", 
                buyer_username="Eleven",
                price=12,
                product="Eggo",
                description="some description")
    create_order(order)
