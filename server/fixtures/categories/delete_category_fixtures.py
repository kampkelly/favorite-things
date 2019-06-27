delete_category_mutation = '''mutation {
  deleteCategory(id: 3) {
    category {
      id
      name
    }
  }
}
'''

delete_category_mutation_response = {
  "data": {
    "deleteCategory": {
      "category": {
        "id": "3",
        "name": "food"
      }
    }
  }
}

delete_category_with_non_existent_id_mutation = '''mutation {
  deleteCategory(id: 30) {
    category {
      id
      name
    }
  }
}
'''

delete_category_with_favorite_mutation = '''mutation {
  deleteCategory(id: 1) {
    category {
      id
      name
    }
  }
}
'''
