# CLASS XI COMPUTER SCIENCE

# UNIT 2 : INTRODUCTION TO C++

**(Assam Higher Secondary First Year — AHSEC Syllabus)**

> **How to use these notes**
> Every topic in this unit is explained using the same simple pattern so that you can revise quickly before the exam:
>
> **Definition → Explanation → Important Points → Example → Exam Tip → Common Mistakes → Board Question**
>
> The language is kept very easy because this is the first time you are learning programming. Read each program slowly, type it yourself, and always check the output.

---

## TABLE OF CONTENTS

1. **Getting Started**
2. **Data Types, Variables and Constants**
3. **Operators and Expressions**

---
---

# CHAPTER 1 : GETTING STARTED

---

## 1.1 Introduction to C++

### Definition
C++ is a **general-purpose, high-level programming language** developed by **Bjarne Stroustrup** at Bell Laboratories (AT&T, USA) in the year **1979**. It is an **extension of the C language**, so it was first called *"C with Classes"* and later renamed **C++** in 1983.

### Explanation
- A **programming language** is a language used to write instructions for a computer.
- C++ was made by adding new features (mainly **Object-Oriented Programming**) to the old **C language**.
- The symbol `++` is taken from C++ itself. In C, `++` means "add one more". So **C++ means "C plus new features" (C incremented)**.
- C++ supports two styles of programming:
  - **Procedural programming** (writing programs as a set of functions/steps).
  - **Object-Oriented programming (OOP)** (writing programs using objects and classes).

### Important Points
- Developed by **Bjarne Stroustrup** in **1979** at **Bell Labs**.
- Old name = **C with Classes**; new name (1983) = **C++**.
- C++ is a **superset of C** (whatever C can do, C++ can also do).
- It is a **compiled language** (the whole program is translated at once before running).
- It is used to make operating systems, games, browsers, banking software, etc.

### Example
A very simple C++ program that prints a message on the screen:

```cpp
#include<iostream.h>
void main()
{
    cout << "Welcome to C++";
}
```

**Output:**
```
Welcome to C++
```

### Exam Tip
Remember these three things for a **1-mark** question: **Who** (Bjarne Stroustrup), **Where** (Bell Labs), **When** (1979). Also remember C++ is an **extension/superset of C**.

### Common Mistakes
- Writing the developer's name wrongly (it is **Bjarne Stroustrup**, not "Dennis Ritchie" — Dennis Ritchie made **C**).
- Confusing C and C++. **Dennis Ritchie → C** and **Bjarne Stroustrup → C++**.

### Board Question
1. Who developed C++ and in which year? *(1 mark)*
2. Write two features of C++. *(2 marks)*

---

## 1.2 C++ Character Set

### Definition
A **character set** is the **complete group of characters (symbols)** that C++ understands and allows us to use while writing a program.

### Explanation
When we write a program, we use letters, digits, and special symbols. The C++ character set is made up of the following groups:

| Category | Characters Allowed |
|----------|--------------------|
| **Letters** | A to Z (capital), a to z (small) |
| **Digits** | 0 to 9 |
| **Special Symbols** | `+  -  *  /  %  =  <  >  ( )  { }  [ ]  ;  ,  .  "  '  :  ?  !  &  \|  #  @  _` etc. |
| **White Spaces** | Blank space, tab, newline (Enter) |

### Important Points
- C++ is **case-sensitive**, so `A` and `a` are treated as **different** characters.
- White spaces (blank, tab, newline) are used to separate words but are ignored during execution.
- Every token in a program is built using only these characters.

### Example
In the statement `cout << "Sum = ";`
- **Letters**: c, o, u, t, S, u, m
- **Special symbols**: `<`, `<`, `"`, `=`, `;`
- **White space**: the blank spaces.

### Exam Tip
For a short-answer question, write the **four categories** (Letters, Digits, Special Symbols, White Spaces) with 2–3 examples each.

### Common Mistakes
- Forgetting that C++ is **case-sensitive**.
- Thinking that white space has no importance — it is a valid part of the character set.

### Board Question
1. What is a character set? Write the categories of the C++ character set. *(2 marks)*

---

## 1.3 C++ Tokens

### Definition
A **token** is the **smallest individual unit** (smallest meaningful part) of a C++ program.

### Explanation
Just as words are the smallest units of an English sentence, **tokens are the smallest units of a C++ program**. The compiler reads a program as a series of tokens.

C++ has **five types of tokens**:

| No. | Token | Example |
|-----|-------|---------|
| 1 | **Keywords** | `int`, `float`, `if`, `return` |
| 2 | **Identifiers** | `sum`, `marks`, `total` |
| 3 | **Constants (Literals)** | `10`, `3.14`, `'A'`, `"Hello"` |
| 4 | **Operators** | `+`, `-`, `*`, `/`, `=` |
| 5 | **Punctuators / Special Symbols** | `;`, `{ }`, `( )`, `,` |

### Important Points
- Tokens are the building blocks of a program.
- The four most important tokens asked in exams are **Identifiers, Keywords, Constants and Operators**.

### Example
In the statement `int sum = a + b;` the tokens are:
- `int` → keyword
- `sum`, `a`, `b` → identifiers
- `=`, `+` → operators
- `;` → punctuator

### Exam Tip
Learn the **five types of tokens** with one example each — this is a common **2 or 3 mark** question.

### Common Mistakes
- Writing only 3 or 4 types of tokens. Remember there are **five**.

### Board Question
1. What is a token? Name the different types of tokens in C++. *(3 marks)*

---

### 1.3.1 Identifiers

#### Definition
**Identifiers** are the **names given by the programmer** to different parts of a program such as variables, functions, arrays and classes.

#### Explanation
We need names to identify things in a program. For example, if we want to store marks, we may name that memory location `marks`. This name is an identifier.

**Rules for writing identifiers:**
- The first character must be a **letter (A–Z, a–z)** or an **underscore ( _ )**.
- After the first character we may use **letters, digits and underscore**.
- **Blank spaces are not allowed** inside an identifier.
- **Special symbols** like `+`, `-`, `#`, `@` are **not allowed**.
- A **keyword cannot** be used as an identifier.
- C++ is **case-sensitive**, so `Sum`, `sum` and `SUM` are three different identifiers.

#### Important Points

| Valid Identifiers | Invalid Identifiers | Reason it is invalid |
|-------------------|---------------------|----------------------|
| `total` | `2total` | starts with a digit |
| `_marks` | `my marks` | contains a blank space |
| `sum1` | `sum-1` | contains a special symbol `-` |
| `roll_no` | `float` | it is a keyword |

#### Example
```cpp
int marks;      // marks is a valid identifier
float area_of_circle;   // valid
int roll_no;    // valid
```

#### Exam Tip
In the exam, questions often give a list of names and ask **"which are valid identifiers?"** Learn the rules well and always check: **first letter, no space, no special symbol, not a keyword.**

#### Common Mistakes
- Starting a name with a digit (e.g., `1num`).
- Using a space or a special symbol in a name.

