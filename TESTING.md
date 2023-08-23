# Testing

## Manual Testing

Usability was tested with the below user acceptance testing, sent to new users to ensure testing from different users, on different browsers to ensure issues were caught and where possible fixed during development.

### User Actions

| User Action            | Expected Result                          | Requirement Met |
|------------------------|------------------------------------------|-----------------|
| Register an account   | Successfully registered and logged in   | Yes             |
| View reservations      | Accessing reservations page lists reservations | Yes             |
| Make a reservation    | Successfully making a reservation       | Yes             |
| Edit a reservation     | Successfully editing an existing reservation | Yes             |
| Cancel a reservation   | Successfully canceling an existing reservation | Yes             |
| View restaurant's menu | Accessing menu page displays menu categories | Yes             |
| Add new menu items     | Successfully adding a new menu item     | Yes             |
| Edit menu items        | Successfully editing an existing menu item | Yes             |
| Delete menu items      | Successfully deleting an existing menu item | Yes             |
| View and edit reservations for preparation | Accessing admin reservations page for management | Yes             |

### User Stories

| User Story            | Expected Result                          | Requirement Met |
|-----------------------|------------------------------------------|-----------------|
| As a Site User, I can register an account so that I can make a reservation with my user details. | Successfully registered and logged in | Yes             |
| As a site user, I can view my reservations online to be reminded of the details of my reservations. | Accessing reservations page lists reservations | Yes             |
| As a site user, I can make an online reservation on the site to book a table securely in advance. | Successfully making a reservation | Yes             |
| As a site user, I can edit my reservation online to allow for my changing schedule. | Successfully editing an existing reservation | Yes             |
| As a site user, I can delete my reservation online to allow for my changing schedule. | Successfully canceling an existing reservation | Yes             |
| As a site user, I can view the restaurant's menu to know what to expect when I make a reservation. | Accessing menu page displays menu categories | Yes             |
| As a site administrator, I can add new menu items to keep my clients up to date with the changing menu. | Successfully adding a new menu item | Yes             |
| As a site administrator, I can edit menu items to allow for changes in the description and pricing. | Successfully editing an existing menu item | Yes             |
| As a site administrator, I can delete a menu item to keep my online menu up to date. | Successfully deleting an existing menu item | Yes             |
| As a site administrator, I can view and edit all reservations on a given day for table preparation. | Accessing admin reservations page for management | Yes             |

## Validation

### HTML Validation:

- HTML validation was done by using the official [W3C](https://validator.w3.org/) validator. This checking was done manually by copying the view page url and pasting it into the validator.

- [Full HTML Validation Report](documentation/validation/html)

- There were only errors around using a table heading with a colspan of 2, these are standard html tags however.

### CSS Validation:

- [Full CSS Validation Report](documentation/validation/css_validator.png)

- No errors or warnings were found when passing through the official [W3C (Jigsaw)](https://jigsaw.w3.org/css-validator/#validate_by_uri) validator.


### Python Validation:
- [Full Python Validation Report](documentation/validation/python)

- No errors were found when the code was passed through this python checker [online validation tool](https://www.pythonchecker.com/). According to the reports, the code is [Pep 8-compliant](https://legacy.python.org/dev/peps/pep-0008/). This checking was done manually by copying python code from all the files and pasting it into the validator. Only errors were that forward slashes needed white spaces even though it is a url. As well as long python code.