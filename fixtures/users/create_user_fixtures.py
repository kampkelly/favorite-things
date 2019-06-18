create_user_mutation = '''mutation {
  signupUser(email: "kamp@example.com", name: "Kamp", password: "password") {
    user {
      email
      name
    }
  }
}
'''

create_user_mutation_response = {
  "data": {
    "signupUser": {
      "user": {
        "email": "kamp@example.com",
        "name": "Kamp"
      }
    }
  }
}
