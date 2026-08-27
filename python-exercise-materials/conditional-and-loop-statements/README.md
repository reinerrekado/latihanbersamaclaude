# Conditional and Loop Statements

Demo code and exercises to go with the *Conditional and Loop
Statements* class. Everything here is plain Python - clone/pull the
repo, open a terminal in this folder (`conditional-and-loop-statements/`),
and run any file with:

```bash
python3 <filename>.py
```

## Demo files

These walk through the same examples covered in class, in order.
Reading them again on your own is a good way to review - each one
has comments explaining *why* the code behaves the way it does, not
just *what* it does.

| File | Topic |
|---|---|
| `01_boolean_comparison_logical.py` | Comparison operators (`==`, `>`, `<=`, ...) and logical operators (`and`, `or`, `not`) |
| `02_conditional_statements.py` | `if`, `if-else`, `if-elif-else` |
| `03_indentation_error_LIVE_DEMO.py` | **Runs on purpose to show an `IndentationError`.** Read the comments inside for the fix |
| `04_nested_if.py` | Putting an `if` inside another `if` |
| `05_for_loop_and_range.py` | `for` loops and the `range()` function |
| `06_iterables.py` | Looping over strings, lists, tuples, dicts, sets, and ranges |
| `07_enumerate_vs_range.py` | Why `enumerate()` is usually better than `range(len(...))` |
| `08_while_loop.py` | `while` loops |
| `09_infinite_loop_LIVE_DEMO.py` | **Loops forever on purpose.** Press `Ctrl+C` in the terminal to stop it |
| `10_break_and_continue.py` | `break` (stop the loop) vs `continue` (skip to the next round) |
| `11_else_in_loop_BONUS.py` | Optional/bonus: `else` on a loop |

## Exercises

Open `exercise_skeleton.py`. It has 4 functions, one per exercise
from class, each with:

- a docstring describing what the function should do
- example inputs/outputs
- a hint
- `TODO` comments marking where your code goes

Work through them one at a time. At the bottom of the file, only one
function call is left uncommented at a time - run the file, solve
that exercise, then comment it out and uncomment the next one:

```python
if __name__ == "__main__":
    check_number_type()
    # average_until_zero()
    # largest_of_three()
    # sum_of_primes_in_range()
```

**Try to solve each one yourself before asking for help.** The hints
are there to point you in the right direction, not to hand you the
full solution - the exercises are 3-6 lines of code once you have
the right idea, so if you find yourself stuck for more than 10-15
minutes on the logic, re-read the matching demo file above, it
almost always has the pattern you need.

## Tips if you get stuck

- **`IndentationError` / `SyntaxError`** - see
  `03_indentation_error_LIVE_DEMO.py`. Python cares about consistent
  spacing (use 4 spaces per indent level, not tabs).
- **Program seems frozen / never stops** - you probably have an
  infinite loop. Press `Ctrl+C` to stop it, then check: does the
  variable in your `while` condition actually change inside the
  loop? See `09_infinite_loop_LIVE_DEMO.py`.
- **`ValueError: invalid literal for int()`** - you typed something
  that isn't a whole number where the code expected one (e.g. typing
  "abc" or leaving it blank).