#### Board Question
1. What is an identifier? Write the rules for naming an identifier. *(3 marks)*
2. State whether the following are valid identifiers: `net-pay`, `_total`, `9class`, `roll no`. *(2 marks)*

---

### 1.3.2 Keywords

#### Definition
**Keywords** are **reserved words** whose meaning is already known (defined) to the C++ compiler. They cannot be used as identifiers.

#### Explanation
- Keywords have a **special, fixed meaning** in C++.
- They must be written in **lowercase** only.
- We are **not allowed** to change their meaning or use them as variable names.

Some common C++ keywords:

| | | | |
|-----|-----|-----|-----|
| `int` | `float` | `double` | `char` |
| `if` | `else` | `for` | `while` |
| `do` | `switch` | `case` | `break` |
| `return` | `void` | `const` | `long` |
| `signed` | `unsigned` | `class` | `struct` |

#### Important Points
- Keywords are always in **small letters**.
- A keyword can **never** be used as an identifier (variable name).
- Examples: `int` is a keyword, but `Int` is **not** (it becomes an identifier).

#### Example
```cpp
int int;   // WRONG: 'int' is a keyword, cannot be a variable name
int age;   // CORRECT: 'age' is a valid identifier
```

#### Exam Tip
If a question asks "Is `float` a valid identifier?", the answer is **No, because it is a keyword.**

#### Common Mistakes
- Using a keyword as a variable name.
- Writing keywords in capital letters (e.g., `INT`, `FOR`). This causes an error.

#### Board Question
1. What are keywords? Give any four examples. *(2 marks)*
2. Differentiate between a keyword and an identifier. *(2 marks)*

---

### 1.3.3 Constants

#### Definition
A **constant** (also called a **literal**) is a **value that does not change** during the execution of a program.

#### Explanation
A constant is a fixed value. For example, the value `10` is always `10`; we cannot change it. Constants are of different types:

| Type of Constant | Meaning | Example |
|------------------|---------|---------|
| **Integer constant** | whole number without decimal | `10`, `-45`, `0` |
| **Floating point constant** | number with decimal point | `3.14`, `-0.5` |
| **Character constant** | a single character in single quotes | `'A'`, `'5'`, `'#'` |
| **String constant** | group of characters in double quotes | `"Hello"`, `"India"` |

#### Important Points
- A constant's value is **fixed**.
- **Character constant** uses **single quotes** `' '`.
- **String constant** uses **double quotes** `" "`.

#### Example
```cpp
#include<iostream.h>
void main()
{
    cout << 100 << endl;      // integer constant
    cout << 3.14 << endl;     // floating point constant
    cout << 'A' << endl;      // character constant
    cout << "Class XI";       // string constant
}
```

**Output:**
```
100
3.14
A
Class XI
```

#### Exam Tip
Always remember: **single quote = one character**, **double quote = string**. `'A'` and `"A"` are different in C++.

#### Common Mistakes
- Using double quotes for a single character constant or forgetting quotes altogether.

#### Board Question
1. What is a constant? Name the different types of constants in C++. *(3 marks)*

*(Note: Constants are explained in more detail in Chapter 2.)*

---

### 1.3.4 Operators

#### Definition
An **operator** is a **symbol** that tells the compiler to perform a **specific operation** (like addition, comparison, etc.) on data.

#### Explanation
Operators work on values called **operands**. For example, in `a + b`, the symbol `+` is the operator and `a`, `b` are the operands.

Main types of operators in C++:

| Type | Symbols | Use |
|------|---------|-----|
| **Arithmetic** | `+ - * / %` | calculations |
| **Relational** | `< > <= >= == !=` | comparison |
| **Logical** | `&& \|\| !` | combine conditions |
| **Assignment** | `=` | store a value |
| **Increment/Decrement** | `++  --` | add/subtract 1 |

#### Important Points
- Operators need **operands** (data) to work on.
- Operators are explained fully in **Chapter 3**.

#### Example
```cpp
int a = 10, b = 3;
cout << a + b;   // + is the operator, answer = 13
```
**Output:** `13`

#### Exam Tip
For a short answer, name the operator types with one symbol each.

#### Common Mistakes
- Confusing `=` (assignment) with `==` (comparison).

#### Board Question
1. What is an operator? Name the different types of operators. *(2 marks)*

---

## 1.4 Structure of a C++ Program

### Definition
The **structure of a C++ program** means the **standard order/arrangement of parts** that every C++ program should follow.

### Explanation
A basic C++ program has the following parts:

```cpp
#include<iostream.h>      // (1) Preprocessor / Header file
                          // (2) Documentation section (comments)
void main()               // (3) main() function
{
    // (4) Statements / body of the program
    cout << "Hello";
}
```

The important parts are:

| Part | Purpose |
|------|---------|
| **Header file** (`#include`) | tells the compiler which library functions to include (e.g., `cout`, `cin`). |
| **`main()` function** | the starting point of every C++ program. Execution always begins here. |
| **Braces `{ }`** | mark the beginning and end of the program body. |
| **Statements** | actual instructions, each ending with a semicolon `;`. |
| **Comments** | notes for humans; ignored by the compiler. |

### Important Points
- Every program **must have `main()`**.
- Execution **always starts from `main()`**.
- Each statement ends with a **semicolon `;`**.

### Example
```cpp
#include<iostream.h>
void main()
{
    cout << "This is my first program";
}
```
**Output:**
```
This is my first program
```

### Exam Tip
A very common **long question** is "Explain the structure of a C++ program with an example." Draw the parts clearly and label the header file, `main()`, braces and statements.

### Common Mistakes
- Forgetting the semicolon `;` at the end of a statement.
- Forgetting the header file `#include<iostream.h>`.
- Writing `Main()` or `MAIN()` instead of `main()`.

### Board Question
1. Explain the general structure of a C++ program with a suitable example. *(5 marks)*

---

### 1.4.1 Header Files

#### Definition
A **header file** is a **file that contains predefined functions and declarations** which we can use in our program by including it with `#include`.

#### Explanation
- Header files are added at the **top of the program**.
- They are included using the **preprocessor directive** `#include`.
- For example, to use `cout` and `cin`, we include `#include<iostream.h>`.

#### Important Points
- `#include` line does **not** end with a semicolon.
- The name of the header file is written inside **angle brackets** `< >`.

#### Example
```cpp
#include<iostream.h>   // for cout and cin
#include<iomanip.h>    // for setw()
```

#### Exam Tip
Remember: **iostream.h → for input/output (cin, cout)**; **iomanip.h → for setw() (formatting)**.

#### Common Mistakes
- Adding a semicolon after `#include<iostream.h>`.
- Forgetting to include the correct header file for a function.

#### Board Question
1. What is a header file? Give two examples. *(2 marks)*

---

### 1.4.2 main() Function

#### Definition
`main()` is the **special function from where the execution of every C++ program begins**.

#### Explanation
- Every C++ program must contain **exactly one `main()`** function.
- The **body of `main()`** is written between curly braces `{ }`.
- In old C++ (Turbo C++), it is written as `void main()`.

