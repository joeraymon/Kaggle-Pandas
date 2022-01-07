'''What combination of countries and varieties are most common? Create a Series whose index is a MultiIndexof {country, variety} pairs.
For example, a pinot noir produced in the US should map to {"US", "Pinot Noir"}. Sort the values in the Series in descending order based on wine count.'''

country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)
