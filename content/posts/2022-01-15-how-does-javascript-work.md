+++
title = 'How does JavaScript Work?'
date = 2022-01-15T00:00:00+05:30
draft = false
tags = ['Programming', 'JavaScript', 'Under The Hood']
+++

JavaScript has become the leading language of the web due to the rapid development of the JavaScript based Libraries and Frameworks during the last decade. Hundreds of libraries and frameworks, for both front end and back end. As I know there are plenty of people in my circle who work with these frameworks and libraries on a daily basis but have no idea about what’s going on under the hood. <!--more-->
Frankly, I too belonged to the same group until I wanted to know what this all about. How did JavaScript become so popular? And moreover, how does JavaScript work?

To talk about JavaScript, first, we have to turn towards our web browser. Mainly web browsers consist of two main programs. These are the main programs that play a huge role when it comes to displaying web pages on our mobile or computer.

### Rendering Engine

Rendering engine consists of the HTML Parser and the CSS Parser. And this bears the responsibility to convert the HTML code and the CSS code into structured web pages that we visually see in the web browser.

### JavaScript Engine

And the JavaScript Engine, javascript engine is the heart of functioning js code. This holds the responsibility of converting the js syntax into machine code.

JavaScript is laid out according to ecma-262 standard. Therefore JavaScript is a High-level, multi-paradigm, dynamic programming language and those definitions are directly related with ecma-262 standards. However ecma-262 does not specify how the javascript interpreter should be implemented.
JavaScript is an interpreted programming language. Hence an interpreter is needed to convert the javascript syntax into machine code.

Since the ecma-262 standard does not carry information about the javascript interpreter, those implementations are done by browser developers.

The way different JavaScript engines work is slightly different but most of them do a thing called JIT (Just In - Time) compilation. Here, Converting the JavaScript code into machine code gets the features of a compiler.

#### There are a number of javascript engines developed by different organizations and communities.

- Google - V8
- FIrefox - spider monkey
- Safari - Nitro
- Internet Explorer / Edge - Chakra

{% include aligner.html images="posts/spider-monkey.jpg" %}

_In case you wonder, Here is a spider monkey._

In this scenario, let’s take a look at the <b>V8 engine</b>,the JavaScript engine which is used inside Google Chrome and Node.js. V8 was originally designed and developed by the big brains at Google, the people who know what they do. V8 is open source and written in C++.

As I mentioned above, most of the js engines do “JIT Compilation”. V8 does it too. So what is this JIT? JavaScript is a very fast language even though it is a dynamically typed language(We will discuss this later.). JIT compilation is the reason for that. During the Just In Time Compilation, the machine code is being generated during the runtime. Compilation and the execution goes at the sametime. Remember in JIT compilation it’s <b>not</b> first compiling ahead of time, finishing the compilation and then executing. It’s a mix of both of the processes.

In modern JavaScript engines, there are at least two compilers. One of the two is an optimizing compiler and the other being the baseline compiler. The optimizing compiler re-complies the “hot functions” in the JS code. A function which is being used a lot and worth speeding up the process is identified as a hot function. So compile, run a few times, optimize, assuming certain conditions, run the optimized code, if the conditions fail, go back to the basic code.

{% include aligner.html images="posts/JavaScriptCode.jpg" column=1 %}

If we come to the V8 engine again, The baseline compiler in the V8 engine is called the “Ignition”. The Optimizing Compiler is called “TurboFan”.

Different JavaScript engines have different optimizers and baseline compilers. Some may have not only one but several numbers of optimizing compilers. For example, safari has two of them.

How JavaScript works is actually a quite complex topic. We have to talk about topics like ‘why javascript is a dynamically typed language?’, ‘What is the JavaScript Parser?’ etc. Hope to learn more and share more about ‘JavaScript under the hood’ in this blog in the future.
