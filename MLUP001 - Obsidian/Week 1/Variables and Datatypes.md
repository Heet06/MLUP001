#### Rules for naming variables in python
1.  Variable name can be alpha-numeric
2.  Variable name must start with an alphabet or an underscore
3.  Variable name cannot start with a number
4.  Variable name cannot contain any symbol other than an underscore

#### Naming Conventions
- Camel Case
	- Lower Camel Case:
		- `ageEmp=45`
	- Upper Camel Case:
		- `AgeEmp=45`
- Snake Case
	- `age_emp=45`
	- `Age_emp=45`
- Pascal
	- `AgeEmp=45`

#### Assigning values to multiple variables
- `Physics, Chemistry, Mathematics = 89,90,75`

#### Basic data types
| Name | Description | Values | Representation |
| --- | --- | --- | --- |
| Boolean | represents two values of logic and associated with conditional statements | True or False | bool |
| Integer | positive or negative whole numbers | set of all integers, Z | int |
| Complex | contains real and imaginary part (a+ib) | set of complex numbers | complex |
| Float | real numbers | floating point numbers | float |
| String | all strings or characters enclosed between single or double quotes | sequence of characters | str |
#### Identifying object data type
- Find data type of object using syntax: `type(object)`

 `Employee_name = "Ram"`
 `Age = 55`
 `Height = 150.6`
 `type(Employee_name)` => `str`
 `type(Age)` => `int`
 `type(Height)` => `float`

#### Verifying object data type
- Verify if an object is of certain data type
- syntax: `type(object) is datatype`

 `type(Height) is int` => `False`
 `type(Age) is float` => `False`
 `type(Employee_name) is str` => `True`

#### Type Conversion
- Convert the data type of an object to another
- syntax: `datatype(object)`
- Changes can be stored in same variable or in different variable

`type(Height)` => `float`
`ht = int(Height)`
`type(ht)` => `int`
`Height = int(Height)`
`type(Height)` => `int`

- Only few type conversions are accepted
`EmpSalary = '20000'`
`type(EmpSalary)` => `str`
`EmpSalary = int(EmpSalary)`
`type(EmpSalary)` => `int`
