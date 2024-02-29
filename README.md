## Nezu

[![PyPI version](https://badge.fury.io/py/nezu.svg)](https://pypi.org/project/nezu/)
[![License](https://img.shields.io/badge/license-MIT-teal)](https://opensource.org/license/mit/)
[![Dependencies](https://img.shields.io/badge/dependencies-None-teal)](https://github.com/Nezu-Devs/Nezu/blob/main/pyproject.toml)

### Elegant debugging module

Example
```py
# file.py
from nezu import say

x = 13
say('x')
```
```bash
$ py file.py --nezu
@5      l  x:int  =>  13
```


### How to install?

```bash
$ python -m pip install nezu
```
or
```bash
$ python -m poetry add nezu
```

### How to use?

#### Basic usage


Inspect variable using `say()` function. Pass name of variable you want to inspect as `str` argument. 

```py
# file.py
from nezu import say

say('egg')          # works on simple variables
say('ham.spam')     # works on attributes
say('spam["spam"]') # works on keys and indexes
say('print')        # works on functions and build-ins
```

Output is hidden by default. If you want to display debug commands run your program with argument `--nezu`.

```bash
$ python file.py            # Nothing is displayed by this command
$ python file.py --nezu     # But everything is displayed by this command
@4      u  egg
@5      u  ham.spam
@6      u  spam["spam"]
@7      b  print:function  =>  Prints the values to a stream, or to sys...
```

### How to interpret output?

```
@7      b  print:function  =>  Prints the values to a stream, or to sys...
 │      │  │     │             │
 │      │  │     │             └───────── Value of inspected variable
 │      │  │     └─────────────── Type of inspected variable.
 │      │  └───────────── Name of inspected variable.
 │      └──────── Scope of inspected variable.
 │				  l:local, g:global, b:build-in, u:undefined          
 └────── Line number of inspection.
```

### Coloring output

By default nezu output is monochrome.
You can color output on terminals that support it. Instead of passing `--nezu` at execution, pass `--nezu-color`.

### Hiding output

Function `say()` can be can be hidden into deeper levels of debugging via `hide` parameter. Execution argument `--nezu` seeks only for says hidden at level 1. Now if you want to display more, you run your program with `--nezu-seek` integer argument. In example bellow only says hidden up to level 3 are displayed.

```python
#file.py
from nezu import say

say('egg', hide=1)
say('ham', hide=2)
say('spam', hide=3)
say('bacon', hide=4)
say('lobster', hide=5)
```

```
$ python file.py --nezu-seek=3
@4      u  egg
@5      u  ham
@6      u  spam
```

### TO DO

- [x] add class method support?
- [x] add coloring
- [ ] add classes parameter (so you can print only group of logs)
- [ ] indicate shadowing
- [x] write docstring for say
- [ ] write tests for say
- [ ] automate testing with Github actions?
- [ ] automate deployment to PyPI with Github actions?
- [ ] publish to Conda
- [ ] test on different CPython versions
- [ ] test on different Pypy
- [ ] test on Anaconda
- [ ] add badges
- [ ] format files with blue
- [ ] remove obsolete tests
- [ ] gitignore .vscode, __pycache, dist
- [ ] write proper documentation
  - [x] How to interpret output
  - [ ] Explain arguments
    - [x] Hiding
    - [ ] Notes
    - [ ] args
  - [ ] Note args
  - [ ] brag about being on pypy and and conda
- [ ] make a helper function, that returns dictionary (so it's easier to assert and doesn't require `--nezu`)
  - [ ] write function
  - [ ] write docstring for it
  - [ ] write tests for it
  - [ ] document it in README
- [ ] Write code of conduct
- [ ] Write/generate TOC