#### Important Points
- Execution **always starts from `main()`**.
- `main()` is written in **lowercase**.
- The statements inside `{ }` form the body of the program.

#### Example
```cpp
#include<iostream.h>
void main()
{
    cout << "Execution starts from main()";
}
```
**Output:**
```
Execution starts from main()
```

#### Exam Tip
A 1-mark question may ask: **"From where does execution of a C++ program begin?"** Answer: **from the `main()` function.**

#### Common Mistakes
- Writing `main` without `()`.
- Using more than one `main()` in a program.

#### Board Question
1. What is the role of the `main()` function in a C++ program? *(2 marks)*

---

## 1.5 Header Files : iostream.h and iomanip.h

### Definition
- **iostream.h** → header file for **input and output** operations (contains `cin`, `cout`).
- **iomanip.h** → header file for **input/output manipulation/formatting** (contains `setw()`).

### Explanation

| Header File | Full form idea | Used for | Contains |
|-------------|----------------|----------|----------|
| `iostream.h` | **i**nput-**o**utput **stream** | reading input and showing output | `cin`, `cout`, `<<`, `>>`, `endl` |
| `iomanip.h` | **i**nput-**o**utput **manip**ulation | formatting the output | `setw()`, `setprecision()` |

### Important Points
- To use `cout` / `cin`, we **must include `iostream.h`**.
- To use `setw()`, we **must include `iomanip.h`**.

### Example
```cpp
#include<iostream.h>
#include<iomanip.h>
void main()
{
    cout << setw(10) << "Name";
}
```
**Output:**
```
      Name
```
(The word `Name` is printed in a field of 10 spaces, so it is shifted to the right.)

### Exam Tip
Match the header file with its function: **cout/cin → iostream.h**, **setw() → iomanip.h**.

### Common Mistakes
- Using `setw()` without including `iomanip.h`.

### Board Question
1. Write the use of `iostream.h` and `iomanip.h`. *(2 marks)*

---

## 1.6 cout (Output Statement)

### Definition
`cout` is the **standard output object** used to **display (print) output on the screen (monitor)**.

### Explanation
- `cout` is read as **"see-out"** (console output).
- It is used with the **insertion operator `<<`**.
- It sends data to the output device (screen).

### Important Points
- `cout` is defined in **`iostream.h`**.
- It uses the **`<<` (insertion) operator**.
- Text (string) must be written inside **double quotes**.

### Example
```cpp
#include<iostream.h>
void main()
{
    cout << "Total marks = ";
    cout << 95;
}
```
**Output:**
```
Total marks = 95
```

### Exam Tip
Remember: **cout → output (screen)** and it goes with **`<<`**.

### Common Mistakes
- Using `>>` with `cout` (wrong). `cout` uses `<<`.
- Forgetting double quotes around text.

### Board Question
1. What is `cout`? Which operator is used with it? *(2 marks)*

---

## 1.7 cin (Input Statement)

### Definition
`cin` is the **standard input object** used to **take input (data) from the keyboard**.

### Explanation
- `cin` is read as **"see-in"** (console input).
- It is used with the **extraction operator `>>`**.
- It stores the input value in a variable.

### Important Points
- `cin` is defined in **`iostream.h`**.
- It uses the **`>>` (extraction) operator**.
- Data taken by `cin` is stored in a variable.

### Example
```cpp
#include<iostream.h>
void main()
{
    int age;
    cout << "Enter your age: ";
    cin >> age;
    cout << "Your age is " << age;
}
```
**Sample Output:**
```
Enter your age: 16
Your age is 16
```
(Here `16` is typed by the user.)

### Exam Tip
Remember: **cin → input (keyboard)** and it goes with **`>>`**.

### Common Mistakes
- Using `<<` with `cin` (wrong). `cin` uses `>>`.
- Trying to read into a value that is not a variable.

### Board Question
1. What is `cin`? Which operator is used with it? *(2 marks)*

---

## 1.8 Insertion (<<) and Extraction (>>) Operators

### Definition
- **`<<`** is the **insertion operator**, used with `cout` to **send data to the output (screen)**.
- **`>>`** is the **extraction operator**, used with `cin` to **take data from the keyboard into a variable**.

### Explanation

| Operator | Name | Used with | Direction | Work |
|----------|------|-----------|-----------|------|
| `<<` | Insertion operator | `cout` | data → screen | shows output |
| `>>` | Extraction operator | `cin` | keyboard → variable | takes input |

An easy trick: the arrows point in the direction the data flows.
- `cout <<` → data goes **out** to the screen.
- `cin >>` → data comes **in** to the variable.

### Important Points
- `<<` always goes with **`cout`**.
- `>>` always goes with **`cin`**.

### Example
```cpp
#include<iostream.h>
void main()
{
    int n;
    cin >> n;            // >> takes input
    cout << "You typed " << n;   // << shows output
}
```
**Sample Output:**
```
7
You typed 7
```

### Exam Tip
Never mix them up: **cout << (out)** and **cin >> (in)**.

### Common Mistakes
- Writing `cin << n;` or `cout >> "hi";` — both are wrong.

### Board Question
1. Differentiate between the insertion operator and the extraction operator. *(2 marks)*

---

## 1.9 endl (End Line Manipulator)

### Definition
`endl` is a **manipulator** used with `cout` to **move the cursor to the next (new) line**.

### Explanation
- `endl` means **"end line"**.
- After `endl`, the next output starts on a **new line**.
- It works almost the same as the escape sequence `\n`.

### Important Points
- `endl` is used with **`cout`** and the **`<<`** operator.
- It is defined in **`iostream.h`**.

### Example
```cpp
#include<iostream.h>
void main()
{
    cout << "Line 1" << endl;
    cout << "Line 2";
}
```
**Output:**
```
Line 1
Line 2
```

### Exam Tip
`endl` and `\n` both move the cursor to a new line. `endl` is a manipulator; `\n` is an escape sequence.

### Common Mistakes
- Writing `endl` inside double quotes like `"endl"` — then it is printed as text, not used as a new line.

### Board Question
1. What is the use of `endl`? *(1 mark)*

---

## 1.10 setw() Manipulator

### Definition
`setw()` (set width) is a **manipulator** used to **set the minimum number of columns (field width)** for the next output value.

### Explanation
- `setw(n)` reserves **`n` spaces** for the value that comes after it.
- If the value has fewer characters, it is **shifted to the right** (right-justified) and extra spaces are added on the left.
- It is defined in **`iomanip.h`**.

### Important Points
- Must include **`iomanip.h`** to use `setw()`.
- It affects **only the next value** printed.
- Very useful for printing data in neat **columns/tables**.

### Example
```cpp
#include<iostream.h>
#include<iomanip.h>
void main()
{
    cout << setw(6) << 5 << endl;
    cout << setw(6) << 100 << endl;
}
```
**Output:**
```
     5
   100
```
(Each number is printed in a width of 6 columns, aligned to the right.)

### Exam Tip
Remember `setw()` needs **`iomanip.h`** and affects **only the very next value**.

### Common Mistakes
- Thinking `setw()` affects all following outputs — it applies to only the next item.
- Forgetting to include `iomanip.h`.

