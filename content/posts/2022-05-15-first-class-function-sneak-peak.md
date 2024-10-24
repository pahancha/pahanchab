+++
title = 'Sneak Peak to First Class Functions'
date = 2022-05-15T00:00:00+05:30
draft = false
tags = ['Programming', 'JavaScript', 'Under The Hood']
+++

If a programming language treats functions as any other variable, that particular programming language is considered to have first-class functions. <!--more-->

In a programming language with first-class functions,

* A function can be assigned as a value to a variable.
* A function can be passed as an argument to another function. 
* Another function can return a function.

## Assign a function to a variable.

```js

const helloWorld = function() {
	console.log(“Hello worldz!”);
}

helloWorld();
```

## Pass a function as an argument to another function.

```js
function sayHello() {
	Return “hello”;
}

function greeting(message, name) {
	console.log(message() + name );
}

greeting(sayHello, “world!”);

```
The above sayHello function is passed as an argument to the greeting function. When a function is used as an argument to another function, that function is called a callback function. Therefore sayHello() is a callback function.

## Return a function from another function.

In a programming language with first-class functions, functions are treated as a value. So a function can be returned from another function. 

```js
function sayHelloWorld() {
	return function() {
		console.log(“Hello world!”);
    }
}
```
If a function returns another function, that function is called a Higher-Order function.

To invoke a Higher-Order function, there are two ways.
1. Using Variables.

```js
const sayHelloWorld() {
	retun function() {
	console.log(“Hello World!”);
    }
}

const func = sayHello();
func();

```

2. Using double parentheses.

```js

function sayHelloWorld() {
	return function() {
		console.log(“Hello world!”);
    }
}

sayHelloWorld()();

```

For the above examples, I have Used JavaScript. JavaScript is not the only language with first-class functions. 

Most functional programming languages (Haskell, Scala, Julia …)  and scripting languages (JavaScript, Python, Perl, PHP … ) are considered to have first-class functions.
