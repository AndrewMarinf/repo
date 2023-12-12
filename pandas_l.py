# 1_lesson_Creating, Reading and Writing

import pandas as pd

pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})





pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])


pd.Series([1, 2, 3, 4, 5])



pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')


# вытащить данные из файлика 
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")

# узнаем на сколько файлик большой 
wine_reviews.shape

# Таким образом, наш новый DataFrame имеет 130 000 записей, разбитых на 14 разных столбцов. 
# Это почти 2 миллиона записей
(129971, 14)


# Мы можем изучить содержимое результирующего DataFrame с помощью команды head (), которая захватывает первые пять строк
wine_reviews.head()

wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
wine_reviews.head()

# ==================================================================================================
# 2_lesson_Indexing, Selecting & Assigning
reviews.country # country название столба


reviews['country']
0            Italy
1         Portugal
            ...   
129969      France
129970      France
Name: country, Length: 129971, dtype: object


reviews['country'][0]
'Italy'


# выдас все столбы с  строкой [0]
reviews.iloc[0]

country                                                    Italy
description    Aromas include tropical fruit, broom, brimston...
                                     ...                        
variety                                              White Blend
winery                                                   Nicosia
Name: 0, Length: 13, dtype: object



# получить первый столб
reviews.iloc[:, 0] 0 это столбец 

0            Italy
1         Portugal
            ...   
129969      France
129970      France
Name: country, Length: 129971, dtype: object


# первый столбец и три строки 0 это столбец 
reviews.iloc[:3, 0]

0       Italy
1    Portugal
2          USA
Name: country, dtype: object

# тут выбираем первый и третью строку 0 это столбец 
reviews.iloc[1:3, 0]

1    Portugal
2          US
Name: country, dtype: object

# тут хз
reviews.iloc[[0, 1, 2], 0] 

0       Italy
1    Portugal
2          US
Name: country, dtype: object


# тут пять последних 
reviews.iloc[-5:]


# тут вытащим по индексу, а не по порядку 

reviews.loc[0, 'country'] 

'Italy' 

# вытащить с стобцами такими то  

reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]


taster_name	taster_twitter_handle	points
0	Kerin O’Keefe	@kerinokeefe	87
1	Roger Voss	@vossroger	87
...	...	...	...
129969	Roger Voss	@vossroger	90
129970	Roger Voss	@vossroger	90


# тут вытащить столбы с назвать их по нужным индексам
a = ['country','province','region_1','region_2']
i = [0,1,10,100]

df = pd.DataFrame(reviews.loc[i,a])

# country	province	region_1	region_2
# 0	Italy	Sicily & Sardinia	Etna	NaN
# 1	Portugal	Douro	NaN	NaN
# 10	US	California	Napa Valley	Napa
# 100	US	New York	Finger Lakes	Finger Lakes


# подставим столбец "title" как индекс для бд
reviews.set_index("title")


# тут в каком индексе(стрке ) есть слово Италия
reviews.country == 'Italy'

0          True
1         False
          ...  
129969    False
129970    False
Name: country, Length: 129971, dtype: bool


# ищем по строке 'Italy' в столбе country
reviews.loc[reviews.country == 'Italy']

# 	country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	title	variety	winery
# 0	Italy	Aromas include tropical fruit, broom, brimston...	Vulkà Bianco	87	NaN	Sicily & Sardinia	Etna	NaN	Kerin O’Keefe	@kerinokeefe	Nicosia 2013 Vulkà Bianco (Etna)	White Blend	Nicosia
# 6	Italy	Here's a bright, informal red that opens with ...	Belsito	87	16.0	Sicily & Sardinia	Vittoria	NaN	Kerin O’Keefe	@kerinokeefe	Terre di Giurfo 2013 Belsito Frappato (Vittoria)	Frappato	Terre di Giurfo
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 129961	Italy	Intense aromas of wild cherry, baking spice, t...	NaN	90	30.0	Sicily & Sardinia	Sicilia	NaN	Kerin O’Keefe	@kerinokeefe	COS 2013 Frappato (Sicilia)	Frappato	COS
# 129962	Italy	Blackberry, cassis, grilled herb and toasted a...	Sàgana Tenuta San Giacomo	90	40.0	Sicily & Sardinia	Sicilia	NaN	Kerin O’Keefe	@kerinokeefe	Cusumano 2012 Sàgana Tenuta San Giacomo Nero d...	Nero d'Avola	Cusumano


# объединяем два запроса , & значит and

reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)] 

