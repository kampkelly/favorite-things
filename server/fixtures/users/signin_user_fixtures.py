signin_user_mutation = '''mutation {
  signinUser(email: "runor@example.com", password: "password") {
    user {
      email
      name
    }
  }
}
'''

signin_user_mutation_response = {
  "data": {
    "signinUser": {
      "user": {
        "email": "runor@example.com",
        "name": "Runor"
      }
    }
  }
}
