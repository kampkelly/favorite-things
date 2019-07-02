<template>
    <div>
        <div class="update-favorite-container">
            <h5 class="mb-3">Update A Favorite Thing</h5>
            <ul>
                <li v-for="(error, index) in this.errors" v-bind:key="index" class="text-danger">
                    {{error}}
                </li>
            </ul>
            <form>
                <div class="form-group">
                    <label for="title">Title</label>
                    <input type="text" class="form-control" id="title" v-model="title" placeholder="">
                </div>
                <div class="form-group">
                    <label for="description">Description</label>
                    <textarea class="form-control" id="description" rows="3" draggable="false" v-model="description" placeholder="optional"></textarea>
                </div>

                <h5>Metadata</h5>
                <p>{{metadataError}}</p>
                <div v-for="(value, key) in originalMetadata" v-bind:key="key">
                    <div class="form-row metadata-box">
                        <div class="form-group col-md-5">
                            <input type="text" class="form-control metadata-key" id="" :value="key" placeholder="key (optional)">
                        </div>
                        <div class="form-group col-md-5">
                            <input type="text" class="form-control metadata-value" id="" :value="value" placeholder="value (optional)">
                        </div>
                    </div>
                </div>

                 <!---additional metadatas -->
                <div v-for="(meta, index) in additionalMetadatas" v-bind:key="meta">
                    <div class="form-row metadata-box">
                        <div class="form-group col-md-5">
                            <input type="text" class="form-control metadata-key" id="" placeholder="key (optional)">
                        </div>
                        <div class="form-group col-md-5">
                            <input type="text" class="form-control metadata-value" id="" placeholder="value (optional)">
                        </div>
                        <div class="form-group col-md-1 remove-metadata" v-on:click="removeMetadata(index)">
                            <a href="#" class="text-danger"><i class="fas fa-minus"></i></a>
                        </div>
                    </div>
                </div>
                <!---additional metadatas -->
                <a href="#" v-on:click="addMetadataField" class="add-metadata">add metadata <i class="fas fa-plus"></i></a>

                <div class="form-group">
                    <label for="ranking">Ranking</label>
                    <input type="number" class="form-control" id="ranking" min="1" max="20" v-model="ranking" placeholder="">
                </div>
                <div class="form-group">
                    <button class="btn btn-primary" type="submit" v-bind:disabled="disabled" v-on:click="updateFavorite">Update Favorite Thing</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
// eslint-disable-next-line
import gql from 'graphql-tag';
import { SET_APP_ERROR_MESSAGE } from '../../mutationTypes';

const singleFavorite = gql`query($id: Int!) {
  getSingleFavoriteThing(id: $id) {
    id
    title
    description
    objectMetadata
    ranking
    categoryId
  }
}
`;

const updateFavoriteThing = gql`mutation ($id: Int!, $title: String!, $description: String!, $objectMetadata: JSONString!, $ranking: Int!) {
  updateFavoriteThing(id: $id, title: $title, description: $description, objectMetadata: $objectMetadata, ranking: $ranking) {
    favoriteThing {
      id
      title
      objectMetadata
      userId
      ranking
    }
  }
}
`;

export default {
  data() {
    return {
      getSingleFavoriteThing: {},
      allCategories: [],
      title: '',
      description: '',
      categoryId: '',
      ranking: '',
      metadata: {},
      originalMetadata: {},
      additionalMetadatas: [],
      errors: [],
      metadataError: '',
      disabled: false,
    };
  },
  apollo: {
    getSingleFavoriteThing: {
      query: singleFavorite,
      variables() {
        return {
          id: this.$route.params.id,
        };
      },
      skip() {
        return this.skipQuery;
      },
    },
  },
  created() {
    this.fetchFavoriteThing();
  },
  methods: {
    async fetchFavoriteThing() {
      this.$apollo.queries.getSingleFavoriteThing.skip = false;
      let favoriteThing = {};
      try {
        favoriteThing = await this.$apollo.queries.getSingleFavoriteThing.refetch();
      } catch (err) {
        this.$store.dispatch(SET_APP_ERROR_MESSAGE, err.message.split(':')[1]);
      }
      this.title = favoriteThing.data.getSingleFavoriteThing.title;
      this.description = favoriteThing.data.getSingleFavoriteThing.description;
      this.originalMetadata = JSON.parse(favoriteThing.data.getSingleFavoriteThing.objectMetadata);
      this.ranking = favoriteThing.data.getSingleFavoriteThing.ranking;
      this.categoryId = favoriteThing.data.getSingleFavoriteThing.categoryId;
    },
    validateInputs() {
      if (!this.title.trim().length) {
        this.errors.push('Title cannot be empty');
      }
      if (isNaN(parseInt(this.ranking))) {
        this.errors.push('Ranking must be a number');
      }
      if (!this.categoryId) {
        this.errors.push('Category cannot be empty');
      }
      if (this.description.trim().length && this.description.trim().length < 10) {
        this.errors.push('Description must be up to 10 letters');
      }
      if (this.errors.length) {
        this.disabled = false;
        return false;
      }
      return true;
    },
    addMetadataField() {
      this.additionalMetadatas.push(Math.random());
    },
    removeMetadata(index) {
      const removed = this.additionalMetadatas.splice(index, 1);
    },
    combineMetadata() {
      const self = this;
      const metadatas = $('.metadata-box');
      const metadata = {};
      metadatas.each(function () {
        const key = $(this).find('.metadata-key').val();
        const value = $(this).find('.metadata-value').val();
        if (key != '' && value != '') {
          metadata[key] = value;
        }
        if ((key != '' && value == '') || (key == '' && value != '')) {
          self.errors.push('Metadata key must have a value');
        }
      });
      this.metadata = metadata;
    },
    async updateFavorite(event) {
      this.disabled = true;
      this.errors = [];
      event.preventDefault();
      this.combineMetadata();
      const validInputs = this.validateInputs();
      const self = this;
      if (validInputs) {
        try {
          const data = await self.$apollo.mutate({
            mutation: updateFavoriteThing,
            variables: {
              id: self.$route.params.id,
              title: self.title,
              description: self.description,
              objectMetadata: JSON.stringify(self.metadata),
              ranking: self.ranking,
            },
          });
          this.$router.push('/favorites');
        } catch (error) {
          this.errors.push(error.message ? error.message.split(':')[1] : 'Server error');
        }
      }
      this.disabled = false;
    },
  },
};
</script>

<style lang="scss" scoped>
.update-favorite-container {
    width: 60%;
    margin: auto;
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
        .add-category {
            padding-top: 37px;
            font-size: 12px;
        }
        .add-metadata {
            font-size: 13px;
        }
        .remove-data {
            padding-top: 37px;
        }
    }

}
</style>
