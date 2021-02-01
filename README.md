# Django REST Framework - Nuxt.js - MDN Local Library

## Purpose

Once again I building a version of the Local Library [Django](https://www.djangoproject.com/) app created by working through the [MDN Django tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django). In this case I am extending the application through the creation of a REST API that will serve all the data to a JAMStack front end that I am building using the [Nuxt.js](https://nuxtjs.org/) meta-framework. This is another practice app to test out different ideas and approaches to building full stack applications that are nonetheless modern SPAs.

## Approach

I am using Docker and Docker Compose to encapsulate all the aspects of this application as services. This is how I am currently developing professionally and I want try and keep much of the infrastruture the same. I am using the Django development server at present but may consider adding a service for an NGINX reverse proxy server to better approximate my professional development approach.

## Outcome

Ultimately I would like to build a user interface that any community library would envy. The Nuxt.js SPA is intended to be an interface for end-users. I will be sticking to using the auto-generated Django admin site as the interface intended for Library staff. Although I may try to spruce it up a bit with some Vue.

## Motivation

The MDN tutorial broadened my understanding of application development in Django beyond what I had gathered through other sources. After working through it, I finally felt confident enough in my understanding of the framework to use it professionally. I have a ridiculous amount of fun developing with the Django framework and I'm always looking for ways to enhance my skillset.

## My Steps

In case anyone stumbles across this repo and thinks it would make a fun project to attempt, here are the steps I've taken.

1. Implement complete app structure in `docker-compose.yml` and write the necessary `Dockerfile`s
2. Work through the MDN Django tutorial as written for parts 1 - 4. Well I did change the database approach as well as working within Docker containers but that is easily copied from the aforementioned files.
3. Create an app for handling the REST API: `./manage.py createapp api`. This is mainly just used to namespace the API URLs so far but I like to take this approach.
4. Create `api_views.py` and `serializers.py` in the Catalog app. I take this approach so that all logic that pertains to that app and its models are contained there. If I wind up using that app (or any other similarly design app) in another project I don't have to track down where the DRF Viewsets or Seriliazers are defined. If the new app isn't employing a REST API, these files don't hurt anything.
5. Starting with the [MDN Django tutorial part 5](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page), any work regarding building a non-admin interface will be done using the Nuxt.js front-end. This is where things start to get new and interesting (for me).

## Future Goals

These are the areas of building a fully featured app I would like to address, beyond just a basic SPA front-end

- Authentication for library patrons using Web Tokens (DRF - SimpleJWT) and `@nuxt/auth` module
- Design workflow for partons to register with the local library
- Design a notification system based on due dates for patrons who have reserved books that are due back
- Deploy my custom approach to using Django templates with AJAX requests using Vue and Axios
- Implement Nuxt composition API refactoring for pages
- Customize Nuxt.js error pages
- Develop a less cookie-cutter style
- Use the data returned by an OPTIONS request to dynamically build table headers and forms in Nuxt.js
