# Python Function and File Handling

Demo code and exercises to go with the *Python Function and File
Handling* class. Everything here is plain Python - clone/pull the
repo, open a terminal in this folder
(`python-function-and-file-handling/`), and run any file with:

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
| `01_defining_and_calling_functions.py` | `def`, calling a function, parameters vs arguments, default parameter values |
| `02_return_and_lambda.py` | The `return` statement, `lambda` functions, writing a clean function (type hints + docstring) |
| `03_namespace_and_scope.py` | Global vs local variables, the `global` keyword, `UnboundLocalError` |
| `04_nested_callback_recursive.py` | Nested functions, callback functions, recursive functions |
| `05_file_handling_basics.py` | Opening a file (`open()`), read/write/append modes, the `with` statement |

## Exercises

Open `exercise_skeleton.py`. It has 5 functions, one per exercise,
each with:

- a docstring describing what the function should do
- example inputs/outputs
- a hint
- `TODO` comments marking where your code goes

Work through them one at a time. At the bottom of the file, only one
function call is left uncommented at a time - run the file, solve
that exercise, then comment it out and uncomment the next one:

```python
if __name__ == "__main__":
    print(get_circle_area(radius=7))
    # print(get_circle_area(diameter=7))
    # print(convert_temperature(20, "C"))
    # print(convert_temperature(68, "F"))
    # print(analyze_number(7))
    # save_invoice()
    # read_prices_and_get_total()
```

**Try to solve each one yourself before asking for help.** The hints
are there to point you in the right direction, not to hand you the
full solution.

Exercises 4 and 5 work together: run `save_invoice()` first to create
`invoice.txt`, then run `read_prices_and_get_total()` to read it back
and apply a discount.

## Tips if you get stuck

- **My function returns `None`** - you probably forgot the `return`
  statement. `print()` only *displays* a value, it doesn't send it
  back to the caller. See `02_return_and_lambda.py`.
- **`UnboundLocalError: local variable '...' referenced before
  assignment`** - you tried to modify a global variable inside a
  function without declaring `global variable_name` first. See
  `03_namespace_and_scope.py`.
- **`NameError: name '...' is not defined`** - you're trying to use a
  variable outside the function it was created in. Local variables
  only exist inside their own function. See `03_namespace_and_scope.py`.
- **`FileNotFoundError`** - you opened a file with `"r"` mode before
  it existed. `"r"` requires the file to already exist; `"w"` and
  `"a"` will create it for you. See `05_file_handling_basics.py`.
- **My file's old content disappeared** - opening a file with `"w"`
  mode erases everything already in it before writing. Use `"a"` if
  you want to add to the existing content instead. See
  `05_file_handling_basics.py`.
