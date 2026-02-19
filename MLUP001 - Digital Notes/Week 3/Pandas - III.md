#### Importing Data
- We need to know how missing values are represented in the dataset in order to make reasonable decisions
- The missing values exists in the form 'nan', '??', '????'
	- Python, by default replace blank values with 'nan'
- Now, importing the data considering other forms of missing values in a dataframe 

`cars_data = pd.read_csv('Toyota.csv', index_col=0, na_values=["??", "????"])`

#### Converting variable's data types
- `astype()` method is used to explicitely convert data types from one to another
- Syntax: `DataFrame.astype(dtype)`
- Ex: Converting 'MetColor', 'Automatic' to object data type:
	- `cars_data['MetColor'] = cars_data['MetColor'].astype('object')`
	- `cars_data['Automatic'] = cars_data['Automatic'].astype('object')`

#### category vs object data type
- `nbytes()` is used to get the total bytes consumed by the elements of the columns
- Syntax: `ndarray.nbytes`
- Ex: Memory usage for 'FuelType' column:
	- As object: `cars_data['FuelType'].nbytes` —> 11488
	- As category: `cars_data['FuelType'].astype('category').nbytes` —> 1460

#### Cleaning columns
- Checking unique values of variable 'Doors':
	- `numpy.unique()`
- `replace()` is used to replace a value with the desired value
- Syntax: `DataFrame.replace([to_replace, value, inplace=True, ....])`
- Ex:
	- `cars_data['Doors'].replace('three', 3, inplace=True)`
	- `cars_data['Doors'].replace('four', 4, inplace=True)`
	- `cars_data['Doors'].replace('five', 5, inplace=True)`
	- `cars_data['Doors'] = pd.to_numeric(cars_data['Doors], errors='coerce').astype('Int64')`
#### To detect missing values
- To check the count of missing values present in each column `Dataframe.isnull.sum()` is used
- `cars_data.isnull().sum()`