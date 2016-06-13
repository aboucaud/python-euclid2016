# Python Project Architecture

## Slides

You will find [here](https://github.com/aboucaud/python-euclid2016/blob/master/notebooks/06-Project.pdf) a presentation given at the second Euclid Developer Workshop on the architecture of a Python project. It contains examples of project directories, and information on how to use `__init__.py` files, the `__all__` variable and the guidelines to clarify a project structure.

***Note***: This does not include instructions on how to write the `setup.py`.

## A toy project

A toy Python project called `euclid` has been shipped with this tutorial and can be found under `python-euclid2016/euclid`, along with a `tests` directory to be used in the testing lesson. The purpose of this project is for you to play around with, especially with the content of the `__init__.py` files.
Before switching to the test lesson, make sure you revert the changes back to their original state

    cd /path/to/python-euclid2016/euclid
    make clean
    make revert

### First glimpse at the `euclid` project

The full project directory can be visualized using the `tree` software (`sudo yum install -y tree` on the VM)

    make clean
    tree euclid/
    euclid/
    ├── __init__.py
    ├── hello.py
    ├── maths
    │   ├── __init__.py
    │   ├── mystats.py
    │   └── mytrigo.py
    └── time
        ├── __init__.py
        └── mytime.py

To be considered as a (sub)module, a folder must contain an `__init__.py` file, empty or not. This project is thus made of one main module `euclid` and two submodules (or subdirectories) `maths` and `time`. The main purpose of such enhanced directory structure is to clarify the code by grouping Python files by topic. Restructuring a code in such manner also helps lowering the number of code lines in each separate file to improve readability and debugging.

### First import of the module

Let's open an IPython terminal and import the `euclid` module.

    ipython

```python
>>> import euclid
>>> print([mod for mod in dir(euclid) if not mod.startswith('__')])
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'maths', 'now', 'time']
>>> # Let's print only the imported elements
>>> print([mod for mod in dir(euclid) if not mod.startswith('__')])
['maths', 'now', 'time']
```

The `maths` and `time` submodules have been imported as well as the `now` object which can be an external module, a function, a variable, etc. To determine its type, one can use the "?" operator

```python
>>> euclid.now?
Signature: euclid.now()
Docstring: Print the current time in a readable way
File:      ~/work/Euclid/devel/python-euclid2016/euclid/euclid/time/mytime.py
Type:      function
```

`now` is thus a function in `mytime` under the `time` submodule.

The only way it has been imported at such high level is because this import has been specify in the higher level `__init__.py`. One can check the content (source) of this file with the "??" operator

```python
>>> euclid??
Type:        module
String form: <module 'euclid' from '/Users/aboucaud/work/Euclid/devel/python-euclid2016/euclid/euclid/__init__.py'>
File:        ~/work/Euclid/devel/python-euclid2016/euclid/euclid/__init__.py
Source:
"""
Euclid - Python tutorial project

The purpose of this toy-model project is to show the various possibilities
to organized.

"""
from . import maths
from .time import now
```

We find an import of the `maths` submodule and a direct import of the `now` function, but no specific import of `time`. The reason the submodule `time` has also been imported is because it is in the path of the `now` function.


### Specific imports

At the first level under the `euclid` module, there is a `hello` file

    make clean
    tree -L 1 euclid/
    euclid/
    ├── __init__.py
    ├── hello.py
    ├── maths
    └── time

This file contains a single function `helloworld` that currently remains unaccessible using the `import euclid`. In order to use it, one requires to use a specific import

```python
>>> import euclid.hello
>>> euclid.hello.helloworld()
Hello world!
```

***Note*** importing `euclid.hello` **without renaming** also imports `euclid`.


### Uses of `__init__.py`

#### Documenting

As seen above, an `__init__.py` file can (and should) contain a docstring that informs on the purpose of the submodule. Like the docstring of every function or class, it can be obtain by requesting information on the (sub)module directly

```python
>>> euclid.maths?
Type:        module
String form: <module 'euclid.maths' from '/Users/aboucaud/work/Euclid/devel/python-euclid2016/euclid/euclid/maths/__init__.py'>
File:        ~/work/Euclid/devel/python-euclid2016/euclid/euclid/maths/__init__.py
Docstring:
Maths submodule

Contains
- trigonometric methods
- stats methods
```


#### Clarifying imports

The `__init__.py` help create a clear and comprehensive structure within a project by splitting classes and methods between files of reasonable size and gathering the one with a common purpose. Although this can help a lot on the developer side, the user may find it tedious to write the full path in order to import methods embedded far in the directory tree, e.g.

```python
>>> from euclid.maths.mytrigo import trigo
>>> from euclid.maths.mystats import average
```

Instead one might rather want to import these methods at the maths level

```python
>>> from euclid.maths import trigo, average
```

This is possible **without changing the directory structure** by writing some local imports inside the `euclid/maths/__init__.py`. This will make the methods available one level up the chain.

This can be done in any `__init__.py`, allowing methods to skip several levels e.g. `now` which is written at the very end

```python
>>> from euclid.time.mytime import now
```

but can be called directly at the base level

```python
>>> from euclid import now
```

since `euclid/__init__.py` has a local import of the `now` method

```python
# in euclid/__init__.py

from .time.mytime import now
```

files of the `maths` and `time` submodules show two different ways of making methods available one level up ; that is making the methods callable at the submodule level instead of needing the full path to catch them.

For instance, for the `maths` submodule, the `__init__.py` imports `trigo` and `trigonp` from `mytrigo`

#### Relative imports

In the `__init__.py` files, it is a good convention (shared among lots of well know projects) to use relative imports. It means that instead of using the full path when importing a method or a submodule, a.k.a. **absolute imports** e.g. in `euclid/maths/__init__.py`

```python
# in euclid/maths/__init__.py

import euclid.maths.mystats
# and/or
from euclid.maths.mystats import average
```

one uses a **relative imports**

```python
# in euclid/maths/__init__.py

from . import mystats
# and/or
from .mystats import average
```

This is only valid **within a given project** and does not extend to external libraries, even those that are shipped with your project.


### The `__all__` variable

If there is one major rule about imports in Python, it is to never write

    from module import *

in a module. It fills the namespace with a ton of useless methods, than can potentially create a collision with your own methods or classes, and forgets about the paternity of all imported methods.

**However** the behaviour of the `from mymodule import *` can be set through the `__all__` variable inside `mymodule.py`.
An example is given in this project with `mytrigo.py`. This file contains three method definitions `trigo`, `trigonp` and `useless_trigo`, and an `__all__` variable set to the list of the first two methods

```python
# in euclid/maths/mytrigo.py

__all__ = ['trigo', 'trigonp']
```

Therefore, when calling

```python
# in euclid/maths/__init__.py

from .mytrigo import *
```

the only things imported are the two methods `trigo` and `trigonp` and none of the other variables defined in `mytrigo.py` like `np` or `math` or `useless_trigo`.

While the rule stated on top remains valid for any module file, `import *` statements are **allowed** in the `__init__.py` files **together with** the use of the `__all__` variable in the imported module since they help, once again, clarifying what elements are imported in the namespace.
