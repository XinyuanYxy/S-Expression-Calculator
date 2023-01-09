# S-Expression-Calculator

> Evaluates simplified s-expressions from the command line using python. It supports functions including `add`, `multiply`.\
> Expression Syntax: `({function} {expression|integer} {expression|integer}) | {integer} `

## Example

```
% python3 calc.py "1"
1

% python3 calc.py "(multiply 1 1)"
1

% python3 calc.py "(multiply 3 (multiply (multiply 3 3) 3))"
81
```

## Getting Started

Open terminal, make sure you have `Python 3.9.13` installed or use a virtual envirnment. Your expression
should be a string. \
run `python3 calc.py expression`

## Testing Result

```
% python3 test_calc.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.123s

OK
```
