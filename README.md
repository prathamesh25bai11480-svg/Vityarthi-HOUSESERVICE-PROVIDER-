# House Service Application

A command-line interface (CLI) application developed in Python to demonstrate Object-Oriented Programming (OOP) principles by simulating a house service booking system. Users can view available services, add them to a cart, and calculate the total cost.

***

## Project Features

* **Service Listing:** Display a curated list of available services (e.g., Plumber, Electrician, Cleaner) with their prices.
* **Provider Ratings:** Each service is linked to a **Provider** with a specific rating.
* **Shopping Cart Logic:** Allows users to add multiple services to a temporary cart.
* **Checkout Calculation:** Calculates and displays the total aggregated cost of all services in the cart.
* **Simple Interface:** A clean, menu-driven console interface for ease of use.

***

## Project Structure and Design

The application is built around three core classes, demonstrating composition and encapsulation.

### 1. Class Diagram

The following diagram illustrates the structural relationships between the main components of the application:



### 2. Core Classes

| Class | Purpose | Key Attributes | Key Methods |
| :--- | :--- | :--- | :--- |
| **Provider** | Represents the individual service professional. | `name`, `rating` | `show()` (Displays provider details) |
| **Service** | Represents a bookable service item. | `name`, `price`, `provider` (Composition link to **Provider** object) | `show()` (Displays service and calls provider's `show()`) |
| **HouseServiceApp** | The main application class that manages state and logic. | `services` (List of available **Service** objects), `cart` (List of selected **Service** objects) | `show_services()`, `add_to_cart()`, `show_cart()`, `checkout()` |

***

## Getting Started

### Prerequisites

This project requires **Python 3.x**.

### Installation and Run

1.  **Save the Code:** Save the entire Python code provided (containing the `Provider`, `Service`, and `HouseServiceApp` classes) into a single file named `main.py`.

2.  **Run the Application:** Open your terminal or command prompt, navigate to the directory where you saved `main.py`, and run the following command:

    ```bash
    python main.py
    ```

***

## How to Use

Once the application is running, you will be presented with the main menu: