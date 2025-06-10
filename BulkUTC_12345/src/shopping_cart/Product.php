<?php

class Product
{
    private int $id;
    private string $title;
    private float $price;
    private int $availableQuantity;

    public function __construct(int $id, string $title, float $price, int $availableQuantity)
    {
        $this->id = $id;
        $this->title = $title;
        $this->price = $price;
        $this->availableQuantity = $availableQuantity;
    }

    public function getId(): int
    {
        return $this->id;
    }

    public function getTitle(): string
    {
        return $this->title;
    }

    public function setTitle(string $title): void
    {
        $this->title = $title;
    }

    public function getPrice(): float
    {
        return $this->price;
    }

    public function setPrice(float $price): void
    {
        $this->price = $price;
    }

    public function getAvailableQuantity(): int
    {
        return $this->availableQuantity;
    }

    public function setAvailableQuantity(int $availableQuantity): void
    {
        $this->availableQuantity = $availableQuantity;
    }

    /**
     * Add Product $product into cart. If product already exists inside cart
     * it must update quantity.
     * This must create CartItem and return CartItem from method
     * Bonus: $quantity must not become more than whatever
     * is $availableQuantity of the Product
     *
     * @param Cart $cart
     * @param int $quantity
     * @return CartItem
     * @throws \InvalidArgumentException
     */
    public function addToCart(Cart $cart, int $quantity): CartItem
    {
        if ($quantity <= 0) {
            throw new \InvalidArgumentException("Quantity must be greater than zero.");
        }

        if ($quantity > $this->availableQuantity) {
            throw new \InvalidArgumentException("Requested quantity exceeds available quantity.");
        }

        $existingItem = $cart->findItem($this->id);

        if ($existingItem !== null) {
            $newQuantity = min($existingItem->getQuantity() + $quantity, $this->availableQuantity);
            $existingItem->setQuantity($newQuantity);
            return $existingItem;
        }

        $cartItem = new CartItem($this, $quantity);
        $cart->addItem($cartItem);
        return $cartItem;
    }

    /**
     * Remove product from cart
     *
     * @param Cart $cart
     * @return bool
     */
    public function removeFromCart(Cart $cart): bool
    {
        return $cart->removeItem($this->id);
    }
}