<?php

require_once "Product.php";
require_once "Cart.php";
require_once "CartItem.php";

// Create product instances
$product1 = new Product(1, "iPhone 11", 2500, 10);
$product2 = new Product(2, "M2 SSD", 400, 10);
$product3 = new Product(3, "Samsung Galaxy S20", 3200, 10);

// Create a new cart
$cart = new Cart();

// Add products to the cart
$cartItem1 = $cart->addItem($product1, 1);
$cartItem2 = $cart->addItem($product2, 1);

// Display cart information
echo "Number of items in cart: " . PHP_EOL;
echo $cart->getTotalQuantity() . PHP_EOL; // This should print 2

echo "Total price of items in cart: " . PHP_EOL;
echo $cart->getTotalPrice() . PHP_EOL; // This should print 2900

// Increase quantity of the second item
$cart->updateItemQuantity($product2->getId(), 3);

// Display updated cart information
echo "Number of items in cart: " . PHP_EOL;
echo $cart->getTotalQuantity() . PHP_EOL; // This should print 4

echo "Total price of items in cart: " . PHP_EOL;
echo $cart->getTotalPrice() . PHP_EOL; // This should print 3700

// Remove a product from the cart
$cart->removeItem($product1->getId());

// Display final cart information
echo "Number of items in cart: " . PHP_EOL;
echo $cart->getTotalQuantity() . PHP_EOL; // This should print 3

echo "Total price of items in cart: " . PHP_EOL;
echo $cart->getTotalPrice() . PHP_EOL; // This should print 1200