### Board Question
1. What is the use of `setw()` manipulator? Give an example. *(2 marks)*

---

## 1.11 Cascading of I/O Operators

### Definition
**Cascading of I/O operators** means **using the `<<` or `>>` operator many times in a single statement** to output or input multiple values.

### Explanation
- Instead of writing many `cout` or `cin` statements, we can join them using `<<` or `>>` repeatedly.
- "Cascading" means one after another (like a waterfall).

### Important Points
- Cascading of **`<<`** is used with **`cout`** (multiple outputs).
- Cascading of **`>>`** is used with **`cin`** (multiple inputs).
- It makes the program **shorter and easier to read**.

### Example
```cpp
#include<iostream.h>
void main()
{
    int a, b;
    cout << "Enter two numbers: ";
    cin >> a >> b;                       // cascading of >>
    cout << "Sum = " << a + b << endl;   // cascading of <<
}
```
**Sample Output:**
```
Enter two numbers: 4 6
Sum = 10
```

### Exam Tip
Cascading = **repeated use of `<<` or `>>`** in one statement. Give one `cout` and one `cin` example.

### Common Mistakes
- Mixing `<<` and `>>` in the same statement wrongly.

### Board Question
1. What is meant by cascading of I/O operators? Give an example. *(2 marks)*

---

## 1.12 Editor, Compilation, Linking and Execution

Before the computer can run a C++ program, it goes through several stages. Understanding these stages is important.

---

### 1.12.1 Editor

#### Definition
An **editor** is a **program used to type, write and save** the source code of a program.

#### Explanation
- We write our C++ program (source code) in an editor.
- The saved file is called the **source file** and has the extension **`.cpp`**.
- Example: Turbo C++ editor, Notepad, VS Code, etc.

#### Important Points
- Source code is written in the editor.
- Source file extension = **`.cpp`**.

#### Exam Tip
Editor is used **only to type and save** the program, not to run it.

#### Common Mistakes
- Confusing an editor with a compiler.

---

### 1.12.2 Compilation

#### Definition
**Compilation** is the process of **converting the source code (`.cpp`) into object code (machine code)** using a program called a **compiler**.

#### Explanation
- The **compiler** reads the whole program and translates it into **object code** (`.obj`).
- If there are mistakes (errors), the compiler shows **error messages** and does not create object code.

#### Important Points
- Done by the **compiler**.
- Source code (`.cpp`) → Object code (`.obj`).
- It checks for **syntax errors**.

#### Exam Tip
Remember: **Compiler converts source code into object code.**

#### Common Mistakes
- Thinking compilation runs the program. It only translates it.

---

### 1.12.3 Linking

#### Definition
**Linking** is the process of **joining the object code with library functions** (from header files) to create an **executable file (`.exe`)**.

#### Explanation
- The **linker** combines our object code with the code of predefined functions (like `cout`, `cin`).
- The result is an **executable file** (`.exe`) that the computer can run.

#### Important Points
- Done by the **linker**.
- Object code (`.obj`) + Library → Executable file (`.exe`).

#### Exam Tip
Remember: **Linker joins object code with library files to make the `.exe` file.**

#### Common Mistakes
- Confusing the linker with the compiler.

---

### 1.12.4 Execution

#### Definition
**Execution** means **running the executable file (`.exe`)** so that the computer performs the instructions and produces the **output**.

#### Explanation
- When we **run** the program, the executable file is loaded into memory and the instructions are carried out step by step.
- The result is shown as **output** on the screen.

#### Important Points
- Execution runs the **`.exe`** file.
- The output is produced at this stage.

#### Exam Tip
Order to remember (very common question):
**Editor → Compilation → Linking → Execution.**

#### Common Mistakes
- Mixing up the order of stages.

#### Board Question (for the whole process)
1. Explain the steps involved in the execution of a C++ program (Editor, Compilation, Linking, Execution). *(5 marks)*

**Summary Table:**

| Stage | Tool Used | Input | Output |
|-------|-----------|-------|--------|
| Editing | Editor | typing | Source file (`.cpp`) |
| Compilation | Compiler | `.cpp` | Object file (`.obj`) |
| Linking | Linker | `.obj` + library | Executable file (`.exe`) |
| Execution | Loader/OS | `.exe` | Output on screen |

---

## 1.13 Error Messages

### Definition
An **error message** is a **message shown by the compiler** when there is a **mistake in the program** that stops it from compiling or running correctly.

### Explanation
Errors are mainly of the following types:

| Type of Error | Meaning | Example |
|---------------|---------|---------|
| **Syntax Error** | breaking the grammar rules of C++ | missing `;`, missing `}` |
| **Logical Error** | program runs but gives wrong output | using `+` instead of `*` |
| **Run-time Error** | error while the program is running | division by zero |

There are also **warnings**, which are not errors but suggestions. The program may still run with warnings.

### Important Points
- **Syntax errors** are found by the **compiler**.
- **Logical errors** are the hardest to find because there is **no error message** — only wrong output.
- **Run-time errors** happen **while running** the program.

### Example
```cpp
#include<iostream.h>
void main()
{
    cout << "Hello"    // ERROR: missing semicolon ;
}
```
The compiler will show a **syntax error** like: *"Statement missing ;"*

### Exam Tip
Learn the **three types of errors** with one example each. Note that a **logical error gives no message**.

### Common Mistakes
- Thinking that if a program compiles successfully, it is always correct. It may still have **logical errors**.

### Board Question
1. What are the different types of errors in C++? Explain with examples. *(3 marks)*

---
---

# CHAPTER 2 : DATA TYPES, VARIABLES AND CONSTANTS

---

## 2.1 Concept of Data Types

### Definition
A **data type** tells us the **type of data** a variable can store and **how much memory** it will use.

### Explanation
- In real life we deal with different kinds of data — numbers, decimals, letters, etc.
- Data types tell the computer **what kind of value** will be stored and **how much space** to reserve in memory.
- Example: an `int` stores whole numbers, a `char` stores a single character.

Data types in C++ are broadly divided into:

| Category | Examples |
|----------|----------|
| **Built-in (Fundamental) data types** | `char`, `int`, `float`, `double`, `void` |
| **Derived data types** | array, pointer, function |
| **User-defined data types** | structure, class, union, enum |

### Important Points
- Data type decides **memory size** and **kind of value**.
- The most common built-in types are **char, int, float, double**.

### Example
```cpp
int marks = 90;     // stores whole number
float price = 45.5; // stores decimal number
char grade = 'A';   // stores single character
```

### Exam Tip
Remember the three categories: **Built-in, Derived, User-defined.**

### Common Mistakes
- Storing a decimal value in an `int` variable (the decimal part is lost).

### Board Question
1. What is a data type? Write the different categories of data types in C++. *(3 marks)*

---

## 2.2 Built-in Data Types

### Definition
**Built-in (fundamental) data types** are the **basic data types provided by the C++ language itself**.

### Explanation
The four main built-in data types are:

