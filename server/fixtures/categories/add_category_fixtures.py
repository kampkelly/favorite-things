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

add_category_with_no_name_mutation = '''mutation {
  createCategory(name: "") {
    category {
      name
    }
  }
}
'''
