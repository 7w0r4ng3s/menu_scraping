import pandas as pd

# read the csv file and make a unique list of foods
df = pd.read_csv('Data.csv').drop('index', 1)
foods = list(df['food'].unique()) # a list of unique foods

# return the number of times a food appears and the number of time you like it
def search():
    food_name = input('Search food: ') # works whether you type it uppercase or lowercase
    if food_name in foods:
        new_df = df.loc[df['food'] == food_name]
        total = new_df['food'].count() # total times the food appears
        like = new_df.iloc[:, 1].sum(0) # number of times you like it
        # TODO: add preference evaluation
        print('-' * 50)
        print(f'Out of {total} time(s), you like {food_name} {like} time(s).')
        print('-' * 50)
        
    elif food_name not in foods:
        tmp = [] # a list to store possible foods
        """if the user type a part of a food name
        it will return the possible food names"""
        
        [tmp.append(item) for item in foods if food_name.lower() in item.lower()] # possible food list
        l = [i+1 for i in list(range(len(tmp)))] # index list

        if len(tmp) == 0:
            print(f'No result related to {food_name}. Please try again.')
            return None

        print('Do you mean:')

        food_dict = dict(zip(l, tmp))
        for i in food_dict.keys():
            print(i, food_dict[i])
        print()

        # choose the desired food name again
        choice = int(input('Enter the index: '))
        new_df = df.loc[df['food'] == food_dict[choice]]
        total = new_df['food'].count() # total times the food appears
        like = new_df.iloc[:, 1].sum(0) # number of times you like it
        score = like / total

        print('-' * 80)
        print(f'Out of {total} time(s), you like [{food_dict[choice]}] {like} time(s).')
        print('-' * 80)
    return score


def report(food_name):
    new_df = df.loc[df['food'] == food_name]
    total = new_df['food'].count() # total times the food appears
    like = new_df.iloc[:, 1].sum(0) # number of times you like it
    food_score = like / total
    print('[{}] score: '.format(food_name), food_score)
    # a simple food preference evaluation to a specific food
    if food_score > 0.5:
        print('You like [{food_name}] over half of the time.')
    elif food_score < 0.5:
        print('You like [{food_name}] below half of the time.')
    else:
        print('50-50')


# an algorithm which calculates a 'food value'
# food value - a value evaluating the likelihood you will like the menu of one day
# based on the food preference database
# def evaluate(date):
    

