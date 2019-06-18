query_all_categories_query = '''query {
  getCategories {
    name
  }
}
'''

query_all_categories_query_response = {
  "data": {
    "getCategories": [
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
