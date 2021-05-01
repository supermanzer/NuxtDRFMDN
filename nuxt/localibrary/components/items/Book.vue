<!--
    localibrary/components/items/Book.vue

    A simple two line item used to display basic information about a book
-->
<template>
    <two-lines>
        <template slot="title">
        <v-btn
            color="primary"
            text
            nuxt
            :to="{ name: 'books-id', params: { id: book.id } }"
        >
            {{ book.title }}
        </v-btn>
        </template>
        <template slot="subtitle">
        {{ book.summary }}
        </template>
    </two-lines>
</template>

<script>
export default {
    name: 'Book',
    props: {
        book: {type: Object, required: true}
    }
}
</script>

<style>

</style>