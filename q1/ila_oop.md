# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation can be used by putting a product's data, such as its name, price, and stock, inside a Product class. The data can be protected from being changed directly by using methods such as update_stock() and change_price(). This keeps the product's information organized and helps prevent accidental or invalid changes.

### 2. Abstraction
Abstraction can be applied by provifing simple methods that hide the complicated details of how the inventory works. For example, a sell_product() method can reduce the product's stock without requiring the user to know how the stock is calculated internally. This makes the program easier to use and allows the internal implementation to be changed without affecting the rest of the system.

### 3. Inheritance
Inheritance can be used if the store has different types of products that share common properties and behaviors. For example, a FoodProduct and a NonFoodProduct class can inherit common properties such as name, price, and stock from a Product class. This reduces repeated code and makes it easier to add new product types.

### 4. Polymorphism
Polymorphism allows different product classes to use the same method in different ways. For example, both FoodProduct and NonFoodProduct could have a display_info() method, but each class could display information specific to its type. This makes the inventory system more flexible because the same method can work with different kinds of objects.

## Reflection
Among the four pillars of Object-Oriented Programming, I think encapsulation would be the most useful for improving the sari-sari store inventory system. It keeps each product's information and related methods together, making the program more organized. It also helps protect important data such as prices and stock quantities from being changed incorrectly. Overall, encapsulation would make the inventory system easier to maintain and manage.