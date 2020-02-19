# AirBnB_clone

AirBnB Clone Project.

# Objectives

## General

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

# Requirements

## Python Scripts


- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7 or more)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation ```(python3 -c 'print(__import__("my_module").__doc__)')``
- All your classes should have a documentation ```(python3 -c 'print(__import__("my_module").MyClass.__doc__)')```
- All your functions (inside and outside a class) should have a documentation ```(python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')```

## Python Unit Tests

- Allowed editors: **vi**, **vim**, **emacs**
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
- e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
- e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation ```(python3 -c 'print(__import__("my_module").__doc__)')```
- All your classes should have a documentation ```(python3 -c 'print(__import__("my_module").MyClass.__doc__)')```
- All your functions (inside and outside a class) should have a documentation ```(python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')```
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

# Usage

~~~bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
~~~

# Description Files

## Models

| Name | Description |
| ---- | ----------- |
| base_ model.py | BaseModel - this class contains the main base attributes and methods for all classes of objects created. attr(id, created_at, updated_at), methods(save, ```__str__```, to_dict) |
| amenity.py | The objects created under this class serve the host to give a description of the comforts offered by your accommodation |
| city.py | The objects created in this class serve the host to give the location of the offered accommodation |
| place.py | The objects created in this class serve the host to give the description of the place of accommodation |
|review.py | The objects created in this class serve the host and the possible guest to see how the experience lived in the accommodation by previous guests. |
| state.py | The objects created in this class serve the host to show the state where the accommodation is located |
| user.py | Objects created in this class contain user information. |

## Engine

| Name | Description |
| ---- | ----------- |
| file_storage.py | Store and read the objects created in the .json file |

## Console

| Name | Description |
| ---- | ----------- |
| console.py | It is an interpreter that allows you to handle the created objects of the different classes (create them, update them, read them and destroy them). |

# Commands

## Start console

In the terminal type **./console.py + enter**

~~~bash
$./console.py
(hbnb)
~~~

## Create an object

~~~bash
$./console.py
(hbnb) create BaseModel
~~~

## show an object

~~~bash
$./console.py
(hbnb) show
~~~

## destroy an object

~~~bash
$./console.py
(hbnb) destroy
~~~

## all an object

Print all objects

~~~bash
$./console.py
(hbnb) all
~~~

print all objects from specific class **all + ```<class name>```**

~~~bash
$./console.py
(hbnb) all BaseModel
~~~

## update an object

~~~bash
$./console.py
(hbnb) update BaseModel 214143232 atribute value
~~~

# Authors

- [Paula Sotelo](https://github.com/omeinsotelo)
- [Joshua Martinez](https://github.com/dantsub)
