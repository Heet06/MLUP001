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
| **Function** | `samp = cars_data.copy(deep=False)`<br>`samp = cars_data`                                                                                                                      | `cars_data1 = cars_data.copy(deep=                                                                                                                                                                      |
| Description  | &bull; It only creates a new variable that shares the reference of the original object<br>&bull; Any changes made to a copy of object will be reflected in the original object | &bull; In case of a deep copy, a copy of object is copied in other object with no reference to the original<br>&bull; Any changes made to a copy of object will not be reflected in the original object |
#### Attributes of data
