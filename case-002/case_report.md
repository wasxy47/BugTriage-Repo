# Case 002 — Fix Report

## Bug summary
`apply_discount(price, percent)` in `shop_utils.py` returned the discount amount instead of the final price after the discount. For example, `apply_discount(200, 10)` returned `20.0` when the correct result is `180.0`.

## Root cause
The function correctly computed the discount (`price * percent / 100`) but returned that discount amount directly, instead of subtracting it from the original price.

## Fix (changed line)
In `apply_discount`, the return statement was changed from:

```python
    return discount
```

to:

```python
    return price - discount
```

Corrected function:

```python
def apply_discount(price, percent):
    discount = price * percent / 100
    return price - discount
```

## Before
Reproduction run against the buggy function: **0 passed, 5 failed** (exit code 1).

## After
Run: `python -m pytest test_shop_utils.py -v`

```
============================= test session starts =============================
platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\abdul\.switch\agents\localhost-65401\fixer-agent
plugins: anyio-4.13.0, langsmith-0.8.4, asyncio-1.3.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 5 items

test_shop_utils.py::test_apply_discount_200_10 PASSED                    [ 20%]
test_shop_utils.py::test_apply_discount_100_0 PASSED                     [ 40%]
test_shop_utils.py::test_apply_discount_100_100 PASSED                   [ 60%]
test_shop_utils.py::test_apply_discount_49_99_20 PASSED                  [ 80%]
test_shop_utils.py::test_apply_discount_10000_25 PASSED                  [100%]

============================== 5 passed in 0.06s ==============================
```

**Result: 5 passed, 0 failed.**

FIX VERIFIED
