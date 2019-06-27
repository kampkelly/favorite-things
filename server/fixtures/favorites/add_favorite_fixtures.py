add_favorite_mutation = '''mutation {
  addFavoriteThing(title: "Tennis", categoryId: 1, description: "", objectMetadata: "{}", ranking: 1) {
    favoriteThing {
      title
      ranking
    }
  }
}
'''

add_favorite_mutation_response = {
  "data": {
    "addFavoriteThing": {
      "favoriteThing": {
        "title": "Tennis",
        "ranking": 1
      }
    }
  }
}

add_favorite_with_empty_title_mutation = '''mutation {
  addFavoriteThing(title: "", categoryId: 1, description: "", ranking: 1) {
    favoriteThing {
      title
      ranking
    }
  }
}
'''

add_favorite_with_no_title_mutation = '''mutation {
  addFavoriteThing(categoryId: 1, description: "", ranking: 1) {
    favoriteThing {
      title
      ranking
    }
  }
}
'''

add_favorite_with_no_category_id_mutation = '''mutation {
  addFavoriteThing(title: "Tennis", description: "", ranking: 1) {
    favoriteThing {
      title
      ranking
    }
  }
}
'''

add_favorite_with_no_ranking_mutation = '''mutation {
  addFavoriteThing(title: "Tennis", categoryId: 1, description: "") {
    favoriteThing {
      title
      ranking
    }
  }
}
'''

add_favorite_with_description_less_than_10_characters = '''mutation {
  addFavoriteThing(title: "Tennis", categoryId: 1, ranking: 1, description: "describe") {
    favoriteThing {
      title
      ranking
    }
  }
}
'''