| Data Type | Meaning | Memory Size (Turbo C++) | Example |
|-----------|---------|--------------------------|---------|
| **char** | single character | 1 byte | `'A'`, `'z'`, `'5'` |
| **int** | whole numbers | 2 bytes | `10`, `-45` |
| **float** | decimal numbers (single precision) | 4 bytes | `3.14`, `-0.5` |
| **double** | decimal numbers (double precision) | 8 bytes | `3.141592`, `12345.678` |

> **Note:** Memory sizes are as per Turbo C++ (16-bit). In modern compilers `int` is usually 4 bytes.

#### char
- Stores a **single character** enclosed in single quotes.
- Uses **1 byte** of memory.

#### int
- Stores **whole numbers** (no decimal part).
- Uses **2 bytes** (Turbo C++).

#### float
- Stores **decimal (real) numbers** with about **6–7 digits** of precision.
- Uses **4 bytes**.

#### double
- Stores **decimal numbers** with **more precision** (about 15 digits).
- Uses **8 bytes**.

### Important Points
- `char` = 1 byte, `int` = 2 bytes, `float` = 4 bytes, `double` = 8 bytes (Turbo C++).
- `double` is **more accurate** than `float`.

### Example
```cpp
#include<iostream.h>
void main()
{
    char grade = 'A';
    int age = 16;
    float marks = 87.5;
    double pi = 3.14159265;

    cout << "Grade: " << grade << endl;
    cout << "Age: " << age << endl;
    cout << "Marks: " << marks << endl;
    cout << "Pi: " << pi << endl;
}
```
**Output:**
```
Grade: A
Age: 16
Marks: 87.5
Pi: 3.14159
```

### Exam Tip
Memorise the **memory sizes** — a very common **1 or 2 mark** question is "Write the size of int/float/char/double."

### Common Mistakes
- Mixing up the sizes of `float` (4 bytes) and `double` (8 bytes).

### Board Question
1. Write any four built-in data types with their memory size. *(2 marks)*
2. Differentiate between `float` and `double`. *(2 marks)*

---

## 2.3 Constants (in Detail)

### Definition
A **constant** is a **value that cannot be changed** during the execution of the program.

### Explanation
There are four main types of constants:

---

#### 2.3.1 Integer Constant
- A **whole number** without any decimal point.
- Can be positive or negative.
- **No comma, no decimal, no space** is allowed.
- Examples: `10`, `-56`, `0`, `1000`

#### 2.3.2 Character Constant
- A **single character** enclosed in **single quotes** `' '`.
- Examples: `'A'`, `'z'`, `'7'`, `'$'`

#### 2.3.3 Floating Point Constant
- A **real number** with a **decimal point**.
- Examples: `3.14`, `-0.5`, `100.0`

#### 2.3.4 String Constant
- A **group of characters** enclosed in **double quotes** `" "`.
- Examples: `"Hello"`, `"Class XI"`, `"A"`

### Important Points

| Constant | Quotes Used | Example |
|----------|-------------|---------|
| Integer | none | `25` |
| Floating point | none | `2.5` |
| Character | single `' '` | `'B'` |
| String | double `" "` | `"Book"` |

- `'A'` (character) and `"A"` (string) are **different**.

### Example
```cpp
#include<iostream.h>
void main()
{
    cout << 50 << endl;       // integer constant
    cout << 3.75 << endl;     // floating point constant
    cout << 'X' << endl;      // character constant
    cout << "Assam" << endl;  // string constant
}
```
**Output:**
```
50
3.75
X
Assam
```

### Exam Tip
Remember the **quotes rule**: single quotes → character, double quotes → string, no quotes → number.

### Common Mistakes
- Using double quotes for a single character.
- Putting a comma in an integer constant like `1,000` (wrong).

### Board Question
1. Explain the different types of constants in C++ with examples. *(4 marks)*

---

## 2.4 Escape Sequences

