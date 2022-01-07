'''Create a Series whose index is reviewers and whose values is the average review score given out by that reviewer.'''

reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()
