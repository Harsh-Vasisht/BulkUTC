<?php

class Cart
{
    /**
     * @var CartItem[]
     */
    private array $items = [];

    /**
     * Get all items in the cart
     *
     * @return CartItem[]
     */
    public function getItems(): array
    {
        return $this->items;
    }

    /**
     * Set the items in the cart
     *
     * @param CartItem[] $items
     */
    public function setItems(array $items): void
    {
        $this->items = $items;
    }

    /**
     * Add Product $product into cart. If product already exists inside cart
     * it must update quantity.
     * This must create CartItem and return CartItem from method
     * Bonus: $quantity must not become more than whatever
     * is $availableQuantity of the Product
     *
     * @param Product $product
     * @param int $quantity
     * @return CartItem
     */
    public function addProduct(Product $product, int $quantity): CartItem
    {
        foreach ($this->items as $item) {
            if ($item->getProduct()->getId() === $product->getId()) {
                $newQuantity = min($item->getQuantity() + $quantity, $product->getAvailableQuantity());
                $item->setQuantity($newQuantity);
                return $item;
            }
        }

        $quantity = min($quantity, $product->getAvailableQuantity());
        $cartItem = new CartItem($product, $quantity);
        $this->items[] = $cartItem;
        return $cartItem;
    }

    /**
     * Remove product from cart
     *
     * @param Product $product
     */
    public function removeProduct(Product $product): void
    {
        $this->items = array_filter($this->items, function($item) use ($product) {
            return $item->getProduct()->getId() !== $product->getId();
        });
    }

    /**
     * This returns total number of products added in cart
     *
     * @return int
     */
    public function getTotalQuantity(): int
    {
        return array_reduce($this->items, function($carry, $item) {
            return $carry + $item->getQuantity();
        }, 0);
    }

    /**
     * This returns total price of products added in cart
     *
     * @return float
     */
    public function getTotalSum(): float
    {
        return array_reduce($this->items, function($carry, $item) {
            return $carry + ($item->getQuantity() * $item->getProduct()->getPrice());
        }, 0.0);
    }
}