### Definition
An **escape sequence** is a **special set of characters starting with a backslash `\`** that is used to perform a special task (like moving to a new line).

### Explanation
- Escape sequences are written inside quotes.
- Even though they are made of **two characters** (`\` + a letter), they are treated as **one character**.

Common escape sequences:

| Escape Sequence | Name | Work |
|-----------------|------|------|
| `\n` | New line | moves cursor to the next line |
| `\t` | Horizontal tab | gives a tab space (gap) |
| `\b` | Backspace | moves cursor one step back |
| `\\` | Backslash | prints a backslash `\` |
| `\"` | Double quote | prints a double quote `"` |
| `\0` | Null character | marks end of a string |

#### \n (New line)
- Moves the cursor to the **beginning of the next line**.

#### \t (Tab)
- Inserts a **horizontal tab space** (about 8 columns).

#### \b (Backspace)
- Moves the cursor **one position to the left**.

### Important Points
- All escape sequences start with a **backslash `\`**.
- `\n` works like `endl`.

### Example
```cpp
#include<iostream.h>
void main()
{
    cout << "Name\tClass\n";
    cout << "Ravi\t11\n";
}
```
**Output:**
```
Name    Class
Ravi    11
```
(`\t` gives the gap between columns and `\n` moves to the next line.)

### Exam Tip
The three most asked escape sequences are **`\n` (new line), `\t` (tab), `\b` (backspace)**. Learn what each one does.

### Common Mistakes
- Using a forward slash `/n` instead of a backslash `\n`.

### Board Question
1. What is an escape sequence? Explain `\n`, `\t` and `\b` with examples. *(3 marks)*

---

## 2.5 const Keyword

### Definition
The **`const` keyword** is used to declare a **constant variable** whose value **cannot be changed** after it is given once.

### Explanation
- `const` makes a variable **read-only**.
- We must give the value at the time of declaration.
- If we try to change it later, the compiler shows an **error**.

**Syntax:**
```cpp
const data_type name = value;
```

### Important Points
- A `const` variable **must be initialized** when declared.
- Its value **cannot be modified** later.
- It is often used for fixed values like `pi = 3.14`.

### Example
```cpp
#include<iostream.h>
void main()
{
    const float PI = 3.14;
    float r = 5, area;
    area = PI * r * r;
    cout << "Area of circle = " << area;
    // PI = 3.15;   // ERROR: cannot change a const value
}
```
**Output:**
```
Area of circle = 78.5
```

### Exam Tip
`const` = fixed value that cannot change. It must be given a value at the time of declaration.

### Common Mistakes
- Declaring a `const` without giving it a value.
- Trying to change a `const` value later in the program.

### Board Question
1. What is the use of the `const` keyword? Give an example. *(2 marks)*

---

## 2.6 Variables

### Definition
A **variable** is a **named memory location** whose value **can be changed** during the execution of the program.

### Explanation
- A variable is like a **container (box)** that stores a value.
- The **name** of the box is the identifier; the **value** inside it can change.
- Each variable has a **data type**.

### Important Points
- A variable name must follow the rules of an **identifier**.
- The value of a variable **can be changed** any number of times.
- A variable must be **declared before use**.

### Example
```cpp
int marks;     // marks is a variable
marks = 80;    // value 80 stored
marks = 95;    // value changed to 95
```

### Exam Tip
Difference to remember: **A variable can change; a constant cannot.**

### Common Mistakes
- Using a variable without declaring it first.

### Board Question
1. What is a variable? How is it different from a constant? *(2 marks)*

---

## 2.7 Variable Declaration

### Definition
**Variable declaration** is the process of **telling the compiler the name and data type** of a variable before using it.

### Explanation
**Syntax:**
```cpp
data_type variable_name;
```
- We can declare **more than one variable** of the same type in one line, separated by commas.

### Important Points
- Declaration reserves memory for the variable.
- Multiple variables of the same type can be declared together.
- Every declaration ends with a **semicolon `;`**.

### Example
```cpp
int a;              // single variable
int x, y, z;        // multiple variables of same type
float price, tax;   // two float variables
char grade;         // one char variable
```

### Exam Tip
Syntax is important: **data_type name;** Learn to declare multiple variables in one line.

### Common Mistakes
- Forgetting to write the data type.
- Forgetting the semicolon.

### Board Question
1. What is variable declaration? Give an example. *(2 marks)*

---

## 2.8 Variable Initialization

### Definition
**Variable initialization** means **giving a value to a variable at the time of its declaration**.

### Explanation
- Declaration + giving value together = initialization.
- **Syntax:**
```cpp
data_type name = value;
```

### Important Points
- Initialization is done **at the time of declaration**.
- If a variable is not initialized, it may contain a **garbage (unknown) value**.

### Example
```cpp
int age = 16;        // declaration + initialization
float pi = 3.14;
char grade = 'A';
```

### Exam Tip
**Declaration** = only reserving memory (`int a;`). **Initialization** = giving a value while declaring (`int a = 5;`).

### Common Mistakes
- Confusing declaration with initialization.
- Using an uninitialized variable and getting garbage values.

### Board Question
1. What is variable initialization? How is it different from declaration? *(2 marks)*

---

## 2.9 Assignment Statement

### Definition
An **assignment statement** uses the **assignment operator `=`** to **store a value in a variable**.

### Explanation
- The `=` operator takes the value on the **right side** and stores it in the variable on the **left side**.
- **Syntax:**
```cpp
variable = value;
```

### Important Points
- `=` is the **assignment operator** (not "equal to").
- The **left side must be a variable**.
- We can also assign the result of an expression: `sum = a + b;`

### Example
```cpp
#include<iostream.h>
void main()
{
    int a, b, sum;
    a = 10;          // assignment
    b = 20;          // assignment
    sum = a + b;     // assignment of an expression
    cout << "Sum = " << sum;
}
```
**Output:**
```
Sum = 30
```

### Exam Tip
`=` means **assignment (store)**, while `==` means **comparison (is equal to)**. Do not confuse the two.

### Common Mistakes
- Writing the value on the left side, like `10 = a;` (wrong).
- Using `==` in place of `=`.

### Board Question
1. What is an assignment statement? Give an example. *(2 marks)*

---

## 2.10 Type Modifiers

### Definition
**Type modifiers** are **keywords used with basic data types to change their size or range** of values.

### Explanation
The main type modifiers are:

| Modifier | Meaning |
|----------|---------|
| **signed** | can store both **positive and negative** values (default) |
| **unsigned** | can store **only positive** values (0 and above) |
| **long** | increases the **size/range** to store bigger values |

#### signed
- Allows both **negative and positive** numbers.
- Example: `signed int x = -50;`

#### unsigned
- Allows **only positive** numbers (and zero), so the positive range becomes larger.
- Example: `unsigned int y = 60000;`

#### long
- Used to **increase the memory size** so that **larger numbers** can be stored.
- Example: `long int population = 1000000;`

### Important Points

| Type | Size (Turbo C++) | Range (approx.) |
|------|------------------|-----------------|
| `int` | 2 bytes | −32768 to 32767 |
| `unsigned int` | 2 bytes | 0 to 65535 |
| `long int` | 4 bytes | very large range |

- `unsigned` cannot store negative values.
- `long` stores bigger numbers by using more memory.

### Example
```cpp
#include<iostream.h>
void main()
{
    unsigned int marks = 500;
    long int distance = 1500000;
    signed int temp = -25;

    cout << marks << endl;
    cout << distance << endl;
    cout << temp << endl;
}
```
**Output:**
```
500
1500000
-25
```

### Exam Tip
Remember: **unsigned → only positive (bigger positive range)**, **long → bigger size (bigger numbers)**, **signed → both + and − (default)**.

### Common Mistakes
- Storing a negative value in an `unsigned` variable (gives a wrong/very large result).

### Board Question
1. What are type modifiers? Explain `signed`, `unsigned` and `long`. *(3 marks)*

---
---

# CHAPTER 3 : OPERATORS AND EXPRESSIONS

---

## 3.1 Arithmetic Operators

### Definition
**Arithmetic operators** are operators used to perform **basic mathematical calculations** like addition, subtraction, multiplication and division.

### Explanation

| Operator | Meaning | Example (`a=10, b=3`) | Result |
|----------|---------|------------------------|--------|
| `+` | Addition | `a + b` | 13 |
| `-` | Subtraction | `a - b` | 7 |
| `*` | Multiplication | `a * b` | 30 |
| `/` | Division (quotient) | `a / b` | 3 |
| `%` | Modulus (remainder) | `a % b` | 1 |

- The **`/` operator** gives the **quotient**. With two integers, the decimal part is dropped (`10/3 = 3`).
- The **`%` operator** gives the **remainder**. It works **only with integers**.

### Important Points
- `%` (modulus) **cannot be used with float or double**.
- `10 / 3` gives `3` (integer division), but `10.0 / 3` gives `3.33...`.

### Example
```cpp
#include<iostream.h>
void main()
{
    int a = 10, b = 3;
    cout << "Sum = " << a + b << endl;
    cout << "Difference = " << a - b << endl;
    cout << "Product = " << a * b << endl;
    cout << "Quotient = " << a / b << endl;
    cout << "Remainder = " << a % b << endl;
}
```
**Output:**
```
Sum = 13
Difference = 7
Product = 30
Quotient = 3
Remainder = 1
```

### Exam Tip
Remember: **`%` gives remainder and works only on integers.** Integer division drops the decimal part.

### Common Mistakes
- Using `%` with `float`/`double` values (error).
- Expecting `5 / 2` to give `2.5` — it gives `2` because both are integers.

### Board Question
1. What are arithmetic operators? Explain with examples. *(3 marks)*

---

## 3.2 Unary Operator

### Definition
A **unary operator** is an operator that works on **only one operand (one value)**.

### Explanation
- Most operators (like `+`, `-`, `*`) need **two** operands and are called **binary operators**.
- A **unary operator** needs **only one** operand.
- Examples of unary operators: **unary minus `-`**, **increment `++`**, **decrement `--`**.

The **unary minus** changes the sign of a value:
- `-a` gives the negative of `a`.

### Important Points
- Unary operator → **one operand**.
- Common unary operators: `-` (unary minus), `++`, `--`.

### Example
```cpp
#include<iostream.h>
void main()
{
    int a = 5;
    int b = -a;      // unary minus
    cout << "b = " << b;
}
```
**Output:**
```
b = -5
```

### Exam Tip
Unary = **one** operand; Binary = **two** operands. Give `++`, `--`, unary `-` as examples of unary operators.

### Common Mistakes
- Thinking every `-` is subtraction. In `-a`, the `-` is a **unary** operator.

### Board Question
1. What is a unary operator? Give examples. *(2 marks)*

---

## 3.3 Increment Operator (++)

### Definition
The **increment operator `++`** is a unary operator that **increases the value of a variable by 1**.

### Explanation
There are two forms:

| Form | Name | Meaning |
|------|------|---------|
| `++a` | **Pre-increment** | first increase, then use the value |
| `a++` | **Post-increment** | first use the value, then increase |

- `a++` and `++a` both increase `a` by 1, but the **timing** is different when used inside another statement.

### Important Points
- `++` adds **1** to the variable.
- **Pre-increment** (`++a`): value increases first.
- **Post-increment** (`a++`): value is used first, then increases.

### Example
```cpp
#include<iostream.h>
void main()
{
    int a = 5, b;
    b = ++a;    // pre-increment: a becomes 6, then b = 6
    cout << "a = " << a << " b = " << b << endl;

    int x = 5, y;
    y = x++;    // post-increment: y = 5, then x becomes 6
    cout << "x = " << x << " y = " << y;
}
```
**Output:**
```
a = 6 b = 6
x = 6 y = 5
```

### Exam Tip
Learn the difference between **pre-increment (`++a`)** and **post-increment (`a++`)** with an example — this is a favourite exam question.

### Common Mistakes
- Thinking `a++` and `++a` give the same result inside an assignment. They differ.

### Board Question
1. Differentiate between pre-increment and post-increment with an example. *(3 marks)*

---

## 3.4 Decrement Operator (--)

### Definition
The **decrement operator `--`** is a unary operator that **decreases the value of a variable by 1**.

### Explanation
Like `++`, the `--` operator also has two forms:

| Form | Name | Meaning |
|------|------|---------|
| `--a` | **Pre-decrement** | first decrease, then use the value |
| `a--` | **Post-decrement** | first use the value, then decrease |

### Important Points
- `--` subtracts **1** from the variable.
- **Pre-decrement** (`--a`): value decreases first.
- **Post-decrement** (`a--`): value is used first, then decreases.

### Example
```cpp
#include<iostream.h>
void main()
{
    int a = 5, b;
    b = --a;    // pre-decrement: a becomes 4, then b = 4
    cout << "a = " << a << " b = " << b << endl;

    int x = 5, y;
    y = x--;    // post-decrement: y = 5, then x becomes 4
    cout << "x = " << x << " y = " << y;
}
```
**Output:**
```
a = 4 b = 4
x = 4 y = 5
```

### Exam Tip
`--` works just like `++`, but it subtracts 1. Remember pre vs post rules.

### Common Mistakes
- Confusing pre-decrement with post-decrement.

### Board Question
1. What is the decrement operator? Explain pre-decrement and post-decrement. *(3 marks)*

---

## 3.5 Relational Operators

### Definition
**Relational operators** are used to **compare two values**. The result is always **true (1) or false (0)**.

### Explanation

| Operator | Meaning | Example (`a=10, b=5`) | Result |
|----------|---------|------------------------|--------|
| `<` | less than | `a < b` | false (0) |
| `>` | greater than | `a > b` | true (1) |
| `<=` | less than or equal to | `a <= b` | false (0) |
| `>=` | greater than or equal to | `a >= b` | true (1) |
| `==` | equal to | `a == b` | false (0) |
| `!=` | not equal to | `a != b` | true (1) |

### Important Points
- Result is always **1 (true)** or **0 (false)**.
- `==` is used for comparison, **not** `=`.
- Mostly used in decision-making (`if`, `while`).

### Example
```cpp
#include<iostream.h>
void main()
{
    int a = 10, b = 5;
    cout << (a > b) << endl;   // true -> 1
    cout << (a == b) << endl;  // false -> 0
}
```
**Output:**
```
1
0
```

### Exam Tip
Remember **`==` (double equal)** is "is equal to", and it is different from `=` (assignment).

### Common Mistakes
- Using `=` instead of `==` for comparison.

### Board Question
1. What are relational operators? List all relational operators with their meaning. *(3 marks)*

---

## 3.6 Logical Operators

### Definition
**Logical operators** are used to **combine two or more conditions** and give a result of **true (1) or false (0)**.

### Explanation

| Operator | Name | Meaning |
|----------|------|---------|
| `&&` | Logical AND | true only if **both** conditions are true |
| `\|\|` | Logical OR | true if **at least one** condition is true |
| `!` | Logical NOT | **reverses** the result (true ↔ false) |

**Truth idea:**
- `(a > 5) && (b > 5)` → true only if **both** are true.
- `(a > 5) || (b > 5)` → true if **any one** is true.
- `!(a > 5)` → true if `a > 5` is false.

### Important Points
- `&&` (AND): both true → true.
- `||` (OR): any one true → true.
- `!` (NOT): reverses the value.

### Example
```cpp
#include<iostream.h>
void main()
{
    int age = 20;
    if(age > 18 && age < 60)
        cout << "Eligible";
    else
        cout << "Not eligible";
}
```
**Output:**
```
Eligible
```

### Exam Tip
Learn the three logical operators (`&&`, `||`, `!`) and one rule each: AND → both true, OR → any one true, NOT → reverse.

### Common Mistakes
- Writing `&` instead of `&&`, or `|` instead of `||`.

### Board Question
1. What are logical operators? Explain `&&`, `||` and `!` with examples. *(3 marks)*

---

## 3.7 Conditional Operator (?:)

### Definition
The **conditional operator `?:`** is a **short form of the if-else statement**. Because it uses **three operands**, it is also called the **ternary operator**.

### Explanation
**Syntax:**
```cpp
result = (condition) ? value_if_true : value_if_false;
```
- If the **condition is true**, the value **before the colon** is chosen.
- If the **condition is false**, the value **after the colon** is chosen.

### Important Points
- It uses **three operands** (ternary).
- It is a short way to write **if-else**.

### Example
```cpp
#include<iostream.h>
void main()
{
    int a = 10, b = 20, big;
    big = (a > b) ? a : b;      // choose the greater
    cout << "Greater number = " << big;
}
```
**Output:**
```
Greater number = 20
```
(Here `a > b` is false, so `b` (20) is chosen.)

### Exam Tip
`(condition) ? true_value : false_value`. It is the **ternary operator** because it has **three parts**.

### Common Mistakes
- Forgetting the colon `:` between the two values.
- Confusing which value comes for true and which for false.

### Board Question
1. What is the conditional (ternary) operator? Explain with an example. *(3 marks)*

---

## 3.8 Operator Precedence

### Definition
**Operator precedence** is the set of **rules that decides the order** in which operators are evaluated in an expression.

### Explanation
- When an expression has many operators, the one with **higher precedence** is done **first**.
- If two operators have the **same precedence**, we look at **associativity** (usually left to right).

A simplified precedence order (high to low):

| Priority | Operators | Description |
|----------|-----------|-------------|
| 1 (highest) | `()` | brackets |
| 2 | `++`, `--`, `!`, unary `-` | unary operators |
| 3 | `*`, `/`, `%` | multiply, divide, modulus |
| 4 | `+`, `-` | add, subtract |
| 5 | `<`, `<=`, `>`, `>=` | relational |
| 6 | `==`, `!=` | equality |
| 7 | `&&` | logical AND |
| 8 | `\|\|` | logical OR |
| 9 (lowest) | `=` | assignment |

**Easy memory trick (for maths part):** **BODMAS-like** → Brackets first, then `* / %`, then `+ -`.

### Important Points
- **Brackets `()`** always have the **highest** priority.
- `*`, `/`, `%` are done **before** `+`, `-`.
- We can change the order by using **brackets**.

### Example
```cpp
#include<iostream.h>
void main()
{
    int result;
    result = 2 + 3 * 4;      // * first: 3*4=12, then 2+12
    cout << result << endl;

    result = (2 + 3) * 4;    // brackets first: 5*4
    cout << result;
}
```
**Output:**
```
14
20
```

### Exam Tip
**Brackets first, then `* / %`, then `+ -`.** Use brackets to be safe and clear.

### Common Mistakes
- Doing `+` before `*` (wrong). Multiplication has higher priority.

### Board Question
1. What is operator precedence? Evaluate `2 + 3 * 4 - 1`. *(3 marks)*

---

## 3.9 Automatic Type Conversion (Implicit Conversion)

### Definition
**Automatic type conversion** is the process where the **compiler itself changes the data type** of a value during an expression, without the programmer telling it to.

### Explanation
- It is also called **implicit conversion** or **type promotion**.
- When operators work on values of **different types**, the compiler converts the **lower type** to the **higher type** automatically.
- Order (low → high): `char → int → float → double`.

### Important Points
- Done **automatically by the compiler**.
- The **smaller data type** is converted to the **larger data type**.
- No data is lost because a lower type is promoted to a higher type.

### Example
```cpp
#include<iostream.h>
void main()
{
    int a = 5;
    float b = 2.0, result;
    result = a / b;     // int a is converted to float automatically
    cout << "Result = " << result;
}
```
**Output:**
```
Result = 2.5
```
(Here `a` becomes `5.0` automatically, so `5.0 / 2.0 = 2.5`.)

### Exam Tip
Remember the promotion order: **char → int → float → double**. The compiler promotes the smaller type.

### Common Mistakes
- Expecting `5 / 2` to give `2.5`. Both are `int`, so there is **no** automatic conversion; the answer is `2`.

### Board Question
1. What is automatic type conversion? Explain with an example. *(3 marks)*

---

## 3.10 Type Casting (Explicit Conversion)

### Definition
**Type casting** is the process where the **programmer manually (by force) changes** the data type of a value.

### Explanation
- It is also called **explicit conversion**.
- The programmer writes the required type inside brackets.
- **Syntax:**
```cpp
(data_type) value;
```

### Important Points
- Done **by the programmer** (not automatic).
- Useful to get correct results in integer division.
- Example: `(float) 5` becomes `5.0`.

### Example
```cpp
#include<iostream.h>
void main()
{
    int a = 5, b = 2;
    float result;
    result = (float) a / b;    // 'a' forced to float -> 5.0 / 2
    cout << "Result = " << result;
}
```
**Output:**
```
Result = 2.5
```
(Without casting, `a / b` would give `2`.)

### Exam Tip
**Automatic conversion = done by compiler. Type casting = done by programmer using `(type)`.** Learn this difference clearly.

### Common Mistakes
- Forgetting the brackets around the data type.
- Casting after division: `(float)(a / b)` gives `2.0` (division already done in int). Cast **before** dividing: `(float)a / b`.

### Board Question
1. What is type casting? How is it different from automatic type conversion? *(3 marks)*

---

## 3.11 Shorthand Operators (Compound Assignment Operators)

### Definition
**Shorthand operators** are **short forms of writing an arithmetic operation together with an assignment**.

### Explanation
They combine an arithmetic operator with `=`.

| Shorthand | Full Form | Meaning (for `a = 10`) | Result |
|-----------|-----------|-------------------------|--------|
| `a += 5` | `a = a + 5` | add 5 to a | 15 |
| `a -= 5` | `a = a - 5` | subtract 5 from a | 5 |
| `a *= 5` | `a = a * 5` | multiply a by 5 | 50 |
| `a /= 5` | `a = a / 5` | divide a by 5 | 2 |
| `a %= 5` | `a = a % 5` | remainder of a ÷ 5 | 0 |

### Important Points
- Shorthand operators make the code **shorter**.
- `a += 5` is exactly the same as `a = a + 5`.

### Example
```cpp
#include<iostream.h>
void main()
{
    int a = 10;
    a += 5;    cout << a << endl;   // 15
    a -= 3;    cout << a << endl;   // 12
    a *= 2;    cout << a << endl;   // 24
    a /= 4;    cout << a << endl;   // 6
    a %= 4;    cout << a << endl;   // 2
}
```
**Output:**
```
15
12
24
6
2
```

### Exam Tip
Convert shorthand to full form to solve: `a += b` means `a = a + b`. Very common **2 or 3 mark** question.

### Common Mistakes
- Writing the operator in the wrong order, like `a =+ 5` instead of `a += 5`.

### Board Question
1. What are shorthand operators? Write the full form of `a += b` and `a %= b`. *(2 marks)*

---
---

# QUICK REVISION (LAST-MINUTE POINTS)

- **C++** developed by **Bjarne Stroustrup** in **1979** at **Bell Labs**.
- **Tokens (5):** Keywords, Identifiers, Constants, Operators, Punctuators.
- **Execution begins from `main()`**.
- **cout << (output), cin >> (input)**; both need **iostream.h**.
- **setw()** needs **iomanip.h**.
- **endl** and **`\n`** → new line.
- **Data type sizes (Turbo C++):** char = 1, int = 2, float = 4, double = 8 (bytes).
- **Quotes:** `'A'` = character, `"A"` = string.
- **Escape sequences:** `\n` (new line), `\t` (tab), `\b` (backspace).
- **`const`** value cannot be changed.
- **Variable** can change; **constant** cannot.
- **`=`** is assignment; **`==`** is comparison.
- **`%`** gives remainder (integers only).
- **Unary** = 1 operand; **Binary** = 2 operands; **Ternary (`?:`)** = 3 operands.
- **Pre (`++a`)**: change first; **Post (`a++`)**: use first.
- **Precedence:** Brackets → `* / %` → `+ -`.
- **Automatic conversion** = by compiler; **type casting** = by programmer.
- **Stages:** Editor → Compilation → Linking → Execution.
- **Errors:** Syntax, Logical, Run-time.

---

*End of Unit 2 : Introduction to C++*
