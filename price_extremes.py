'''What are the minimum and maximum prices for each variety of wine? Create a DataFrame whose index is the variety category from the dataset
and whose values are the min and max values thereof.'''

price_extremes = reviews.groupby('variety').price.agg([min, max])
