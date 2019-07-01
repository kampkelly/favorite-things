query_all_categories_query = '''query {
  allCategories {
    name
  }
}
'''

query_all_categories_query_response = {
  "data": {
    "allCategories": [
      {
        "name": "person"
      },
      {
        "name": "place"
      },
      {
        "name": "food"
      }
    ]
  }
}

query_categories_with_favorites_query = '''query {
  getCategoriesAndFavorites {
    id
    name
    favoriteThings {
      title
      ranking
    }
  }
}

'''

query_categories_with_favorites_query_response = {
  "data": {
    "getCategoriesAndFavorites": [
      {
        "id": 1,
        "name": "person",
        "favoriteThings": [
          {
            "title": "Football",
            "ranking": 1
          }
        ]
      }
    ]
  }
}
