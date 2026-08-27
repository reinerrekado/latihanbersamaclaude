# Python Exercise Materials

Demo code and exercises for Python classes, organized by topic. Each
folder is self-contained - clone/pull the repo, open a terminal in
the topic folder you want, and run any file with:

```bash
python3 <filename>.py
```

## Running Jupyter notebooks (`.ipynb`)

Some topics (e.g. [`data-visualization/`](data-visualization/)) use
Jupyter notebooks instead of plain `.py` files. To run one:

1. Create/activate the conda environment you want to use for the
   course, and install the packages that topic's demo/exercise files
   import (e.g. `pandas`, `matplotlib`, `seaborn`).
2. Install `ipykernel` in that environment - it's what lets
   Jupyter/VS Code actually execute code inside it:
   ```bash
   conda activate <your-env-name>
   conda install ipykernel   # or: pip install ipykernel
   ```
3. Open the `.ipynb` file in VS Code (or run `jupyter lab` /
   `jupyter notebook` from a terminal), then pick that environment
   from the **kernel picker** (top-right corner of the notebook in
   VS Code) before running any cells.
4. Run cells top to bottom - `Shift+Enter` for one cell at a time, or
   "Run All" to execute the whole notebook.

If your environment doesn't show up in the kernel picker, register it
explicitly:
```bash
python -m ipykernel install --user --name <your-env-name> --display-name "Python (<your-env-name>)"
```

## Topics

| Folder | Topic |
|---|---|
| [`conditional-and-loop-statements/`](conditional-and-loop-statements/) | `if`/`elif`/`else`, `for` and `while` loops, `break`/`continue`, iterables |
| [`collection-data-type/`](collection-data-type/) | `list`, `tuple`, `set`, `dict` - creation, methods, indexing/slicing, comprehension, set operations |
| [`python-function-and-file-handling/`](python-function-and-file-handling/) | Defining/calling functions, `return`/`lambda`, global vs. local scope, nested/callback/recursive functions, reading and writing files |
| [`object-oriented-programming/`](object-oriented-programming/) | Classes and objects, `__init__`/`self`, methods, inheritance |
| [`python-modular-programming/`](python-modular-programming/) | Splitting code into modules/packages, `if __name__ == "__main__"`, organizing a multi-file project |
| [`data-manipulation-pandas-numpy/`](data-manipulation-pandas-numpy/) | NumPy arrays (creation, indexing, broadcasting) and pandas `Series`/`DataFrame` (selection, manipulation, groupby, merge, pivot, I/O) |
| [`data-visualization/`](data-visualization/) | Matplotlib/Seaborn/pandas plotting - histograms, boxplots, line/scatter/bar plots, pie charts, correlation heatmaps |

More topics will be added as new folders alongside these.
