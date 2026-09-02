# Text Preprocessing

Demo notebooks and exercises to go with the *Text Preprocessing* class
(Modul 2). Everything here runs in Jupyter - clone/pull the repo, open
a terminal in this folder (`text-preprocessing/`), and launch:

```bash
jupyter notebook
```

You'll need pandas and nltk installed:

```bash
pip install pandas nltk
```

The demo/exercise notebooks download the small nltk corpora they need
(`punkt`, `stopwords`, `wordnet`, `omw-1.4`) automatically the first
time they run - you'll need an internet connection for that first run.

## Demo notebooks

These walk through the same examples covered in class, in order.
Reading them again on your own is a good way to review - each one has
markdown notes explaining *why* the code behaves the way it does, not
just *what* it does.

| File | Topic |
|---|---|
| `01_case_normalization.ipynb` | Lowercasing/uppercasing/title case, why case differences inflate vocabulary size |
| `02_text_cleaning.ipynb` | Removing HTML tags, URLs, extra whitespace, and punctuation with `re` |
| `03_tokenization.ipynb` | Word and sentence tokenization with `nltk`, why `word_tokenize` beats `str.split()`, subword tokenization (conceptual) |
| `04_stop_word_removal.ipynb` | Filtering `nltk.corpus.stopwords`, the negation caution (`"not good"` vs `"good"`) |
| `05_stemming_lemmatization.ipynb` | `PorterStemmer` vs `WordNetLemmatizer`, why lemmatization needs a part-of-speech tag |
| `06_full_pipeline.ipynb` | Combining every step into one `preprocess_text()` function, the sentiment-analysis vocabulary example, the search-matching example, best practices and common pitfalls |