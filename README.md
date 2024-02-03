Introduction to Programmin in Python - Final Project
===
## TODOs

In this project, we are going to design a pocket money manager. The application keeps records of money deposit and withdrawal and allows addition, deletion, modification of each records. The records will be kept in the `record.txt` file.

## Demo

* Start Messages

    ```shell
        > How much money do you have?     20000
        > You have  20000  dollars
        > Reset your money? (Yes/No)      No
    ``` 
* View Records
     ```shell
        > What do you want to do (Add, View, Delete, Categories, Find, Exit)?  View
        > Here's your expense and income record:
        > Record  Category        Description     Amount
        > ------  --------------  --------------  ------
        > 1       food            dinner            -100
        > 2       transportation  bikes              -20
        > ------  --------------  --------------  ------
        > Now you have  19880  dollars!
    ```
* Add Records

    ```shell
        > What do you want to do (Add, View, Delete, Categories, Find, Exit)?  Add
        > Add some expense or income records with category, discription, and amount:
        > food dinner 100
    ```
* Delete Records

    ```shell
        > What do you want to do (Add, View, Delete, Categories, Find, Exit)?  Delete
        > Which record do you want to delete?     1
    ```

* Show Categories

    ```shell
        > What do you want to do (Add, View, Delete, Categories, Find, Exit)?  Categories
        > -expense
        >   -food
        >     -meal
        >     -snack
        >     -drink
        >   -transportation
        >     -bus
        >     -railway
        > -income
        >   -salary
        >   -bonus
     ```

* Find Records

    ```shell
        > What do you want to do (Add, View, Delete, Categories, Find, Exit)?  Find
        > Which category do you want to find?     transportation
        > Here's your expense and income records under category " transportation ":
        > Record  Category        Description     Amount
        > ------  --------------  --------------  ------
        > 1       transportation  bikes              -20
        > ------  --------------  --------------  ------
        >                                            -20
    ```
