import pandas as pd
data = pd.read_table('http://bit.ly/chiporders')
data = pd.read_table('http://bit.ly/chiporders', sep= '|', header=None, names=col_names)
data.head()
data.tail()
data.shape
data.describe()
data.describe(include=['object'])
data.columns
data.rename(columns = { 'star_rating' : 'Rating Reviews'})
data.drop('Title',axis=1)
data.drop(['Genre','Time','ActorList'], axis=1)
data.drop([0,1,2,3], axis=0)
data['StarRating'].sort_values(ascending=False)
data.sort_values('Time', ascending=False)
data.sort_values(['Title','ActorList'], ascending=True)
data.sort_values(['Title','ActorList'], ascending=False)
data[data.Time >='110']
booleans = []
for value in data.Time:
    if value >="100":
        booleans.append(True)
    else:
        booleans.append(False)
data[booleans]
data.types
type(data)
type(data['Age'])
data.Age
data.new    = data.Profession + data.Gender
data['new'] = data.Profession + data.Gender

# Data Aquisition
data = pd.read_csv('http://bit.ly/imdbratings')
data = pd.read_csv('http://bit.ly/imdbratings', usecols=['title','genre','duration'])
data = pd.read_csv('http://bit.ly/imdbratings', usecols=['title','genre','duration'], nrows = 30)
data[(data.genre == 'Crime') | (data.genre == 'Drama') | (data.genre == 'Action')]
data[data.genre.isin(['Crime','Drama','Action'])]
data[(data.content_rating == 'R') & (data.genre == 'Crime')]
(data.content_rating == 'R') & (data.genre == 'Crime')
data[data.genre == 'Crime']
data[data.genre == 'Action']
data[data.genre == 'Drama']
data.describe()
data.mean()
data.duration.describe()
data.genre.str.upper()
data.genre.str.lower()
data.title.str.upper()

# Data Type Changing Mechanism
data = pd.read_csv('http://bit.ly/imdbratings')
data = pd.read_csv('http://bit.ly/imdbratings', dtype= {'duration':float})
data.dtypes
data.duration.astype(float)
data.duration = data.duration.astype(float)
data.dtypes

# Real Example
data = pd.read_table('http://bit.ly/chiporders')
data.dtypes
data.item_price
data.item_price.str.replace('$','').astype(float)
data.item_price.str.replace('$','').astype(float).mean()
data.item_name.str.contains('and').head(10)
data.item_name.str.contains('and').head(10).astype(int)

# Review on Pandas
import pandas as pd
data = ['BMW','Toyota','Mercedez','Mitshubishi']
df   = pd.DataFrame(data)
df   = pd.DataFrame(data, index=['Brand_001','Brand_002','Brand_003','Brand_004'])
df   = pd.DataFrame(data, index=['Brand_001','Brand_002','Brand_003','Brand_004'], columns=['Car Model'])
print(df)

data = [ ['Apple', 135], ['Orange', 143], ['Mango', 145]]
df   = pd.DataFrame(data)
df   = pd.DataFrame(data, columns=['Food','Price'])
df   = pd.DataFrame(data, columns=['Food','Price'], index=['Item_001','Item_002','Item_003'])
print(df)

data = {'Food' :['Apple','Mango','Orange'], 
		'Price':[124,150,175]}
df   = pd.DataFrame(data)
df   = pd.DataFrame(data, index=['ID_001','ID_002','ID_003'])
print(df)

data = pd.read_csv('http://bit.ly/imdbratings')
data.head()
data.duration.describe()
%matplotlib inline
data.duration.plot(kind='hist')
data.duration.plot(kind='bar')

data.genre
data.genre.value_counts()
data.genre.value_counts().plot(kind='bar')

# Dealing with Missing Data
data = pd.read_csv('http://bit.ly/uforeports')
data.head(10)
data.isnull()
data.notnull()
data.isnull().sum()
data.isnull().head()	
data.City.isnull().sum()

# Dealing with Data Indexing
data = pd.read_csv('http://bit.ly/uforeports')
data.head()
data.columns
data.index
data.shape
data.loc[5,'City']
data.set_index('City', inplace=True)
data.State == 'NY'
data[data.State == 'NY']
data[data.State == 'NY'].describe()

# Column Index
data = pd.read_csv('http://bit.ly/uforeports')
data.set_index('City', inplace=True)
data.reset_index(inplace=True)
data.describe()
data.describe().index
data.describe().columns
data.describe().loc['freq','State']

drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks = pd.read_csv('http://bit.ly/drinksbycountry', index_col = 'country')