# Assignment 1 Documentation

## Introduction

This documentation outlines the structure and functionality of a phone contract management system. It includes several classes, each designed to handle different types of contracts: `TermContract`, `MTMContract`, and `PrepaidContract`. These classes inherit from a base `Contract` class that encapsulates common functionalities and properties essential for managing various customer contracts.

## TermContract

### Description
The `TermContract` class is designed for fixed-term agreements, focusing on handling initial deposits and offering potential free minutes to the customers. It manages the lifecycle of a term contract, including billing for calls and the termination process.

### Methods
- `__init__`: Initializes a new term contract with a start date, end date, and term deposit.
- `new_month`: Updates contract status for a new month, adjusting billing as necessary.
- `bill_call`: Bills a particular call, deducting from free minutes or adding charges as applicable.
- `cancel_contract`: Calculates the total amount due upon contract cancellation, including handling the initial deposit.

### Attributes
- `start`: Start date of the contract.
- `enddate`: End date of the contract.
- `currentdate`: Date of the latest month added.
- `bill`: Bill for the last month.
- `freeminutes`: Number of free calling minutes.
- `termdeposit`: Initial deposit amount.

## MTMContract

### Description
The `MTMContract` subclass handles month-to-month agreements, providing flexibility with standard monthly charges and additional call fees. It inherits the `bill_call` and `cancel_contract` methods from the base `Contract` class.

### Methods
- `__init__`: Initializes a new month-to-month contract with a specified start date.
- `new_month`: Updates the contract for a new month, including billing details.

### Attributes
- `start`: Start date of the contract.
- `bill`: Bill for the last month.

## PrepaidContract

### Description
The `PrepaidContract` subclass caters to users preferring to pay upfront, monitoring and managing credit balances with a focus on prepayment. It includes functionalities for charging calls against the prepaid balance and handling the end of contract situations.

### Methods
- `__init__`: Sets up a new prepaid contract with a starting balance.
- `new_month`: Advances the contract to a new month, updating the billing and balance.
- `bill_call`: Deducts call charges from the prepaid balance and updates the bill.
- `cancel_contract`: Calculates the final balance, issuing refunds or billing for additional usage as needed.

### Attributes
- `start`: Start date of the contract.
- `bill`: Bill for the last month.
- `balance`: Current credit balance.

---

This documentation aims to provide a comprehensive overview of the system's functionality and its components, facilitating better understanding and management of phone contracts.
