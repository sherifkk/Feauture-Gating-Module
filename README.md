# Feauture Gating Module
Evaluates whether the user is allowed to access a particular feature or not depending on conditional expression evaluated against user attributes.

## This Feauture Gating Module support 
### User Atributes
* gender, age, salary, height, city, spends, latitude, longitude

### operators
* ||, &&, !, ==, !=, \>, \>=, <, <=, between, allof, noneof

### data types
* String, Boolean, Integer, Float

## Notes
* In Conditional Expression, between each and every operands and operators (including parantheses) white space is esential

## Testcases
* Run using pytest

    `pytest featureGating_test.py`
