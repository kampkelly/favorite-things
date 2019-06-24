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
                        <li class="" v-for="(value, key) in JSON.parse(favorite.objectMetadata)" v-bind:key="key">
                            {{key}} : {{value}}
                        </li>
                    </td>
                    <td>{{favorite.ranking}}</td>
                    <td>{{favorite.category.name}}</td>
                    <td><router-link :to="`/favorites/update/${favorite.id}`" class="text-warning">Update</router-link></td>
                    <td><a href="#" class="text-danger" v-on:click="deleteFavorite(favorite.id)">Delete</a></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
// eslint-disable-next-line
import gql from 'graphql-tag';
import Swal from 'sweetalert2';

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
                await self.$apollo.queries.getFavoriteThings.refetch();
            }
        }
    }
}
</script>


<style lang="scss" scoped>
    li {
        list-style: none;
    }
</style>
