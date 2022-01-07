'''What is the best wine I can buy for a given amount of money? Create a Series whose index is wine prices and whose values is the maximum number
of points a wine costing that much was given in a review. Sort the values by price, ascending (so that 4.0 dollars is at the top and 3300.0 dollars
is at the bottom).'''

best_rating_per_price = reviews.groupby('price').points.max()
