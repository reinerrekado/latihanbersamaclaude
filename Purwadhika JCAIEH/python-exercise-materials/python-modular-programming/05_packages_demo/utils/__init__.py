"""
__init__.py - the presence of this file tells Python "utils/ is a
PACKAGE, not just a folder". It also lets us expose specific
names, so callers can do `from utils import clean_text` instead of
the longer `from utils.text import clean_text`.
"""
from .data import load_data
from .text import clean_text
from .visualization import plot
