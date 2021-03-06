from collections import defaultdict

sample_dict = defaultdict(list)

print(type(sample_dict))

print('{:*^100}'.format(''))
print('*' *100)

sample_dict['key_1'].append(1)
sample_dict['key_1'].append(2)

defaultdict(list, {'key_1': [1, 2]})

sample_dict['key_2'].append(4)

defaultdict(list, {'key_1': [1, 2], 'key_2': [4]})

print(sample_dict)

for key, value in sample_dict.items():
    print(key, value)


# Another example of defaultdict
from collections import defaultdict

row_genres = ['Action|Adventure|Fantasy|Sci-Fi',
                'Action|Adventure|Fantasy',
                'Action|Adventure|Thriller',
                'Action|Thriller',
                'Documentary',
                'Action|Adventure|Sci-Fi']


genre_counts = defaultdict(int)
for row_genre in row_genres:
    genres = row_genre.split('|')
    for genre in genres:
        genre_counts[genre] += 1

print(genre_counts)
