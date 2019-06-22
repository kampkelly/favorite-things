<template>
    <div>
        <div class="signup-container">
            <h5 class="mb-3">Create an account to start entering your favorite things</h5>
            <ul>
                <li v-for="(error, index) in this.errors" v-bind:key="index" class="text-danger">
                    {{error}}
                </li>
            </ul>
            <form>
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" class="form-control" id="name" v-model="name" placeholder="">
                </div>
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="text" class="form-control" id="email" v-model="email" placeholder="">
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" class="form-control" id="password" v-model="password" placeholder="">
                </div>
                <div class="form-group">
                    <label for="confirm_password">Confirm Password</label>
                    <input type="password" class="form-control" id="confirm_password" v-model="confirmPassword" name="confirm_password" placeholder="">
                </div>
                <div class="form-group">
                    <button class="btn btn-primary" type="submit" v-bind:disabled="disabled" v-on:click="signup">Sign Up</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
// eslint-disable-next-line
import gql from 'graphql-tag';
const filter = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/;
const signUpQuery = gql`mutation ($email: String!, $name: String!, $password: String!) {
  signupUser(email: $email, name: $name, password: $password) {
    user {
      email
      name
    }
    token
  }
}`;

export default {
    data() {
        return {
            name: '',
            email: '',
            password: '',
            confirmPassword: '',
            disabled: false,
            errors: []
        };
    },
    methods: {
        async signup(event) {
            try {
                event.preventDefault();
                this.disabled = true;
                const validInputs = this.validateFormInputs();
                if (validInputs) {
                    const data = await this.$apollo.mutate({
                        mutation: signUpQuery,
                        // Parameters
                        variables: {
                            email: this.email,
                            name: this.name,
                            password: this.password,
                        },
                    });
                    this.$router.push('/');
                    this.disabled = false;
                } else {
                    this.disabled = false;
                }
            } catch (error) {
                this.errors.push(error.graphQLErrors[0].message);
                this.disabled = false;
            }
        },
        validateFormInputs() {
            this.errors = [];
            if (this.password != this.confirmPassword) {
                this.errors.push('Passwords do not match');
            }
            if (this.password < 8) {
                this.errors.push('Password must be at least 8 characters');
            }
            if (this.name < 1) {
                this.errors.push('Name is too short');
            }
            if (!filter.test(this.email)) {
                this.errors.push('Email is not valid');
            }
            if (this.errors.length) {
                return false;
            } else {
                return true;
            }
        },
    }
}
</script>


<style lang="scss" scoped>
.signup-container {
    background: white;
    padding: 0px 5em 0px 5em;
    form {
        .form-group {
            margin-bottom: 28px;
            label {
                float: left;
            }
            button {
                background: #6202EE;
                color: white;
            }
        }
    }
}
</style>