# 	country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	title	variety	winery
# 120	Italy	Slightly backward, particularly given the vint...	Bricco Rocche Prapó	92	70.0	Piedmont	Barolo	NaN	NaN	NaN	Ceretto 2003 Bricco Rocche Prapó (Barolo)	Nebbiolo	Ceretto
# 130	Italy	At the first it was quite muted and subdued, b...	Bricco Rocche Brunate	91	70.0	Piedmont	Barolo	NaN	NaN	NaN	Ceretto 2003 Bricco Rocche Brunate (Barolo)	Nebbiolo	Ceretto
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 129961	Italy	Intense aromas of wild cherry, baking spice, t...	NaN	90	30.0	Sicily & Sardinia	Sicilia	NaN	Kerin O’Keefe	@kerinokeefe	COS 2013 Frappato (Sicilia)	Frappato	COS
# 129962	Italy	Blackberry, cassis, grilled herb and toasted a...	Sàgana Tenuta San Giacomo	90	40.0	Sicily & Sardinia	Sicilia	NaN	Kerin O’Keefe	@kerinokeefe	Cusumano 2012 Sàgana Tenuta San Giacomo Nero d...	Nero d'Avola	Cusumano


# объединяем два запроса , | значит or

reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]

# 	country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	title	variety	winery
# 0	Italy	Aromas include tropical fruit, broom, brimston...	Vulkà Bianco	87	NaN	Sicily & Sardinia	Etna	NaN	Kerin O’Keefe	@kerinokeefe	Nicosia 2013 Vulkà Bianco (Etna)	White Blend	Nicosia
# 6	Italy	Here's a bright, informal red that opens with ...	Belsito	87	16.0	Sicily & Sardinia	Vittoria	NaN	Kerin O’Keefe	@kerinokeefe	Terre di Giurfo 2013 Belsito Frappato (Vittoria)	Frappato	Terre di Giurfo
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 129969	France	A dry style of Pinot Gris, this is crisp with ...	NaN	90	32.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Domaine Marcel Deiss 2012 Pinot Gris (Alsace)	Pinot Gris	Domaine Marcel Deiss
# 129970	France	Big, rich and off-dry, this is powered by inte...	Lieu-dit Harth Cuvée Caroline	90	21.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Domaine Schoffit 2012 Lieu-dit Harth Cuvée Car...	Gewürztraminer	Domaine Schoffit



# тоже обьединить 
reviews.loc[reviews.country.isin(['Italy', 'France'])] 


# 	country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	title	variety	winery
# 0	Italy	Aromas include tropical fruit, broom, brimston...	Vulkà Bianco	87	NaN	Sicily & Sardinia	Etna	NaN	Kerin O’Keefe	@kerinokeefe	Nicosia 2013 Vulkà Bianco (Etna)	White Blend	Nicosia
# 6	Italy	Here's a bright, informal red that opens with ...	Belsito	87	16.0	Sicily & Sardinia	Vittoria	NaN	Kerin O’Keefe	@kerinokeefe	Terre di Giurfo 2013 Belsito Frappato (Vittoria)	Frappato	Terre di Giurfo
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 129969	France	A dry style of Pinot Gris, this is crisp with ...	NaN	90	32.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Domaine Marcel Deiss 2012 Pinot Gris (Alsace)	Pinot Gris	Domaine Marcel Deiss
# 129970	France	Big, rich and off-dry, this is powered by inte...	Lieu-dit Harth Cuvée Caroline	90	21.0	Alsace	Alsace	NaN	Roger V



# где price.notnull

reviews.loc[reviews.price.notnull()]

# 	country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	title	variety	winery
# 1	Portugal	This is ripe and fruity, a wine that is smooth...	Avidagos	87	15.0	Douro	NaN	NaN	Roger Voss	@vossroger	Quinta dos Avidagos 2011 Avidagos Red (Douro)	Portuguese Red	Quinta dos Avidagos
# 2	US	Tart and snappy, the flavors of lime flesh and...	NaN	87	14.0	Oregon	Willamette Valley	Willamette Valley	Paul Gregutt	@paulgwine	Rainstorm 2013 Pinot Gris (Willamette Valley)	Pinot Gris	Rainstorm
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 129969	France	A dry style of Pinot Gris, this is crisp with ...	NaN	90	32.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Domaine Marcel Deiss 2012 Pinot Gris (Alsace)	Pinot Gris	Domaine Marcel Deiss
# 129970	France	Big, rich and off-dry, this is powered by inte...	Lieu-dit Harth Cuvée Caroline	90	21.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Domaine Schoffit 2012 Lieu-dit Harth Cuvée Car...	Gewürztraminer	Domaine Schoffit

