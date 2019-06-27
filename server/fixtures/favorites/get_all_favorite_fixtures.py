get_all_favorite_query = '''query {
  getFavoriteThings {
    title
  }
}

'''

get_all_favorite_response = {
  "data": {
    "getFavoriteThings": [
      {
        "title": 'Football'
      }
    ]
  }
}
