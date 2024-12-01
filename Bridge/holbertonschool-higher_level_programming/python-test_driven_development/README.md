# Python Test-Driven Development - Holberton School

Welcome to the **Python Test-Driven Development** project repository! This project is part of the **Holberton School Higher-Level Programming** curriculum and focuses on writing robust and reliable Python code using Test-Driven Development (TDD). Each task emphasizes writing tests before implementing functionality, ensuring correctness and scalability.

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Test Suite](#test-suite)
- [Learning Objectives](#learning-objectives)

---

## Description

This project introduces the methodology of Test-Driven Development (TDD) in Python. The tasks involve:

- Writing tests using **doctest** and **unittest**.
- Validating input types and handling edge cases.
- Developing functions for mathematical operations, string manipulation, and matrix computations.
- Exploring Python's testing framework to ensure code quality.

Each implementation is complemented by thorough testing to demonstrate correctness under various scenarios.

---

## Project Structure

Here’s an overview of the files included in the `python-test_driven_development` directory:

| File                     | Description                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------- |
| `0-add_integer.py`       | Function that adds two integers, enforcing type validation.                           |
| `2-matrix_divided.py`    | Divides all elements of a matrix by a given number, with detailed validation.         |
| `3-say_my_name.py`       | Prints a formatted name from `first_name` and `last_name`.                            |
| `4-print_square.py`      | Prints a square of a given size using the `#` character.                              |
| `5-text_indentation.py`  | Formats a text by adding newlines after `.`, `?`, or `:`.                             |
| `6-max_integer_test.py`  | Unit tests for the `max_integer` function, covering edge cases and typical scenarios. |
| `100-matrix_mul.py`      | Performs matrix multiplication, validating dimensions and content.                    |
| `101-lazy_matrix_mul.py` | Efficiently performs matrix multiplication using the `numpy` library.                 |

---

## Test Suite

The project includes a comprehensive test suite to validate the functionality of each script. Tests are located in the `tests/` directory and utilize **doctest** and **unittest**.

### Test Files

| Test File                       | Description                                       |
| ------------------------------- | ------------------------------------------------- |
| `tests/0-add_integer.txt`       | Doctests for the `0-add_integer.py` script.       |
| `tests/2-matrix_divided.txt`    | Doctests for the `2-matrix_divided.py` script.    |
| `tests/3-say_my_name.txt`       | Doctests for the `3-say_my_name.py` script.       |
| `tests/4-print_square.txt`      | Doctests for the `4-print_square.py` script.      |
| `tests/5-text_indentation.txt`  | Doctests for the `5-text_indentation.py` script.  |
| `tests/6-max_integer_test.py`   | Unittest file for the `6-max_integer.py` script.  |
| `tests/100-matrix_mul.txt`      | Doctests for the `100-matrix_mul.py` script.      |
| `tests/101-lazy_matrix_mul.txt` | Doctests for the `101-lazy_matrix_mul.py` script. |

### Running Tests

You can run tests using the commands below:

#### Running Doctests

```bash
python3 -m doctest -v test.txt
```

#### Running Unittests

```bash
python3 -m unittest test.py
```

---

## Learning Objectives

- Understand and apply the principles of **Test-Driven Development**.
- Write effective **doctests** and **unittest** test cases.
- Validate function inputs rigorously to handle edge cases and invalid data.
- Gain familiarity with Python's testing tools and libraries.
- Develop reliable and reusable Python modules.

---
