# I'm focusing on `MildlyInteresting` and `MildlyInfuriating` to do 4 main things:

1. Task 1. Compare these subreddits based on their content from 2013. (see [2013 Data](jn_1_2013_data.ipynb))
2. Task 2. Compare these subreddits based on their content from 2017. (see [2017 Data](jn_2_2017_data.ipynb))
3. Task 3. Individually compare each subreddit based on their content from 2013 and 2017. (see [2017 Data](jn_2_2017_data.ipynb))
4. Task 4. Predict which subreddit a new post made in 2018 belongs to. (see [2017 Data](jn_2_2017_data.ipynb))

I want to use reddit to not only advertise my product, but to also hurt my competitors. Taking what I learned from my above 4 goals, can I casually advertise my product, with success, on `MildlyInteresting` and "smack talk" on my competitors on `MildlyInfuriating`?

After going through my data, modelling 2013 and 2017 data, I can predict which subreddit a late 2018 post belongs to with 70% accuracy using my model trained with 2017 data. I found that around 45% of the most impactful features remain the same from 2013 to 2017. This tells me that the less impactful features are what play a part in distinguishing a subreddit. Not only that, I'm confident that if I trained data using posts from the first half of 2018, I would be able to better predict posts made later in 2018.

## So, how would I advertise my product on these subreddits?
These are the 15 most impactful words to show interest: 'looks', 'tree', 'found', 'shaped', 'bird', 'growing', 'plant', 'face', 'shadow', 'caught', 'snow', 'fell', 'made', 'leaf', and 'accidentally'.
#### Thus, I would write something that goes along the lines of "This new product that I *found* *looks* great. *It recently *caught* my eye, and when *face* to face with its competition, it does much better, and leaves it in the *shadows*. I know this product with continue to *grow* and it *makes* my life better and easier. I'm so glad it *accidentally* *fell* my way."

## So, how would I market against my competitors on these subreddits?
These are the 15 most impactful words to show infuriation: 'centered', 'tile', 'fucking', 'every', 'crooked', 'ads', 'hate', 'order', 'roommate', 'even', 'thanks', 'annoying', 'uneven', 'shit', and 'thread'.
#### Thus, I would write something that goes along the lines of "I *f___ing* *hate* this product. *Every* time my *roomate* or I have had to use it, it works like *s__t*. It's beyond *annoying* with its *ads* which aren't even *centered* or *ordered properly*. *Thanks* Obama..."