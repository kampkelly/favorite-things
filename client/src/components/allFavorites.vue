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
                        <a href="#" v-on:click="showMetadata(JSON.parse(favorite.objectMetadata))">View</a>
                    </td>
                    <td>{{favorite.ranking}}</td>
                    <td>{{favorite.category.name}}</td>
                    <td><router-link :to="`/favorites/update/${favorite.id}`" class="text-warning">Update</router-link></td>
                    <td><a href="#" class="text-danger" v-on:click="deleteFavorite(favorite.id)">Delete</a></td>
                </tr>
            </tbody>
        </table>
        <p class="no-favorite-text" v-if="getFavoriteThings && !getFavoriteThings.length">You have not added any favorite thing yet.<br> Click the plus sign to add one.</p>
    </div>
</template>

<script>
// eslint-disable-next-line
import gql from 'graphql-tag';
import Swal from 'sweetalert2';
import { SET_APP_ERROR_MESSAGE } from '../mutationTypes';

const swalWithBootstrapButtons = Swal.mixin({
    customClass: {
        confirmButton: 'btn btn-danger',
        cancelButton: 'btn btn-danger'
    },
    buttonsStyling: false,
});

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

const deleteFavorite = gql`mutation  ($id: Int!){
  deleteFavoriteThing(id: $id) {
    favoriteThing {
      id
      title
      ranking
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
    async created() {
        try {
            await this.$apollo.queries.getFavoriteThings.refetch();
        } catch(err) {
            this.$store.dispatch(SET_APP_ERROR_MESSAGE, err.message.split(':')[1]);
        };
    },
    methods: {
        async deleteFavorite(id) {
            const self = this;
            const result = await Swal.fire({
                title: 'Are you sure?',
                text: "You won't be able to revert this!",
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Yes, delete it!'
            });
            if (result.value) {
                try {
                    await self.$apollo.mutate({
                        mutation: deleteFavorite,
                        variables: {
                            id: id,
                        },
                    });
                    Swal.fire(
                        'Deleted!',
                        'Favorite thing deleted',
                        'success'
                    );
                } catch(err) {
                    swalWithBootstrapButtons.fire(
                        'Cancelled',
                        'Favorite thing could not be deleted',
                        'error'
                    )
                    return;
                };
                try {
                    await self.$apollo.queries.getFavoriteThings.refetch();
                } catch(err) {
                    this.$store.dispatch(SET_APP_ERROR_MESSAGE, err.message.split(':')[1]);
                };
            }
        },
        showMetadata(metadata) {
            let html = '';
            let swalHtml = '';
            const keys = Object.keys(metadata);
            for (let i = 0; i < keys.length; i++) {
                html += `<tr><td>${keys[i]}</td>
                    <td>${metadata[keys[i]]}</td></tr>`;
            }
            if (!keys.length) {
                swalHtml = 'no metadata';
            } else {
                swalHtml = `
                <table class="table">
                <thead class="thead-dark">
                    <tr>
                        <th scope="col">key</th>
                        <th scope="col">value</th>
                    </tr>
                </thead>
                <tbody>
                    ${html}
                </tbody>
                </table>`;
            }
            Swal.fire({
                title: '<h6>Metadata</h6>',
                html: swalHtml,
                focusConfirm: false,
                confirmButtonText:
                    'Ok',
                confirmButtonAriaLabel: 'Thumbs up, great!',
                showCancelButton: false
            });
        }
    }
}
</script>


<style lang="scss" scoped>
    li {
        list-style: none;
    }
</style>
