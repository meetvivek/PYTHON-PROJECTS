# Coffee Machine

This project simulates the functionality of a coffee machine using object-oriented programming (OOP) principles in Python. It allows users to interactively select drinks from a menu, check the status of available resources, and make payments.

## Key Features
- Interactive menu selection: Users can choose from a variety of drinks available in the menu.
- Resource management: The coffee maker tracks the available resources (water, milk, coffee) and alerts when ingredients are insufficient.
- Payment processing: The money machine handles coin inputs, calculates change, and updates the machine's profit.
- Reporting: Users can request reports to view the current resources available in the coffee machine and the total profit generated.

## Python Concepts Used
- Object-Oriented Programming (OOP): The project is structured using classes and objects to model the coffee maker, money machine, and menu items.
- Encapsulation: Classes encapsulate related data and functions, promoting modularization and code organization.
- Abstraction: The underlying complexity of making drinks and handling payments is abstracted away, providing a simplified interface for users.
- Inheritance: The `MenuItem` class inherits properties and methods from the `Menu` class, demonstrating the concept of inheritance in OOP.

## Usage
1. Run the Coffee_Machine_Using_OPPs.py file in your Python environment.
2. Follow the prompts to select your drink from the available menu options.
3. If you want to turn off the coffee machine, type "off".
4. If you want to see the current resources and profit, type "report".
5. Follow the instructions to insert coins for payment.
6. Enjoy your drink once the payment is accepted and the coffee is prepared!

## Files
- **`coffee_machine_using_OOPs.py`**: Implements the main functionality of the coffee machine, including user interaction and control flow.
- **`coffee_maker.py`**: Defines the `CoffeeMaker` class, which models the coffee-making functionality and resource management.
- **`menu.py`**: Contains the `Menu` and `MenuItem` classes, representing the available menu items and their ingredients.
- **`money_machine.py`**: Implements the `MoneyMachine` class, which handles payment processing and maintains the machine's profit.

## Contributing
Contributions are welcome! If you'd like to improve the project, feel free to fork the repository and submit a pull request with your changes. Alternatively, you can open an issue to report any bugs or suggest new features. Your feedback is valuable and helps to make the project better for everyone. Thank you for contributing!

