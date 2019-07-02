<template>
    <div>
        <div class="signin-container">
            <h5 class="mb-3">Log in to access your favorite things</h5>
            <ul>
                <li v-for="(error, index) in this.errors" v-bind:key="index" class="text-danger">
                    {{error}}
                </li>
            </ul>
            <form>
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="text" class="form-control" id="email" v-model="email" placeholder="">
                </div>
                <div class="form-group">
                    <label for="password">Passworddd</label>
                    <input type="password" class="form-control" id="password" v-model="password" placeholder="">
                </div>
                <div class="form-group">
                    <button class="btn btn-primary" type="submit" v-bind:disabled="disabled" v-on:click="signin">Signin</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
// eslint-disable-next-line
import gql from 'graphql-tag';
import { LOGIN } from '../mutationTypes';
import { SET_APP_ERROR_MESSAGE } from '../mutationTypes';

const filter = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/;
const signInQuery = gql`mutation ($email: String!, $password: String!) {
  signinUser(email: $email, password: $password) {
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
            email: '',
            password: '',
            disabled: false,
            errors: [],
            user: {},
            token: '',
        };
    },
    methods: {
        async signin(event) {
            try {
                event.preventDefault();
                this.disabled = true;
                const validInputs = this.validateFormInputs();
                if (validInputs) {
                    const data = await this.$apollo.mutate({
                        mutation: signInQuery,
                        // Parameters
                        variables: {
                            email: this.email,
                            password: this.password,
                        },
                    });
                    this.user = data.data.signinUser.user;
                    this.token = data.data.signinUser.token;
                    this.$store.dispatch(LOGIN, { user: this.user, token: this.token });
                    this.$router.push('/');
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
            if (this.password.length < 8) {
                this.errors.push('Password must be at least 8 characters');
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
.signin-container {
    background: white;
    padding: 1.2em 5em 1em 5em;
    ul {
        li {
            text-align: left;
        }
    }
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
