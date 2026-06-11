# Data Analyzer and Transformer Program

## Description

This Python program allows users to input numerical data and perform different operations such as:

* Data Summary
* Factorial Calculation using Recursion
* Data Filtering using Lambda Function
* Data Sorting
* Dataset Statistics using `*args` and `**kwargs`

---

## Features

### 1. Input Data

Store integer values in a 1D array.

### 2. Display Data Summary

Shows:

* Total Elements
* Minimum Value
* Maximum Value
* Sum
* Average

### 3. Calculate Factorial (Recursion)

Calculates factorial of a number using a recursive function.

### 4. Filter Data by Threshold (Lambda Function)

Displays values greater than or equal to the entered threshold.

### 5. Sort Data

Sort data in:

* Ascending Order
* Descending Order

### 6. Dataset Statistics

Displays:

* Minimum Value
* Maximum Value
* Sum
* Average

using a function that returns multiple values.

---

## Functions Used

### statistics(*args, **kwargs)

Calculates:

* Minimum value
* Maximum value
* Sum
* Average

Uses:

* `*args` for dataset values
* `**kwargs` for optional title

### fact(n)

Recursive function to calculate factorial.

---

## Python Concepts Used

* List
* Functions
* Docstrings
* Recursion
* Lambda Function
* Filter Function
* Built-in Functions
* *args
* **kwargs
* Return Multiple Values
* Conditional Statements
* Loops

---

## Documentation Used

### Docstrings

The program uses docstrings to describe functions, their parameters, return values, and usage examples.

Functions with docstrings:
- statistics(*args, **kwargs)
- fact(n)

---

## Methods and Functions NOT Used

### List Methods Not Used

* append()
* insert()
* extend()
* remove()
* pop()
* clear()
* copy()
* reverse()
* count()
* index()

### Built-in Functions Not Used

* map()
* enumerate()
* zip()
* any()
* all()

### String Methods Not Used

* replace()
* upper()
* lower()
* strip()
* splitlines()

### Collection Types Not Use

* Set
* Dictionary

---

## ▶️ How to Run

```bash
python Functional_Treat.py
```

## Example Input

10 20 30 40 50

## Example Output

Data Summary:

* Total elements: 5
* Minimum value: 10
* Maximum value: 50
* Sum of all values: 150
* Average value: 30.00

Dataset Statistics:

* Minimum value: 10
* Maximum value: 50
* Sum of all values: 150
* Average value: 30.00

Thank you for using the Data Analyzer and Transformer Program.
