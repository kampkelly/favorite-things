<template>
    <div>
         <div class="add-favorite-container">
            <h5 class="mb-3">Add A New Favorite Thing</h5>
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
                <div class="form-row metadata-box">
                    <div class="form-group col-md-5">
                        <input type="text" class="form-control metadata-key" id="" placeholder="key (optional)">
                    </div>
                    <div class="form-group col-md-5">
                        <input type="text" class="form-control metadata-value" id="" placeholder="value (optional)">
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
                <span class="text-success">{{categorySuccess}}</span>
                <span class="text-danger">{{categoryError}}</span>
                <div class="form-row new-category-field" v-if="creatingNewCategory">
                    <div class="form-group col-md-6">
                        <input type="text" class="form-control" id="new-category" v-model="newCategoryEntry" placeholder="Enter new category">
                    </div>
                    <div class="form-group col-md-5">
                        <input type="button" class="btn btn-primary mr-2" v-on:click="saveNewCategory" value="save category" v-bind:disabled="disabled">
                        <a href="#" class="text-danger" v-on:click="toggleCategoryField">cancel</a>
                    </div>
                </div>
                <div class="form-row">
                    <div class="form-group col-md-6">
                        <label for="category">Category</label> <br>
                        <v-select class="style-chooser" label="name" placeholder="select category" taggable :options="allCategories" :reduce="name => name.id" v-model="categoryId"></v-select>
                    </div>
                    <div class="form-group col-md-5 add-category">
                        <a href="#" v-on:click="toggleCategoryField" class="">add category <i class="fas fa-plus"></i></a>
                    </div>
                </div>
                <div class="form-group">
                    <button class="btn btn-primary" type="submit" v-bind:disabled="disabled" v-on:click="saveFavorite">Save Favorite Thing</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
// eslint-disable-next-line
import gql from 'graphql-tag';
import { SET_APP_ERROR_MESSAGE } from '../../mutationTypes';

const getCategoriesQuery = gql`query {
  allCategories {
    id
    name
  }
}`;

const addCategory = gql`mutation ($name: String!) {
  createCategory(name: $name) {
    category {
      id
      name
    }
  }
}`;

const saveFavoriteThing = gql`mutation ($title: String!, $categoryId: Int!, $description: String!, $objectMetadata: JSONString!, $ranking: Int!) {
  addFavoriteThing(title: $title, categoryId: $categoryId, description: $description, objectMetadata: $objectMetadata, ranking: $ranking) {
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
            allCategories: [],
            title: '',
            description: '',
            categoryId: '',
            ranking: '',
            metadata: {},
            additionalMetadatas: [],
            errors: [],
            metadataError: '',
            newCategoryEntry: '',
            categoryError: '',
            categorySuccess: '',
            disabled: false,
            creatingNewCategory: false
        }
    },
    apollo: {
        allCategories: {
            query: getCategoriesQuery,
        },
    },
    methods: {
        validateInputs() {
            this.categorySuccess = '';
            if (!this.title.length) {
                this.errors.push('Title cannot be empty');
            }
            if (isNaN(parseInt(this.ranking))) {
                this.errors.push('Ranking must be a number');
            }
            if (!this.categoryId) {
                this.errors.push('Category cannot be empty');
            }
            if (this.description.length && this.description.length < 10) {
                this.errors.push('Description must be up to 10 letters');
            }
            if (this.errors.length) {
                this.disabled = false;
                return false;
            } else {
                return true;
            }
        },
        addMetadataField() {
            this.additionalMetadatas.push(Math.random());
        },
        removeMetadata(index) {
            const removed = this.additionalMetadatas.splice(index,1)
        },
        combineMetadata() {
            const self = this;
            const metadatas = $('.metadata-box');
            const metadata = {};
            metadatas.each(function() {
                const key = $(this).find(".metadata-key").val();
                const value = $(this).find(".metadata-value").val();
                if (key != '' && value != '') {
                    metadata[key] = value
                }
                if ((key != '' && value == '') || (key == '' && value != '')) {
                    self.errors.push('Metadata key must have a value');
                }
            });
            this.metadata = metadata;
        },
        toggleCategoryField() {
            this.categoryError = '';
            this.creatingNewCategory = !this.creatingNewCategory;
        },
        async saveNewCategory() {
            if (!this.newCategoryEntry.length) {
                this.categoryError = 'Category name cannot be empty';
                return true;
            }
            this.disabled = true;
            try {
                const data = await this.$apollo.mutate({
                    mutation: addCategory,
                    variables: {
                        name: this.newCategoryEntry,
                    },
                });
                const newCategory = data.data.createCategory.category;
                this.allCategories.push(newCategory);
                this.categoryError = '';
                this.categorySuccess = 'category added';
                this.creatingNewCategory = false;
            }
            catch(error) {
                this.categorySuccess = '';
                this.categoryError = error.message.split(':')[1];
            };
            this.disabled = false;
        },
        async saveFavorite(event) {
            this.disabled = true;
            this.errors = [];
            event.preventDefault();
            this.combineMetadata();
            const validInputs = this.validateInputs();
            const self = this;
            if (validInputs) {
                try {
                    await self.$apollo.mutate({
                        mutation: saveFavoriteThing,
                        variables: {
                            title: self.title,
                            description: self.description,
                            categoryId: self.categoryId,
                            objectMetadata: JSON.stringify(self.metadata),
                            ranking: self.ranking
                        },
                    });
                    this.$router.push('/favorites');
                }
                catch(error) {
                    this.errors.push(error.message ? error.message.split(':')[1] : 'Server error');
                }
            }
            this.disabled = false;
        },
    }
}
</script>


<style lang="scss">
.add-favorite-container {
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
            font-size: 13px;
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
