## Nezu

[![PyPI version](https://badge.fury.io/py/nezu.svg)](https://pypi.org/project/nezu/)
[![License](https://img.shields.io/badge/license-MIT-teal)](https://opensource.org/license/mit/)
[![Dependencies](https://img.shields.io/badge/dependencies-None-teal)](https://github.com/Nezu-Devs/Nezu/blob/main/pyproject.toml)

### Elegant debuging module

### How to install

`python -m pip install nezu`
or
`python -m poetry add nezu`

### How to use?

Inspect variables scope and value using `say()` function...

```py
# file.py
from nezu import say

x = 13
say('x')
```

...and executing your code with `--nezu` argument.

```bash
python file.py --nezu
```

Output should look something like that.

```python-repl
@5      l  x:int  =>  13
```

### How to interpret output

[Incoming...]

### TO DO

- [x] add class method support?
- [ ] add coloring
- [ ] indicate shadowing
- [ ] write docstring for say
- [ ] write tests for say
- [ ] automate testing with Github actions?
- [ ] automate deployment to PyPI with Github actions?
- [ ] publish to Conda
- [ ] test on different CPython versions
- [ ] test on different Pypy
- [ ] test on Anaconda
- [ ] add badges
- [ ] write proper documentation
  - [ ] How to interpret output
  - [ ] Explain arguments
  - [ ] Note args
  - [ ] brag about being on pypy and and conda
- [ ] make a helper function, that returns dictionary (so it's easier to assert and doesn't require `--nezu`)
  - [ ] write function
  - [ ] write docstring for it
  - [ ] write tests for it
  - [ ] document it in README
- [ ] Write code of conduct
- [ ] Write/generate TOC
