# Django REST Framework - Nuxt.js - MDN Local Library

## Purpose

Once again I building a version of the Local Library [Django](https://www.djangoproject.com/) app created by working through the [MDN Django tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django). In this case I am extending the application through the creation of a REST API that will serve all the data to a JAMStack front end that I am building using the [Nuxt.js](https://nuxtjs.org/) meta-framework. This is another practice app to test out different ideas and approaches to building full stack applications that are nonetheless modern SPAs.

## Approach

I am using Docker and Docker Compose to encapsulate all the aspects of this application as services. This is how I am currently developing professionally and I want try and keep much of the infrastruture the same. I am using the Django development server at present but may consider adding a service for an NGINX reverse proxy server to better approximate my professional development approach.

## Outcome

Ultimately I would like to build a user interface that any community library would envy. The Nuxt.js SPA is intended to be an interface for end-users. I will be sticking to using the auto-generated Django admin site as the interface intended for Library staff. Although I may try to spruce it up a bit with some Vue.
