movies = [
  {
    title: "Beetlejuice",
    year: 1988,
    genres: ["Comedy", "Fantasy"],
  },
  {
    title: "The Cotton Club",
    year: 1984,
    genres: ["Crime", "Drama", "Music"],
  },
  {
    title: "The Shawshank Redemption",
    year: 1994,
    genres: ["Crime", "Drama"],
  },
  {
    title: "Crocodile Dundee",
    year: 1986,

    genres: ["Adventure", "Comedy"],
  },
  {
    title: "Valkyrie",
    year: 2008,
    genres: ["Drama", "History", "Thriller"],
  },
  {
    title: "Ratatouille",
    year: 2007,
    genres: ["Animation", "Comedy", "Family"],
  },
  {
    title: "City of God",
    year: 2002,

    genres: ["Crime", "Drama"],
  },
  {
    title: "Memento",
    year: 2000,

    genres: ["Mystery", "Thriller"],
  },
  {
    title: "The Intouchables",
    year: 2011,

    genres: ["Biography", "Comedy", "Drama"],
  },
  {
    title: "Stardust",
    year: 2007,
    genres: ["Adventure", "Family", "Fantasy"],
  },
]

def sort_by_year(movies):
    sorted_movies = sorted(movies, key=lambda x: x['year'], reverse=True)
    return sorted_movies

# Test the sort_by_year function
sorted_by_year = sort_by_year(movies)
for movie in sorted_by_year:
    print(f"{movie['title']} - {movie['year']}")

def sort_by_title(movies):
    def remove_leading_articles(title):
        articles = ["A ", "An ", "The "]
        for article in articles:
            if title.startswith(article):
                return title[len(article):]
        return title

    sorted_movies = sorted(movies, key=lambda x: remove_leading_articles(x['title']))
    return sorted_movies

# Test the sort_by_title function
sorted_by_title = sort_by_title(movies)
for movie in sorted_by_title:
    print(movie['title'])
