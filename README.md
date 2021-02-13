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
6. Built out Vuex store methods for working with the resources exposed by the REST API
7. Created Vuetify table component to allow server side pagination, ordering, and searching
8. Built List and Detail pages for both Books and Authors
9. Configured project to use @nuxt/auth on the front-end and SimpleJWT on the back-end for token authentication of users.

## Future Goals

These are the areas of building a fully featured app I would like to address, beyond just a basic SPA front-end

- Authentication for library patrons using Web Tokens (DRF - SimpleJWT) and `@nuxt/auth` module <- IN PROGRESS!
- Design workflow for partons to register with the local library
- Design a notification system based on due dates for patrons who have reserved books that are due back
- Deploy my custom approach to using Django templates with AJAX requests using Vue and Axios
- Implement Nuxt composition API refactoring for pages
- Customize Nuxt.js error pages
- Develop a less cookie-cutter style
- Use the data returned by an OPTIONS request to dynamically build table headers and forms in Nuxt.js <- In progress!
- Utilize the toast plugin properly to return messages to users. <- IN PROGRESS
- Add necessary config files to deploy back end to GCP and AWS cloud providers, front-end to Netlify.

## Changes/Challenges

While working through this project I try to consider all the features I would find useful as a library patron and a library staff member. When I come across something like that I tend to deviate from the proscribed approach used in the MDN tutorial. I will try to keep a record of each of these cases as much for my own benefit as for anyone else.

### Book Checkout

The [MDN Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication), in the section on authentication, simply suggests that you add a `ForeignKey` to the `BookInstance` model, essentially tracking the current borrower of any given copy. However I decided that I wanted to have a record of each time a library patron checked out a book. I created a [custom through model](https://docs.djangoproject.com/en/3.1/topics/db/models/#extra-fields-on-many-to-many-relationships) that would allow me to keep track of the Many-to-Many relationship between User and BookInstance. A benefit of using the custom model approach is I can add additional fields to store data. Take a look at the model definition below:

```python
class BorrowedCopies(models.Model):
    """Defining a custom model to relate the borrowing of a book instance to a library patron"""
    patron = models.ForeignKey(User, on_delete=models.CASCADE)
    copy = models.ForeignKey(BookInstance, on_delete=models.CASCADE)
    date_checked_out = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    date_returned = models.DateTimeField(null=True, blank=True)
```

I want to be able to keep a record of when each copy was checked out (date/time), due, and when it was returned. I may implement a model to store library policy data like late fees and the create a custom model annotation for tracking the fees associated with any overdue book. Although, then when the library staff adjust their fees it would appear to retroactively change the fees for past overdue books. Perhaps simply a `fine` field that would be set once the patron returns the book, based on the defined per day fee and the difference between the `due_date` and the `date_returned`.
