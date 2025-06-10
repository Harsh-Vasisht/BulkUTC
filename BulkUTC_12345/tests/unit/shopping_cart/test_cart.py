import unittest
from typing import List, Dict

# Mock implementations of external classes

class Product:
    def __init__(self, id: int, name: str, price: float, available_quantity: int):
        self._id = id
        self._name = name
        self._price = price
        self._available_quantity = available_quantity

    def getId(self) -> int:
        return self._id

    def getName(self) -> str:
        return self._name

    def getPrice(self) -> float:
        return self._price

    def getAvailableQuantity(self) -> int:
        return self._available_quantity

class CartItem:
    def __init__(self, product: Product, quantity: int):
        self._product = product
        self._quantity = quantity

    def getProduct(self) -> Product:
        return self._product

    def getQuantity(self) -> int:
        return self._quantity

    def setQuantity(self, quantity: int) -> None:
        self._quantity = quantity

# Implementation of the Cart class
class Cart:
    def __init__(self):
        self.items: List[CartItem] = []

    def getItems(self) -> List[CartItem]:
        return self.items

    def setItems(self, items: List[CartItem]) -> None:
        self.items = items

    def addProduct(self, product: Product, quantity: int) -> CartItem:
        for item in self.items:
            if item.getProduct().getId() == product.getId():
                new_quantity = min(item.getQuantity() + quantity, product.getAvailableQuantity())
                item.setQuantity(new_quantity)
                return item

        quantity = min(quantity, product.getAvailableQuantity())
        cart_item = CartItem(product, quantity)
        self.items.append(cart_item)
        return cart_item

    def removeProduct(self, product: Product) -> None:
        self.items = [item for item in self.items if item.getProduct().getId() != product.getId()]

    def getTotalQuantity(self) -> int:
        return sum(item.getQuantity() for item in self.items)

    def getTotalSum(self) -> float:
        return sum(item.getQuantity() * item.getProduct().getPrice() for item in self.items)

# Test class for Cart
class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.product1 = Product(1, "Product 1", 10.0, 5)
        self.product2 = Product(2, "Product 2", 15.0, 3)

    def test_add_new_product(self):
        cart_item = self.cart.addProduct(self.product1, 2)
        self.assertEqual(len(self.cart.getItems()), 1)
        self.assertEqual(cart_item.getProduct().getId(), 1)
        self.assertEqual(cart_item.getQuantity(), 2)

    def test_add_existing_product(self):
        self.cart.addProduct(self.product1, 2)
        cart_item = self.cart.addProduct(self.product1, 1)
        self.assertEqual(len(self.cart.getItems()), 1)
        self.assertEqual(cart_item.getQuantity(), 3)

    def test_add_product_exceed_available_quantity(self):
        cart_item = self.cart.addProduct(self.product1, 10)
        self.assertEqual(cart_item.getQuantity(), 5)

    def test_remove_product(self):
        self.cart.addProduct(self.product1, 2)
        self.cart.addProduct(self.product2, 1)
        self.cart.removeProduct(self.product1)
        self.assertEqual(len(self.cart.getItems()), 1)
        self.assertEqual(self.cart.getItems()[0].getProduct().getId(), 2)

    def test_get_total_quantity(self):
        self.cart.addProduct(self.product1, 2)
        self.cart.addProduct(self.product2, 1)
        self.assertEqual(self.cart.getTotalQuantity(), 3)

    def test_get_total_sum(self):
        self.cart.addProduct(self.product1, 2)
        self.cart.addProduct(self.product2, 1)
        self.assertEqual(self.cart.getTotalSum(), 35.0)

    def test_set_items(self):
        items = [
            CartItem(self.product1, 2),
            CartItem(self.product2, 1)
        ]
        self.cart.setItems(items)
        self.assertEqual(len(self.cart.getItems()), 2)
        self.assertEqual(self.cart.getTotalQuantity(), 3)
        self.assertEqual(self.cart.getTotalSum(), 35.0)

if __name__ == '__main__':
    unittest.main()