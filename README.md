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
  - [Debuf Interpretation](#debug-interpretation)
  - [Function dbg](#function-dbg)
  - [Function say](#function-say)
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

- Inspect variables with [function `dbg`](#function-dbg).
- Display literals with [function `say`](#function-say).
- [Configure Nezu](#config) to show output.
- [Interpret output](#debug-interpretation).
- Fix bugs.

#### Debug Interpretation
Using debbuging function `dbg` will display something like:
- **_Example output_**
  ```
  @7 ..B print:function  =>  Prints the values to a stream, or to sys...
  ```
- **_Interpretation_**
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

To debug, use funtion `dbg`, it will inspect scopes and values of given keys (variable names etc.).

- **_Args_**

  - `*keys:str`

    Names of variables to inspect

  - `hide:int = 1`

    This argument is compared with `Nezu.seek`.
    If `Nezu.seek >= hide` this debug inspection will be displayed.


  - `bp:int = 0`

    This argument is compared with `Nezu.flow`.
    If `Nezu.flow < bp` this debug inspection will be considered breakpoint.

- **_Python Code Example_**

  ```py
  # file.py
  from nezu import dbg

  nortius = 3
  maximus = int()
  biggus = {'dickus':'sillius'}

  dbg('nortius')          # Works on simple variables.
  dbg('maximus.real')     # Works on attributes.
  dbg('print')            # Works on functions and built-ins.
  dbg('biggus["dickus"]') # DOES NOT work on keys and indexes yet.
  ```

- **_Note_**

  Output of `dbg` function is hidden by default. If you want to see dbg you need to configure env var `NEZU_SEEK` with value of `1` or more.

#### Function `say`

Simple literal output.

- **_Args_**

  - `*val`

    Value to display.

  - `hide:int = 1`

    This argument is compared with `nezu.seek`.
    If `nezu.seek >= hide` this call will be displayed.

  - `bp:int = 0`

    This argument is compared with `Nezu.flow`.
    If `Nezu.flow < bp` this call will be considered breakpoint.

- **_Python Code Example_**

  ```py
  # file.py
  from nezu import say

  biggus = 'dickus'

  say('biggus') # displays something like `      @5 biggus`
  say(biggus)   # displays something like `      @6 dickus`

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
  export NEZU_FLOW=5
  export NEZU_COLOR=1
  export NEZU_LOCK=0
  python file.py
  ```

- **_PowerShell_**
  ```powershell
  $env:NEZU_SEEK = 1
  $env:NEZU_FLOW = 5
  $env:NEZU_COLOR = $True
  $env:NEZU_LOCK = $False
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
    "flow": 5,
    "color": true,
    "locked": false
  }
  ```

---

#### Hardcoded Config

If you don't want to use _env vars_ as config you can also call object `nezu` like function to make hardcoded config.

- **_Args_**

  - `seek:int = 0`

    Debug level

  - `flow:int = 5` 

    Skipping breakpoits

  - `color:bool = False`

    Output coloring

  - `lock:bool = False` 

    Lock this config


- **_Example_**

  ```py
  # file.py
  from nezu import nezu, dbg

  nezu(1, 7, True, False)
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

Functions `dbg()` and `say()` can be hidden more by `hide` parameter. By default only calls with `hide <= nezu.seek` will be printed. In examples bellow only `dbg` hidden up to level 3 are displayed.

- **_Python Code Example_**

  ```python
  #file.py
  from nezu import say

  say('biggus', hide=1)
  say('dickus', hide=2)
  say('nortius', hide=3)
  say('maximus', hide=4)
  say('sillius', hide=5)
  say('soddus', hide=6)
  ```

- **_Bash Example_**

  ```bash
  export NEZU_SEEK=3
  python file.py
        @4 biggus
        @5 dickus
        @6 nortius
  ```

- **_PowerShell Example_**

  ```powershell
  $ENV:NEZU_SEEK = 3
  python file.py
        @4 biggus
        @5 dickus
        @6 nortius
  ```

- **_JSON File Example_**

  ```json
  "nezu": {
      "seek": 3,
  }
  ```
- **_Example Hardcoded Config_**

  ```py
  from nezu import nezu, dbg

  nezu(3)
  ...
  ```
### Breakpoints

Functions `dbg()` and `say()` can be used as breakpoints by `bp` parameter. Calls with `bp > nezu.flow` will stop program execution. Hidden calls are never considered brerakpoints. In examples bellow only second call will behave as breakpoint.

- **_Python Code Example_**

  ```python
  #file.py
  from nezu import dbg

  say('biggus' bp=6)
  say('dickus', bp=7)
  say('nortius', hide=2, bp=8)
  ```

- **_Bash Example_**

  ```bash
  export NEZU_SEEK=1
  export NEZU_FLOW=6
  python file.py
        @4 biggus
        @5 dickus   # Program stop execution until user press Enter
        @6 nortius
  ```

- **_PowerShell Example_**

  ```powershell
  $ENV:NEZU_SEEK = 1
  $ENV:NEZU_FLOW = 6
  python file.py
        @4 biggus
        @5 dickus   # Program stop execution until user press Enter
        @6 nortius
  ```

- **_JSON File Example_**

  ```json
  "nezu": {
      "flow": 6,
  }
  ```
- **_Example Hardcoded Config_**

  ```py
  from nezu import nezu, dbg

  nezu(flow = 6)
  ...
  ```