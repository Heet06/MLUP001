#### Operators and Operands
- An operator are special symbols that help in carrying out an assignment operation or arithmetic or logical computation
- Value that the operator operates on is operand
- `2+3` => `5`

#### Arithmetic operators
- Used to perform mathematical operations between two operands
- Create two variables a and b with values 10 and 5 respectively

`a, b = 10, 5`

| Symbol | Operation      | Example         |
| ------ | -------------- | --------------- |
| +      | Addition       | a+b<br>15       |
| -      | Subtraction    | a-b<br>5        |
| *      | Multiplication | a * b<br>50     |
| /      | Division       | a/b<br>2        |
| %      | Remainder      | a%b<br>0        |
| **     | Exponents      | a ** b<br>10000 |


#### Hierarchy of arithmetic operators
| Decreasing order of precedence | Operation |
| ------------------------------ | --------- |
| Perenthesis                    | ()        |
| **                             | Exponent  |
| Division                       | /         |
| Multiplication                 | *         |
| Addition and Subtraction       | +,-       |

`A = 7 - 2 * (27/3**2) + 4`
`print(A)` => `5`

#### Assignment operators
- Used to assign values to variables

| Symbol | Operation                                                                                  | Example    |
| ------ | ------------------------------------------------------------------------------------------ | ---------- |
| \=     | Assign values from right side operands to left side operand                                | a=10   b=5 |
| +=     | Adds right operand to left operand and stores result on left side operand (a=a+b)          | a+=b<br>15 |
| \-=    | Subtracts right operand from left operand and stores result on left side operand (a=a-b)   | a-=b<br>5  |
| \*=    | Multiplies right operand with left operand and stores result on left side operand (a=a\*b) | a*=b<br>50 |
| /=     | Divides right operand from left operand and stores result on left side operand (a=a/b)     | a/=b<br>2  |

#### Relational or comparison operators
- Tests numerical equalities and inequalities between two operands and returns a boolean value
- All operators have same precedence
- Create two variables x and y with values 5 and 7 respectively

`x, y = 5, 7`

| Symbol | Operation             | Example                |
| ------ | --------------------- | ---------------------- |
| <      | Strictly less than    | print(x<y)<br>True     |
| <=     | Less than equal to    | print(x>=y)<br>False   |
| \>     | Strictly greater than | print(x>y)<br>False    |
| \>=    | Greater than equal to | print(x>=y)<br>False   |
| \==    | Equal to equal to     | print(x == y)<br>False |
| !=     | Not equal to          | print(x!=y)<br>True    |

#### Logical operators
- Used when operands are conditional statements and return boolean value
- In python, logical operators are designed to work with scalars or boolean values 

| Symbol | Operation   | Example                         |
| ------ | ----------- | ------------------------------- |
| or     | Logical OR  | print((x<y) or (x>y))<br>True   |
| and    | Logical AND | print((x<y) and (x>y))<br>False |
| not    | Logical NOT | print(not (x == y))<br>True     |

#### Bitwise operators
- Used when operators are integers
- Integers are treated as string of binary digits
- Operates bit by bit
- Can operate on conditional statements which compare scalar values or arrays
- Bitwise OR(|), AND (&)

- Create two variables x and y with values 5 and 7 respectively

`x, y = 5, 7`

- Binary codes for 5 is 0000 0101 and 7 is 0000 0111
- 0 corresponds to False and 1 corresponds to True
- In bitwise OR(|), operator copies a bit to the result if it exists either operand
- In bitwise AND(&), operator copies a bit to the result if exists in both operands

`print(x|y)` => `7`
`print(x&y)` => `5`

#### Hierarchy of arithmetic operators
| Decreasing order of precendence | Operation             |
| ------------------------------- | --------------------- |
| Perenthesis                     | ()                    |
| \*\*                            | Exponent              |
| Division                        | /                     |
| Multiplication                  | \*                    |
| Addition and Subtraction        | +,-                   |
| Bitwise AND                     | &                     |
| Bitwise OR                      | \|                    |
| Relational/comparison operators | \==, !=, <, <=, >, >= |
| Logical NOT                     | not                   |
| Logical AND                     | and                   |
| Logical OR                      | or                    |
