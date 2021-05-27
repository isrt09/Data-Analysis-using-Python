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