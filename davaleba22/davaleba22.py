import json

with open('movies.json', 'r') as json_file:
    data = json.load(json_file)

movies_struct = []
page = 1

for movies in data:
    results = []
    for movie in movies['results']:
        release_year = int(movie['release_date'].split('-')[0])
        genre = movie['genres']

        if release_year > 2000 and "Crime" in genre:
            crime_index = genre.index('Crime')
            genre[crime_index] = "New_Crime"
        elif release_year < 2000 and "Drama" in genre:
            drama_index = genre.index('Drama')
            genre[drama_index] = "Old_Drama"
        elif release_year == 2000 and "New_Century" not in genre:
            genre.append("New_Century")
        else:
            continue
        results.append(movie)

    movies_struct.append({
        "page": page,
        "results": results
    })
    page += 1

print(movies_struct)

with open('movies.json', 'w') as json_file:
    json.dump(movies_struct, json_file, indent=4)
