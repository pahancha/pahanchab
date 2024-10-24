+++
title = 'Unlocking the power of Data Structures in C'
date = 2023-06-14T00:00:00+05:30
draft = false
tags = ['Programming', 'Computer Memory', 'Data Structures']
+++

Arrays, Structures Unions, Enums, Pointers and Bit Fields in C language.

<!--more-->

As I began revising data structures, my curiosity led me toward the C language and its inherent data types and structures. Unlike high-level programming languages, C doesn't offer built-in data structures such as dynamic arrays, linked lists, hash tables/maps, stacks, or queues. Instead, it provides some basic yet powerful low-level data structures. The purpose of this post is to discuss these data structures in a brief yet informative manner.


### Arrays
Imagine that you need to store multiple values of the same type. Replacing dozens of variables, arrays come into play!
An array is like a container, holding elements of a single type. Arrays in the C language are a fixed-size, sequential collection of elements of the same type. For example, we can declare an array of 5 integers as 'int array[5]'.

``` c
int array[5] = {1, 2, 3, 4, 5}
```

As usually accessing those elements is possible via element's index. 
``` c
printf("%d", array[2])
```

In C, there is no built-in way to remove an element from an array. Arrays in C are static meaning that the size is fixed at the time of declaring the array. 

### Structures

Structures in C, is a user defined data type that allows related data elements to be grouped together. This is useful when we want to store related data that are of different types (int, char, float, double). For example, we can store information about a book such as title, author, price in a single structure. 

``` c
struct Book {
    char title[50];
    char author[50];
    float price;
}
```

After defining the stucture type, we can create structure variables. 

``` c
struct Book book1, book2;
```
Above, book1 and book2 are variables of the 'Book' structure type. 

We can access the fields of a structure using the dot operator. 
```c
strcpy(book1.title, "The C Programming Language");
strcpy(book1.author, "Dennis Ritchie");
book1.price = 19.99;

printf(book1.author)
```

### Unions

Union is a special data type that allows different types of variables to share the same memory location. You can define a union with many members, but only one member can contain a value at any given time.

```c
union my_union {
    int my_int;
    double my_double;
}

union my_union u;
u.my_int = 2 // The union now contains an int. Any previous value (int or double) is overwritten.

u.my_double = 4.5 // The union now contains a double value. The previous int value is now overwritten.
```

### Enums
Enumerations are a data type that consists of inegral contrants. By default, the first enumerator has the value 0, and the value of each successive enumerator is increased by 1.

For example we can have a 'week' enum like below. 
```c
enum week {
    Sun,
    Mon, 
    Tue,
    Wed,
    Thu,
    Fri,
    Sat
}
```
By default, the days will be assigned values from 0 to 6.

### Pointers

A pointer is a aribale that stores the address of another variable. Pointers provide the basis for dunamic data structures such as linked lists, trees and graphs. To declare a pointer, we have to use '*' operator in "int *ptr" way. Here, ptr is a pointer to an integer.

Pointers deal with memory addresses directly and can be tricky to understand at the first place. I am hoping to write about pointers in a dedicated post. 

```c
int var = 20;
int *ptr;
ptr = &var;
```

### Bit Fields

Bit fileds allow the packing of data in a structure. This is especially useful when memory is limited. As mentioned earlier, bit field is declared as a structure, where the number of bits used for each element is specified. 

```c
struct BitField {
    unsigned int is_true:1;   // Uses only 1 bit
    unsigned int value:4;     // Uses 4 bits
    unsigned int:0;           // Forces alignment to next boundary.
    unsigned int other_value:6;  // Uses 6 bits
};
```

As we can see, the basic low level data structures in c, involves memory not like other high-level programming languages. Even though there is a learning curve, learning data structures in C, allows to explore the inner behaviour of data structures and helps to understand them in a better and clearer way. 



