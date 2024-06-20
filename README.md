# Program to manage data types

## Problem:

You are expected to model and implement, in the language of your choice, a program that simulates a data type handler. This program must meet the following characteristics:

a. It must know how to handle atomic types, registers (struct) and variant registers (union).

b. Once the program is started, it will repeatedly ask the user for an action to proceed. Such action can be:
  1. ```ATOMICO <name> <representation> <alignment>```<br>
    Defines a new atomic type of name <name>, whose representation occupies <representation> bytes and must be aligned to <alignment> bytes.
    For example: ```ATOMICO char 1 2 and ATOMICO int 4 4```.
    The program should report an error and ignore the action if <name> already corresponds to some type created in the program.
  2. ```STRUCT <name> [<type>]```<br>
    This defines a new record named <name>. The definition of the record fields is given by the list in [<type>].
    Note that the fields will not have names, but will be represented only by the type they have.
    For example: ```STRUCT foo char int```.
    The program should report an error and ignore the action if <name> already corresponds to some type created in the program or if any of the types in [<type>] have not been defined.
  3. ```UNION <name> [<type>]```<br>
    It defines a new variant record of name <name>. The definition of the variant record fields is given by the list in [<type>]. Note that the fields will not have names, but will be represented only by the type
    that have.
    For example: ```UNION bar int foo int```.
    The program should report an error and ignore the action if <name> already corresponds to some type created in the program or if any of the types in [<type>] have not been defined.
  4. ```DESCRIBIR <name>```<br>
    It must give the information corresponding to the type with name <name>. This information should include size, alignment, and number of bytes wasted for the type, if:
    - The language stores unpackaged registers and variant registers.
    - The language saves registers and packaged variant registers.
    - The language saves records and variant records by ordering the fields optimally (minimizing memory, without violating alignment rules).
    The program should report an error and ignore the action if <name> does not correspond to some type created in the program.
  5. ```SALIR```<br>
    Debe salir del simulador.

At the end of each action, the program must ask the user for the next action.

## Requirements:
To run this program, you must have the following installed:<br>
- Python

## How to install the project
Follow these steps to install the project:
1. **Clone the repository**: Clone the repository using the following git command:<br>
   ```git clone https://github.com/PanquecaFuriosa/Type-Handler```

## How to run the project
Follow these steps to run the project:
1. **Run the following bash command**:<br>
   ```python ManejadorDeTipos.py```
