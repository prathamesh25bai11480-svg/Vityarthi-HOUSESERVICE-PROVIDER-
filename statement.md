# House Service Application - Project Statement

***

## 1. Problem Statement

In an increasingly digital world, homeowners and renters often face difficulty in quickly and reliably finding and hiring qualified service providers (like plumbers, electricians, and cleaners) and managing their service bookings. The lack of a centralized, easy-to-use platform leads to inefficient searching, unreliable provider selection, and a fragmented booking experience.

**The goal of this project is to create a simple, console-based application that centralizes service listings, allows users to view essential details (price, provider rating), select services, and calculate the total cost before checkout.**

***

## 2. Scope of the Project

The project is a foundational, **proof-of-concept** application demonstrating Object-Oriented Programming (OOP) principles in Python.

### In Scope:

* **Service Management:** Defining and storing a fixed list of available services, each linked to a specific provider.
* **User Interface:** A simple, text-based (console) menu for interacting with the application.
* **Transaction Management:** Functions to add selected services to a cart and calculate the total price for all items in the cart.
* **Data Structure:** Implementation using classes (`Provider`, `Service`, `HouseServiceApp`) to model real-world entities and their relationships.

### Out of Scope (Future Enhancements):

* Persistent data storage (e.g., using databases or files).
* User authentication or personalized accounts.
* Actual payment processing or real-time booking/scheduling.
* Complex filtering, sorting, or provider search functionality.

***

## 3. Target Users

The primary target users for this application, in a real-world context, would be:

* **Homeowners/Renters:** Individuals needing quick access to household maintenance and repair services.
* **Students/Developers:** Users studying OOP principles who want a clear, functional example of class design and object composition.

***

## 4. High-Level Features

The application offers the following core capabilities:

| Feature Category | Description |
| :--- | :--- |
| **View Services** | Display a numbered list of all available services, including the service name, price, and the provider's name and rating. |
| **Add to Cart** | Allow the user to select one or more services (by entering the corresponding number) and add them to a temporary shopping cart. |
| **View Cart** | Display all services currently held in the user's cart, showing the name, price, and provider details for each selected service. |
| **Checkout** | Calculate and display the final, cumulative cost (`Total = $...`) of all services currently in the cart. |
| **Exit** | Gracefully terminate the application loop. |