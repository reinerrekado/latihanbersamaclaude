"""
DEMO 4: __name__ == "__main__"
=============================================================
Goal: see the problem (unwanted code running on import) and the
fix (the __name__ == "__main__" guard).

Run this file:
    python main.py
"""
if __name__ == "__main__":

    # -------------------------------------------------
    # 1. Importing calculator_no_guard.py runs its top-level code too!
    # -------------------------------------------------
    # print("Importing calculator_no_guard...")
    # import calculator_no_guard   # prints "result = 3" even though we
    #                               # only wanted the add() function!

    # print("-" * 40)

    # -------------------------------------------------
    # 2. Importing calculator.py (with the guard) stays silent
    # -------------------------------------------------
    print("Importing calculator (with the __name__ guard)...")
    print('__name__ variable inside main.py', __name__)
    import calculator            # nothing extra gets printed

    # We can still use its function normally:
    print("calculator.add(5, 7) =", calculator.add(5, 7))   # 12

    print("-" * 40)

    # -------------------------------------------------
    # 3. Why this matters
    # -------------------------------------------------
    # print("""
    # Why use __name__ == "__main__":
    #   - Prevent Unwanted Execution -> importing a module for its
    #     functions shouldn't also run its test/demo code.
    #   - Boost Code Reusability     -> one file can be BOTH a reusable
    #     module AND a standalone script.
    #   - Easy Quick Testing         -> put quick test code under the
    #     guard to try a module without affecting anyone who imports it.
    # """)

    # print('Try running "python calculator.py" directly - it prints')
    # print('result = 3, because THIS TIME __name__ really is "__main__".')
