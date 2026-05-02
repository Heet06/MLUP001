### Introduction to Data Structures in Python

#### What are Data Structures?
##### Definition:
Data Structures are specialized formats for organizing, processing, retrieving, and storing data efficiently

##### Purpose:
They help manage data for operations like:
- Insertion
- Deletion
- Searching
- Updating

##### Analogy:
Just as a kitchen needs different organizational systems (drawers, shelves, racks), programming needs various data structures to handle information effectively

#### Why use Data Structures?
- Efficiency
	- Determines how quickly you can find, add, or remove data. Searching through an unorganized pile versus a sorted list illustrates this difference dramatically
- Scalability
	- Measures how well your system performs as data grows. Proper data structure ensure your programs continue to run efficiently with increasing amounts of data
- Problem Solving
	- Choosing the right data structure can transform complex problems into manageable ones, making your code more elegant and efficient

#### Python's built-in collection types
Primitives types: int, float, bool, str
Collection types (our focus):
- list
- tuple
- set
- dict
- range
- str (as a sequence)
- array

#### Mutability in python
Mutability determines whether an object's state can be modified after creation:

- Mutable objects can be changed in-place after creation
`my_list = [1, 2, 3]`
`my_list.append(4) # Result: [1, 2, 3, 4]`

- Immutable objects cannot be modified after creation; operations return new objects
`text = "Hello"`
`text += " World" # Result: "Hello World"`

- Understanding mutability helps prevent unexpected behavior and bugs in code

##### Mutable
- list
- set
- dict

##### Immutable
- str
- tuple
- range

#### Strings - definition and characteristics
- Ordered, immutable sequence of characters
- Supports indexing, slicing and iteration
- Written with quotes 'Hello' or "World" or """hello world """

##### Why use Strings?
- Store and display text
- Parse/format data from APIs
- Communicate with users (input/output)

#### Lists
- Ordered mutable collection of items (elements)
- Heterogeneous: Lists can contain elements of different types (integer, strings, other lists, etc)

#### Why use Lists?
- Group related data (names, scores, items)
- Modify easily — add, remove, update elements
- Loop, search, sort with built-in methods
- Support nesting for 2D / matrix-like data
- Flexible I/O - great for user input & file data

#### Tuples
- Ordered, immutable collection of items (elements)
- Heterogeneous

#### Why use Tuples?
- Store & display text
- Parse/format data from files or APIs
- Communicate with users (input/output)

#### Dictionaries
- Mutable, unordered
- Stores data in key-value pairs
- Keys must be unique and immutable
- Values can be any type

#### Why use Dictionaries?
- Fast lookups by key — great for large data
- Map relations (eg., name -> score)
- Store structured data like records/configs
- Count or group items by category

#### Sets
- Unordered, mutable collection
- Only stores unordered and unique items
- Not indexable or sliceable
- Elements can be added or removed

#### Why use Sets?
- Remove duplicates from lists or strings
- Fast membership tests (`x in my_set`)
- Supports set operations (union, intersection, difference)

#### Range
- Immutable, ordered sequence of numbers
- Generates values on demand — memory-efficient
- Not a list, but behaves like one in loops
	Key Parameters:
	start: optional (defaults to 0)
	stop: required (non-inclusive)
	step: optional (interval)

#### Why use Range?
- Looping - ideal for `for` loops
- Index generation - for sequence generation
- Memory efficient - doesn't store all values
- Arithmetic sequences - custom start/stop/step

#### Arrays
- Ordered, mutable, homogeneous collection
- All elements must be of same data type (eg. all integers)
- More efficient than lists for numeric data
- Key parameters (array module
	Typecode: defines the data type ('i' for int, 'f' for float) 
- Initializer: optional iterable to populate the array

#### Why use Arrays?
- Numeric Computation - fast for math-heavy tasks (eg. stats, simulations)
- Memory-efficient - less overhead than lists for large data
- High performance - optimized for speed with homogenous values