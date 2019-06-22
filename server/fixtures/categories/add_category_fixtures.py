add_category_mutation = '''mutation {
  createCategory(name: "music") {
    category {
      name
    }
  }
}
'''

add_category_mutation_response = {
  "data": {
    "createCategory": {
      "category": {
        "name": "music"
      }
    }
  }
}
