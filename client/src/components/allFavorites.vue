<template>
    <div>
        <h5 class="mt-2 mb-3">All Favorites</h5>
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th scope="col">Title</th>
                    <th scope="col">Description</th>
                    <th scope="col">Metadata</th>
                    <th scope="col">Ranking</th>
                    <th scope="col">Category</th>
                    <th scope="col">Update</th>
                    <th scope="col">Delete</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="favorite in getFavoriteThings" v-bind:key="favorite.id">
                    <th scope="row">{{favorite.title}}</th>
                    <td>{{favorite.description}}</td>
                    <td>
                        <li class="" v-for="(key, value) in JSON.parse(favorite.objectMetadata)" v-bind:key="key">
                            {{key}} : {{value}}
                        </li>
                    </td>
                    <td>{{favorite.ranking}}</td>
                    <td>{{favorite.category.name}}</td>
                    <td>Update</td>
                    <td>Delete</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
// eslint-disable-next-line
import gql from 'graphql-tag';

const allFavorites = gql`query {
  getFavoriteThings {
    id
    title
    description
    objectMetadata
    ranking
    createdDate
     category {
      name
    }
  }
}
`;
export default {
    data() {
        return {
            getFavoriteThings: []
        }
    },
    apollo: {
        getFavoriteThings: {
            query: allFavorites,
        },
    },
}
</script>


<style lang="scss" scoped>
    li {
        list-style: none;
    }
</style>
