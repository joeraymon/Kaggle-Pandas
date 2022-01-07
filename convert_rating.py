''' We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too hard to understand. We'd like to
translate them into simple star ratings. A score of 95 or higher counts as 3 stars, a score of at least 85 but less than 95 is 2 stars. Any other score
is 1 star. Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should automatically get 3 stars, regardless
of points. Create a series star_ratings with the number of stars corresponding to each review in the dataset. '''

star_ratings = reviews.apply(lambda x: 3 if (x['points'] >= 95 or x['country'] == 'Canada') else 2 if x['points'] >= 85 else 1, axis=1)
