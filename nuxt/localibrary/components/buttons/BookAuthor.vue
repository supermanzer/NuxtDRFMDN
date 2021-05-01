<!--
    localibrary/components/buttons/BookAuthor.vue

    A component that uses a button with a Nuxt router link to display the author
    of a book on the detail view of that book
-->
<template>
   <v-btn
    color="grey"
    nuxt
    text
    :to="{ name: 'authors-id', params: { id: id } }"
    >
        {{authorName}}
    </v-btn>
</template>

<script>
export default {
    name: 'BookAuthor',
    props: {
        id: {type: Number, required: true} // the ID value for this author
    },
    data: () => ({
        author: false
    }),
    computed: {
        authorName() {
            return this.author ? `${this.author.last_name}, ${this.author.first_name}` : ''
        }
    },
    async fetch() {
        this.author = await this.$store.dispatch('library/fetchAction', {type: 'authors', id: this.id})
    }
}
</script>

<style>

</style>