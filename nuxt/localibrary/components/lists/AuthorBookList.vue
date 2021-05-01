<!--
    locallibrary/components/lists/BookList.vue

    A simple list of Book items.  This components hanldes the fetching of
    all books related to a given author.
-->
<template>
    <div>
        <template v-for="book in books">
            <book :book="book" :key="book.id"></book>
        </template>
    </div>
</template>

<script>
import Book from '../items/Book.vue'
export default {
  components: { Book },
    name: 'AuthorBookList',
    props:{
        id: {type: Number, required: true} // Author ID
    },
    data: () => ({
        books: []
    }),
    async fetch() {
        const args = {suffix: 'books', type: 'authors', id: this.id}
        this.books = await this.$store.dispatch('library/fetchAction', args)
    }
}
</script>

<style>

</style>