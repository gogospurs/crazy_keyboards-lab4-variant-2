# crazy-keyboards - lab 4 - variant 2

Group Member:

- Haixiao Wang 212320012
- Yu Zhang 212320015

## Variant description

- implement a multiple-dispatch library for Python in

Common Lisp Object System (CLOS) style by decorators,

and add the before, after, around method.

## Project structure

- `multipledispatch_module.py` -- multiple-dispatch library

- `dispatch_example_func` -- example function implemented with library

- `example_func_test.py` -- unit and PBT tests for example function

## Features

- PBT: `test_add_dict`, `test_add_float`, `test_add_int`,

`test_add_list`, `test_add_str`, `test_add_inheritance`,

`test_add_IntAndFloat`

## Contribution

- Yu Zhang -- module part and upload the files to github
- Haixiao Wang -- example function and test part

## Explanation of taken decision and analysis

- The libarary mainly contains three parts,

one is the dispatch libary which include the before,

after, and around method with clos style, and one is

the function impled the multipledispatch module,

the last one is the test part.

## Conclusion

- First of all, in this lab,

we met many problems that need to be considered as a library developer.

An excellent container library should support functions of variable objects.

Function, which helped us detect many problems.

## Changelog

-20.06.2022 - 0
  -Initial
