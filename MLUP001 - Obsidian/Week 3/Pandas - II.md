#### Data types
- The way information gets stored in a dataframe or a python object affects the analysis and outputs of calculations
- There are two main types of data
	- numeric and character types
-  Numeric data types include integers and floats
	- For example: integer - 10, float - 10.53
- Strings are known as objects in pandas which can store values that contain numbers and / or characters
	- For example: 'category1'

#### Numeric types
- Pandas and base Python uses different names for data types

| Python data type | Pandas data type | Description                      |
| ---------------- | ---------------- | -------------------------------- |
| int              | int64            | Numeric characters               |
| float            | float64          | Numeric characters with decimals |
- '64' simply refers to the memory allocated to store data in each cell which effectively relates to how many digits it can store in each cell
- 64 bits is equivalent to 8 bytes
- Allocating space ahead of time allows computers to optimize storage and processing efficiency

#### Character types
- Two types: category and object

| category                                                                                                                                              | object                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| &bull; A string variable consisting of only a few different values. Converting such a string variable to a categorical variable will save some memory | &bull; The column will be assigned as object data type when it has mixed types (numbers and strings). If a column contains 'nan' (blank cells), pandas will default to object datatype. |
| &bull; A categorical variable takes on a limited, fixed numbers of possible values                                                                    | &bull; For strings, the length is not fixed                                                                                                                                             |

#### Checking data types of each column
- dtypes returns a series with the data type of each column
- Syntax: `DataFrame.dtypes`
- `cars_data1.dtypes`

#### Count of unique data types
- dataframe.dtypes.value_counts() returns counts of unique data types in the dataframe
- Syntax: `DataFrame.dtypes.value_counts()`
- `cars_data1.dtypes.value_counts()`

#### Selecting data based on data types
- pandas.DataFrame.select_dtypes() returns a subset of the columns from dataframe based on the column dtypes
- Syntax: `DataFrame.select_dtypes(include=None, exclude=None`)
- `cars_data.select_dtypes(exclude=[object])`

#### Concise summary of dataframe
- info() returns a concise summary of a dataframe
- data type of index
- data type of column
- count of non-null values
- memory usage
- Syntax: `DataFrame.info()`
- `cars_data1.info()`

#### Unique elements of columns
- unique() is used to find the unique elements of a column
- Syntax: `numpy.unique(array)`
- `np.unique(cars_data1['KM']`