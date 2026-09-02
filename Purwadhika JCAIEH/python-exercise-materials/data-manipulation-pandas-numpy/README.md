# Python Data Manipulation with Pandas and NumPy

Demo code and exercises to go with the *Python Data Manipulation
with Pandas and NumPy* class. Everything here is plain Python -
clone/pull the repo, open a terminal in this folder
(`data-manipulation-pandas-numpy/`), and run any file with:

```bash
python3 <filename>.py
```

You'll need NumPy and pandas installed:

```bash
pip install numpy pandas
```

## Demo files

These walk through the same examples covered in class, in order.
Reading them again on your own is a good way to review - each one
has comments explaining *why* the code behaves the way it does, not
just *what* it does.

| File | Topic |
|---|---|
| `01_numpy_array_creation.py` | Why NumPy is faster than a list, creating arrays from lists, `arange`, `zeros`/`ones`/`eye`, `linspace`, `random.rand`/`randn`/`randint` |
| `02_numpy_indexing_slicing.py` | `shape`, `reshape`, `max`/`min`/`argmax`/`argmin`, indexing/slicing 1D and 2D arrays, views vs. `.copy()`, fancy indexing |
| `03_numpy_broadcasting_math.py` | Element-wise arithmetic, broadcasting rules, comparison operators as filters, `sqrt`/`exp`/`log`/`sin`, `where`/`transpose`/`flatten`/`concatenate` |
| `04_pandas_series.py` | What makes a `Series` different from an array (index labels), creating one from a list/array/dict |
| `05_pandas_dataframe_creation.py` | What a `DataFrame` is, creating one from a dict/list/array, `.shape`/`.columns`/`.head()`/`.tail()` |
| `06_pandas_selection_indexing.py` | Column selection, `.loc` (by label), `.iloc` (by position), conditional/boolean filtering |
| `07_pandas_dataframe_manipulation.py` | Adding/dropping rows and columns, `.insert()`, `reset_index()`/`set_index()`, multi-level index with `.xs()` |
| `08_pandas_sorting_summary_stats.py` | `sort_values()`/`sort_index()`, `.info()`/`.describe()`, `.mean()`/`.unique()`/`.value_counts()` |
| `09_pandas_missing_values_groupby.py` | `.isna()`, `.dropna()`/`.fillna()`, `.groupby()` with `.agg()` |
| `10_pandas_merge_join_concat.py` | `pd.merge()` (inner/outer/left/right), `.join()`, `pd.concat()` on both axes |
| `11_pandas_apply_pivot_io.py` | Arithmetic between columns, `.apply()`/lambda, `pivot_table()`, `to_csv()`/`read_csv()` |

## Exercises

Open `exercise_skeleton.py`. It has 6 functions, one per exercise -
2 using NumPy, 4 using pandas with `titanic_sample.csv` (a small
made-up dataset that sits in this same folder, modeled after the
real Titanic dataset). Each function has a comment describing what
it should do, but not exactly how - that's for you to work out using
what you saw in the demo files.

At the bottom of the file, only one function call is left
uncommented at a time - run the file, solve that exercise, then
comment it out and uncomment the next one:

```python
if __name__ == "__main__":
    border_array()
    # random_matrix_reverse()
    # filter_female_survivors()
    # age_group_avg_fare()
    # class_summary()
    # survival_by_class_and_gender()
```

**Try to solve each one yourself before asking for help.**

## Tips if you get stuck

- **`ValueError: cannot reshape array of size X into shape (r,c)`** -
  the rows x columns you picked don't multiply to the array's total
  element count. `reshape(rows, -1)` lets NumPy figure out the
  column count for you, as long as `rows` evenly divides the total.
  See `02_numpy_indexing_slicing.py`.
- **Editing a slice changed my original array too** - slicing an
  array returns a *view*, not a copy. Use `.copy()` if you need an
  independent copy. See `02_numpy_indexing_slicing.py`.
- **`TypeError: unsupported operand type(s)` on `df[(cond1) and cond2]`**
  - combining conditions on a DataFrame needs `&`/`|`, not
  `and`/`or`, and each condition needs its own parentheses:
  `df[(df['A'] > 0) & (df['B'] > 0)]`. See `06_pandas_selection_indexing.py`.
- **My `.drop()`/`.sort_values()`/`.set_index()` call didn't seem to
  do anything** - these return a *new* DataFrame by default instead
  of changing the original. Either reassign it
  (`df = df.drop(...)`) or pass `inplace=True`. See
  `07_pandas_dataframe_manipulation.py`.
- **`KeyError` from `.groupby()` or column selection** - column
  names are case-sensitive and must match exactly
  (`"Pclass"`, not `"pclass"`). Print `df.columns` if you're not
  sure what's available.
