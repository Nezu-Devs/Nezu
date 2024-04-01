## Nezu

[![PyPI version](https://badge.fury.io/py/nezu.svg)](https://pypi.org/project/nezu/)
[![License](https://img.shields.io/badge/license-MIT-teal)](https://opensource.org/license/mit/)
[![Dependencies](https://img.shields.io/badge/dependencies-None-teal)](https://github.com/Nezu-Devs/Nezu/blob/main/nezu/pyproject.toml)

Elegant debug module

- **_Python Code Example_**

  ```py
  # file.py
  from nezu import dbg
  x = 13
  dbg('x')  # Prints debug info.
  ```

- **_Bash Commands to Debug_**

  ```bash
  export NEZU_SEEK=1
  python file.py
      @4 L.. x:int  =>  13
  ```

- **_Powershell Commands to Debug_**

  ```bash
  $env:NEZU_SEEK = 1
  python file.py
      @4 L.. x:int  =>  13
  ```

### Table of Contents

[NEZU](#nezu)

- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
  - [Output Interpretation](#output-interpretation)
  - [Function dbg](#function-dbg)
- [Config](#config)
  - [Env Vars Config](#env-vars-config)
  - [JSON Config](#json-config)
  - [Hardcoded Config](#hardcoded-config)
- [Coloring output](#coloring-output)
- [Hiding output](#hiding-output)

### Installation

- **_Pip_**

  ```bash
  python -m pip install nezu
  ```

- **_Poetry_**

  ```bash
  python -m poetry add nezu
  ```

### Usage

- Inspect variable using [function dbg](#function-dbg) in your code.
- [Configure](#config) Nezu to show output.
- [Interpret](#output-interpretation) output and debug.

#### Output Interpretation

```
@7 ..B print:function  =>  Prints the values to a stream, or to sys...
 │ │   │     │             │
 │ │   │     │             └─ Value of inspected variable
 │ │   │     │
 │ │   │     └─────────────── Type of inspected variable.
 │ │   │
 │ │   └───────────────────── Name of inspected variable.
 │ │
 │ └───────────────────────── Scope of inspected variable (see bollow).
 |
 └─────────────────────────── Line number of inspection.
```

- **_Scope codes_**
  - `L..` - local scope, no shadowing
  - `Lg.` - local scope, shadowing global
  - `L.b` - local scope, shadowing built-in
  - `Lgb` - local scope, shadowing global and built-in
  - `.G.` - Global scope, no shadowing
  - `.Gb` - Global scope, shadowing built-in
  - `..B` - Built-in scope, no shadowing
  - `...` - Undefined 

#### Function `dbg`

Inspect scopes and values of given keys (variable names etc.).

- **_Args_**

  - `*keys:str`

    Names of variables to inspect

  - `note:str = None`

    Optional comment. Ignored if equal to None.

  - `hide:int = 1`

    This argument is compared with `nezu.seek`.
    If `nezu.seek >= hide` this debug inspection will be displayed.
    If hide <= 0, this message will be displayed by default.

- **_Python Code Example_**

  ```py
  # file.py
  from nezu import dbg

  egg = 3
  ham = int()
  spam = {'spam':'bacon'}

  dbg('egg')          # Works on simple variables.
  dbg('ham.real')     # Works on attributes.
  dbg('print')        # Works on functions and built-ins.
  dbg('spam["spam"]') # DOES NOT work on keys and indexes yet.
  ```

- **_Note_**

  Output of `dbg` function is hidden by default. If you want to see dbg you need to configure env var `NEZU_SEEK` with value of `1` or more.

### Config

Module `nezu` creates `nezu` object that has config attributes used by function `dbg`.

- **_Attributes_**
  - `nezu.seek:int = 0`
    Compared to `dbg` argument`hide`, if `nezu.seek >= hide` then `dbg` will be printed.
  - `nezu.color:bool = False`
    Determines if output of `dbg` function should be colored.
  - `nezu.lock:bool = False`
    If `nezu.lock = True`, this config cannot be changed later, during runtime.

#### Env Vars Config

If you want to use default config method, change your _env vars_ in terminal and run Python script.

- **_Bash_**

  ```bash
  export NEZU_SEEK=1
  export NEZU_COLOR=1
  export NEZU_LOCK=0
  python file.py
  ```

- **_PowerShell_**
  ```powershell
  $env:NEZU_SEEK = 1
  $env:NEZU_COLOR = $True
  $env:NEZU_LOCK = $True
  python file.py
  ```

#### JSON Config

If you don't want to use _env vars_ as config, you can call `nezu.json()` to read config data from json file.
It will search for key `nezu` inside chosen file.

- **_Args_**

  - `path:str = 'nezu.json'` - path of config file

- **_Example Python Code_**

  ```python
  from nezu import nezu, dbg
  nezu.json('my/json/file.json')
  ```

- **_Example Config File_**

  ```json
  "nezu": {
    "seek": 1,
    "color": true,
    "locked": false
  }
  ```

---

#### Hardcoded Config

If you don't want to use _env vars_ as config you can also call object `nezu` like function to make hardcoded config.

- **_Args_**

  - `seek:int = 0` - debug level
  - `color:bool = False` - output coloring
  - `lock:bool = False` - lock this config

- **_Example_**

  ```py
  # file.py
  from nezu import nezu, dbg

  nezu(1, True, False)
  ...
  ```

- **_Tip_**

  There is no built-in support for _yaml_, _toml_ or _.env_ in _nezu_
  This is so _nezu_ can stay free of dependencies.
  However you can use hardcoded config to pass data from any config file.

### Coloring output

By default nezu output is monochrome.
If your terminal of choise support coloring you can change that.

- **_Example Bash Command_**

  ```bash
  export NEZU_COLOR=1
  python file.py
  ```

- **_Example PowerShell Command_**

  ```powershell
  $env:NEZU_COLOR = $True
  python file.py
  ```

- **_Example JSON Config File_**

  ```json
  "nezu": {
    "color": true,
  }
  ```

- **_Example Hardcoded Config_**

  ```py
  from nezu import nezu, dbg

  nezu(color = True)
  ...
  ```

### Hiding Output

Function `dbg()` can be hidden more by `hide` parameter. By default only `dbg` calls with `hide <= nezu.seek` will be printed. In examples bellow only `dbg` hidden up to level 3 are displayed.

- **_Python Code Example_**

  ```python
  #file.py
  from nezu import dbg

  dbg('egg', hide=1)
  dbg('ham', hide=2)
  dbg('spam', hide=3)
  dbg('bacon', hide=4)
  dbg('lobster', hide=5)
  ```

- **_Bash Example_**

  ```bash
  export NEZU_SEEK=3
  python file.py
        @4 ... egg
        @5 ... ham
        @6 ... spam
  ```

- **_PowerShell Example_**

  ```powershell
  $ENV:NEZU_SEEK = 3
  python file.py
        @4 ... egg
        @5 ... ham
        @6 ... spam
  ```

- **_JSON File Example_**

  ```json
  "nezu": {
      "seek": 3
  }
  ```
