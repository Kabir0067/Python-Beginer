import random
rand1=random.randint(0,6)
print('Generate a random integer between 0 and 6','\n',rand1)
rand2=random.randint(5,9)
print('Generate a random integer between 5 and 10, excluding 10','\n',rand2)
rand3=random.randrange(0,10,3)
print('Generate a random integer between 0 and 10, with a set of 3','\n',rand3)

from datetime import datetime, timedelta
start_date = datetime(2024, 5, 7)
end_date = datetime(2024, 5, 8)
random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
print('Random Date between two dates:\n',random_date.strftime('%Y-%m-%d'))

