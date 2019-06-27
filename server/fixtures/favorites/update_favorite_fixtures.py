update_favorite_mutation = '''mutation {
  updateFavoriteThing(id: 1, title: "New Tennis", ranking: 1) {
    favoriteThing {
      id
      title
      ranking
    }
  }
}
'''

update_favorite_mutation_response = {
  "data": {
    "updateFavoriteThing": {
      "favoriteThing": {
        "id": "1",
        "title": "New Tennis",
        "ranking": 1
      }
    }
  }
}

update_favorite_with_no_id_mutation = '''mutation {
  updateFavoriteThing(title: "New Tennis", ranking: 1) {
    favoriteThing {
      id
      title
      ranking
    }
  }
}
'''

update_favorite_with_no_ranking_mutation = '''mutation {
  updateFavoriteThing(id: 1, title: "New Tennis") {
    favoriteThing {
      id
      title
      ranking
    }
  }
}
'''

update_favorite_with_description_less_than_10_characters = '''mutation {
  addFavoriteThing(title: "Tennis", categoryId: 1, ranking: 1, description: "describe") {
    favoriteThing {
      title
      ranking
    }
  }
}
'''

update_favorite_with_empty_title_mutation = '''mutation {
  addFavoriteThing(title: "", categoryId: 1, description: "", ranking: 1) {
    favoriteThing {
      title
      ranking
    }
  }
}
'''
