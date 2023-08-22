# Vegan Burgers Website

![Website Screenshot](link-to-image)

## About

The Vegan Burgers website is a platform designed to provide restaurant clients with the opportunitity to explore and interact with the digital space of our restaurant. From making reservations to exploring a variety of delicious vegan burger options, this website aims to cater to the diverse tastes of food enthusiasts.

## User Experience Design

### Strategy

The primary strategy behind Vegan Burgers is to create a user-friendly interface that enables users to effortlessly navigate through various features. The website is designed to offer an intuitive and engaging experience, encouraging users to explore the menu and make reservations.

### Target Audience

The target audience of the Vegan Burgers website includes vegans, vegetarians, and individuals interested in exploring plant-based food options. It's designed to cater to food lovers looking for healthier and sustainable alternatives.

### User Stories

1. As a Site User I can register an account so that I can make a reservation with my user details.
2. As a site user, I can view my reservations online to be reminded of the details of my reservations.
3. As a site user, I can make an online reservation on the site to book a table securely in advance.
4. As a site user, I can edit my reservation online to allow for my changing schedule.
5. As a site user, I can delete my reservation online to allow for my changing schedule.
6. As a site user, I can view the restaurant's menu to know what to expect when I make a reservation
7. As a site administrator, I can add new menu items to keep my clients up to date with the changing menu.
8. As a site administrator, I can edit menu items to allow for changes in the description and pricing of menu items.
9. As a site administrator, I can delete a menu item to keep my online menu up to date.
10. As a site administrator, I can view and edit all reservations on a given day to prepare the tables for them beforehand.

## Technologies Used

### Languages:
    + [Python](https://www.python.org/downloads/release/python-385/): the primary language used to develop the server-side of the website.
    + [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): the markup language used to create the website.
    + [CSS](https://developer.mozilla.org/en-US/docs/Web/css): the styling language used to style the website.
- ### Frameworks and libraries:
    + [Django](https://www.djangoproject.com/): python framework used to create all the backend logic of the website.
- ### Databases:
    + [SQLite](https://www.sqlite.org/): was used as a database during the development stage of the website.
    + [PostgreSQL](https://www.postgresql.org/): the database used to store all the data.
- ### Other tools:
    + [Github Projects and kanban boards](https://github.com/lexach91/Django-social-network-PP4/projects) was used to track the progress of the project in general and of every application in the project.
    + [Git](https://git-scm.com/): the version control system used to manage the code.
    + [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.
    + [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images and other media.
    + [Psycopg2](https://www.python.org/dev/peps/pep-0249/): the database driver used to connect to the database.
    + [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.
    + [GitHub](https://github.com/): used to host the website's source code.
    + [Heroku](https://www.heroku.com/): used to deploy the website.
    + [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
    + [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
    + [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
    + [PEP8](https://pep8.org/): was used to validate Python code for the website.

## Features

### Home Page

The home page welcomes users with an enticing display of our main seller (Vegan Burgers) and encourages them to explore the menu or make a reservation.

### Make Reservation

Users can effortlessly book a table for their desired date time and guest number, providing a seamless reservation experience.

### Reservations View

Users can view their upcoming and past reservations. They can also edit or cancel reservations as needed.

### View Menu

The menu page showcases a variety of menu item options, put in four different menu categories.

### Admin Reservation Dashboard

Restaurant staff have access to a dedicated dashboard that allows them to manage reservations efficiently.

### Add, Edit, and Delete Menu Items

Admins can add new menu items, modify existing ones, or remove items that are no longer offered.

## Future Improvements

### Editing Opening Hours Dynamically

Enhance user experience by dynamically updating opening hours based on specific days and holidays, which will affect date/time validation with user reservations.

### Logging in as a Guest or with a Social Account

Offer users the convenience of logging in as a guest or using their social media accounts for a more personalized experience.

## Design

The application's design draws inspiration from Material Design principles, prioritizing a user-friendly interface. With a focus on simplicity, the design ensures a seamless and intuitive experience for users.

### Wireframes

Here is the [initial wireframe](https://app.visily.ai/projects/9f0e1a72-8817-4de8-ae91-0b7354b33088/boards/522417) created on Visiliy.ai.

## Information Architecture

### Database

The database was created on PostgreSQL.

#### Data Modelling

##### Reservation Model

| Name     | Database Key | Field Type    | Validation                     |
|----------|--------------|---------------|--------------------------------|
| user     | user         | ForeignKey    | User, on_delete=models.CASCADE |
| date     | date         | DateField     |                                |
| time     | time         | TimeField     |                                |
| guests   | guests       | PositiveIntegerField |                          |


##### Menu Model
 | Name        | Database Key | Field Type       | Validation                         |
|-------------|--------------|------------------|-----------------------------------|
| name        | name         | CharField        | max_length=50                     |
| description | description  | CharField        | max_length=300                    |
| price       | price        | DecimalField     | max_digits=5, decimal_places=2    |
| category    | category     | CharField        | max_length=10, choices=CATEGORY_CHOICES, default=BURGERS |
| item_image  | item_image   | CloudinaryField  | default='placeholder'             |


##### Allauth User Model

The user model was created using Django-allauth.
The user model was then migrated to PostgreSQL.

## Deployment and Acknowledgments

### Deployment and Testing
The app was deployed to Heroku. Please refer to the TESTING.md file for manual, automatic and validation documentation.

### Acknowledgements
I would like to thank my Mentor, Alex Konovalov, for his detail oriented work and his consistent support. 
