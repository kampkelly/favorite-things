delete_favorite_mutation = '''mutation {
  deleteFavoriteThing(id: 1) {
    favoriteThing {
      id
      title
      ranking
    }
  }
}
'''

delete_favorite_mutation_response = {
  "data": {
    "deleteFavoriteThing": {
      "favoriteThing": {
        "id": "1",
        "title": "Football",
        "ranking": 1
      }
    }
  }
}
