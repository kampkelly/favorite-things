get_single_favorite_query = '''query {
  getSingleFavoriteThing(id: 1) {
    id
    title
  }
}
'''

get_single_favorite_query_response = {
  "data": {
    "getSingleFavoriteThing": {
      "id": "1",
      "title": "Football",
    }
  }
}

get_single_favorite_with_non_existing_id_query = '''query {
  getSingleFavoriteThing(id: 10) {
    id
    title
  }
}
'''
