<template>
    <div>
        <h5 class="mt-2 mb-3">Category Favorites</h5>
        <ul class="list-group">
            <li class="list-group-item" v-for="(category, index) in getCategoriesAndFavorites" v-on:click="favoriteIndex = index" v-bind:key="category.id">
                <span href="#">{{category.name | capitalize}}</span>
                 <div v-show="favoriteIndex == index">
                    <table class="table table-bordered">
                    <thead>
                        <tr>
                            <th scope="col">Title</th>
                            <th scope="col">Description</th>
                            <th scope="col">Metadata</th>
                            <th scope="col">Ranking</th>
                            <th scope="col">Update</th>
                            <th scope="col">Delete</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="favorite in favorites(category)" v-bind:key="favorite.id">
                            <th scope="row">{{favorite.title}}</th>
                            <td>{{favorite.description}}</td>
                            <td>
                                <li class="" v-for="(value, key) in JSON.parse(favorite.objectMetadata)" v-bind:key="key">
                                    {{key}} : {{value}}
                                </li>
                            </td>
                            <td>{{favorite.ranking}}</td>
                            <td><router-link :to="`/favorites/update/${favorite.id}`">All favorites</router-link></td>
                            <td>Delete</td>
                        </tr>
                    </tbody>
                </table>
                </div>    
            </li>
        </ul>
    </div>
</template>

<script>
// eslint-disable-next-line
import gql from 'graphql-tag';

const allFavoritesByCategory = gql`query {
  getCategoriesAndFavorites {
    id
    name
    favoriteThings {
      id
      title
      description
      objectMetadata
      ranking
      createdDate
    }
  }
}

`;
export default {
    data() {
        return {
            getCategoriesAndFavorites: [],
            favoriteIndex: -1
        }
    },
    apollo: {
        getCategoriesAndFavorites: {
            query: allFavoritesByCategory,
        },
    },
    methods: {
        favorites(category) {
            return category.favoriteThings;
        }
    },
    filters: {
        capitalize: function (value) {
            if (!value) return ''
            value = value.toString()
            return value.charAt(0).toUpperCase() + value.slice(1)
        }
    }
}
</script>

<style lang="scss" scoped>
    li {
        list-style: none;
    }
    ul {
        li {
            cursor: pointer;
            span {
                color: #61B7FF;
                float: left;
            }
        }
    }
</style>
