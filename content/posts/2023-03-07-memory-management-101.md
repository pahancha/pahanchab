+++
title = 'Stack and Heap :- Computer Memory 101'
date = 2023-03-07T00:00:00+05:30
draft = false
tags = ['Programming', 'Computer Memory', 'Data Structures']
+++

When giving instructions to computers(programming, not giving commands in natural language), computer memory is the space where the instructions (computer program) and data are stored during runtime.
<!--more-->

Computer memory can be divided into two primary types. 
* Stack Memory
* Heap Memory

## Stack Memory
Stack memory is the area of memory that is allocated to the program automatically by the compiler. The stack memory is used to store data and metadata related to the execution of a program which are listed below. 

* **Function parameters.** - When a function is called, its parameters are typically passed on to the stack memory. For example, let's assume that a function has parameters x and y. When the function is called, the values of x and y are pushed to the stack. Then the function accesses them from the stack memory.

* **Local variables.** - The variables that are declared inside a function are defined as local variables. And the local variables are only accessible within the function scope. Let’s assume that variable x has been assigned the value of 12. The value of x would be stored in the stack until that particular function returns. 

* **Function return addresses.** - When a function is called, the address of the next intended instruction to execute can be called the function return address. The function return address is pushed into the stack memory and this allows the program to return to the correct location after the execution of the function has been completed.

The stack memory is managed by the CPU. Mainly pushing and popping data from the stack memory as required by the particular program.

## Heap Memory

Heap memory is used to store dynamically allocated data such as arrays and objects. In many programming languages such as Java and python, the heap memory is managed automatically by a process known as garbage collection. 
But when it comes to a low level programming language like C, it does not have built-in garbage collection. It's the programmer’s duty to manage memory allocation and deallocation using `malloc()` and `free()` functions. If the programmer fails to deallocate heap memory, it can lead to memory leaks.
