# Case 003 — Fix Report

## Bug summary
`average_item_price(prices)` in `cart_utils.py` crashed with `ZeroDivisionError: division by zero` when the cart was empty (`prices == []`), e.g. when a user opened the cart after removing all items.

## Root cause
The function summed the list and then divided by `len(prices)`. For an empty list `len(prices)` is `0`, so the final `return total / len(prices)` raised `ZeroDivisionError` instead of returning a value.

## Fix
Added an empty-list guard at the top of `average_item_price`, returning `0.0` before the division. The summing loop and the `return total / len(prices)` line are unchanged.

Corrected function:

```python
def average_item_price(prices):
    if not prices:
        return 0.0
    total = 0
    for p in prices:
        total = total + p
    return total / len(prices)
```

## Before
Reproduction run against the buggy function: **3 passed, 1 failed** (exit code 1). The failing case was `average_item_price([])`, which raised `ZeroDivisionError: division by zero` at `cart_utils.py:5`.

## After
Run: `python -m pytest test_cart_utils.py -v`

```
============================= test session starts =============================
platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\abdul\.switch\agents\localhost-65401\fixer-agent
plugins: anyio-4.13.0, langsmith-0.8.4, asyncio-1.3.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 4 items

test_cart_utils.py::test_average_100_200_300 PASSED                      [ 25%]
test_cart_utils.py::test_average_single_item PASSED                      [ 50%]
test_cart_utils.py::test_average_10_20 PASSED                            [ 75%]
test_cart_utils.py::test_average_empty_list PASSED                       [100%]

============================== 4 passed in 0.04s ==============================
```

**Result: 4 passed, 0 failed.**

FIX VERIFIED
