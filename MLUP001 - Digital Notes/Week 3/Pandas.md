#### Introduction to Pandas
- Provides high-performance, easy-to-use data structures and analysis tools for the Python programming language
- Open-source Python library providing high-performance data manipulation and analysis tool using its powerful data structures
- Name pandas is derived from the word Panel Data — and econometrics terms for multidimensional data

- Pandas deals with dataframes

| Name      | Dimension | Description                                                                                                                        |
| --------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Dataframe | 2         | &bull; two-dimensional size-mutable <br>&bull; potential heterogeneous tabular data structure with labeled axes (rows and columns) |
#### Creating a copy of data
- In Python, there are two ways to create copies
	- Shallow copy
	- Deep copy

|              | Shallow Copy                                                                                                                                                                   | Deep Copy                                                                                                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Function** | `samp = cars_data.copy(deep=False)`<br>`samp = cars_data`                                                                                                                      | `cars_data1 = cars_data.copy(deep=True)`                                                                                                                                                                |
| Description  | &bull; It only creates a new variable that shares the reference of the original object<br>&bull; Any changes made to a copy of object will be reflected in the original object | &bull; In case of a deep copy, a copy of object is copied in other object with no reference to the original<br>&bull; Any changes made to a copy of object will not be reflected in the original object |
#### Attributes of data
- DataFrame.index - to get the index (row labels) of the dataframe
	`cars_data1.index`
- DataFrame.columns - to get the index (column labels) of the dataframe
	`cars_data1.columns`
- DataFrame.size - to get the total number of elements from the dataframe
	`cars_data1.size`
- DataFrame.shape - to get the dimensionality of the dataframe.
	`cars_data1.shape`
- DataFrame.memory_usage([index, deep]) - The memory usage of each column in bytes
	`cars_data1.memory_usage()`
- DataFrame.ndim: The number of axes / array dimensions
	`cars_data1.ndim`

#### Indexing and selecting data

- Python slicing operation '[]' and attribute/ dot operator '.' are used for indexing
- Provides quick and easy access to pandas data structures

| DataFrame.head([n])                                           |                                                      |
| ------------------------------------------------------------- | ---------------------------------------------------- |
| The function head returns the first n rows from the dataframe |                                                      |
| `cars_data1.head(6)`                                          | By default, the head() function returns first 5 rows |

| DataFrame.tail([n])                                          |                                                     |
| ------------------------------------------------------------ | --------------------------------------------------- |
| The function tail returns the last n rows from the dataframe |                                                     |
| `cars_data1.tail(6)`                                         | By default, the tail() function returns last 5 rows |
- To access a scalar value, the fastest way is to use the `at` and `iat` methods
	- `at` provides label-based scalar lookups
	- `cars_data1.at[4, 'FuelType']`

	- `iat` provides integer-based lookups
	- `cars_data1.iat[4, 3]`
	
- To access a group of rows and columns by label(s) `.loc[]` can be used
	- `car_data1.loc[:, 'FuelType']`