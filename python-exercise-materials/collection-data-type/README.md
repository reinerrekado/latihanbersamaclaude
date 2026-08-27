# Python Collection Data Types

Demo code and exercises to go with the *Python Collection Data
Types* class. Everything here is plain Python - clone/pull the
repo, open a terminal in this folder (`collection-data-type/`),
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
| `01_python_list_basics.py` | Creating a `list`, indexing basics, empty lists, nested lists |
| `02_python_list_methods.py` | List methods (`append`, `insert`, `pop`, `remove`, `clear`, `copy`, `extend`) and `len`/`sorted` |
| `03_list_comprehension.py` | Building a new list with a for loop vs. list comprehension |
| `04_python_tuple.py` | Creating a `tuple`, why tuples are immutable, nested tuples |
| `05_tuple_methods.py` | Tuple methods (`.index()`, `.count()`) and `len` |
| `06_indexing_and_slicing.py` | Indexing (`[i]`) and slicing (`[start:stop:step]`) for lists and tuples |
| `07_python_set.py` | Creating a `set`, removing duplicates, why sets have no index |
| `08_set_methods.py` | Set methods (`add`, `update`, `remove`, `discard`, `pop`, `clear`, `copy`) |
| `09_set_operations.py` | `union`, `intersection`, `difference`, `symmetric_difference`, subset/superset checks |
| `10_python_dictionary.py` | Creating a `dict`, key-value pairs, unique keys vs. repeatable values |
| `11_dictionary_methods.py` | Dictionary methods (`update`, `setdefault`, `pop`, `popitem`, `get`, `keys`, `values`, `items`) |
| `12_dictionary_access_update.py` | Reading values safely with `[]` vs `.get()`, and updating/adding values |

## Exercises

Open `exercise_skeleton.py`. It has 4 functions, one per exercise,
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
    unique_attendance()
    # student_lookup()
    # filter_fruits()
    # course_enrollment()
```

**Try to solve each one yourself before asking for help.** The hints
are there to point you in the right direction, not to hand you the
full solution.

## Tips if you get stuck

- **`TypeError: 'tuple' object does not support item assignment`** -
  tuples are read-only. If you need to change the data, use a list
  instead. See `04_python_tuple.py`.
- **`KeyError: '...'`** - you tried to access a dictionary key that
  doesn't exist with `dictionary["key"]`. Use
  `dictionary.get("key", default_value)` instead if the key might be
  missing. See `12_dictionary_access_update.py`.
- **A set prints in a different order than you typed it, or the
  order changes between runs** - that's expected. Sets are
  unordered, so never rely on set order. See `07_python_set.py`.
- **`{}` isn't behaving like an empty set** - `{}` is an empty
  `dict`, not an empty `set`. Use `set()` instead. See
  `07_python_set.py`.
