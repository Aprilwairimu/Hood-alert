##  7220 Neighbourhood

This is a Neighbourhood Web-App that helps you connect with people who are living in the same region. Residents of the same region can communicate with each other. Health and police department contact information is easily accessible. The user can also see nearby businesses.

## Project preview
![7220 Neighbourhood](./static/css/images/7220%20screenshot.png)

## contributors

Written by: 
George Gichuru.
April Wairimu

## Installation

Clone the repository
Create a virtual environment
Install Django and other requirements in my requirements.txt file in your repository folder
Run the IP address on the browser

## User Stories

These are the behaviours/features that the application implements for use by a user.

As a user I would like to:


- Sign in with the application to start using.
- Set up a profile about me and a general location and my neighborhood name.
- Find a list of different businesses in my neighborhood.
- Find Contact Information for the health department and Police authorities near my neighborhood.
- Create Posts that will be visible to everyone in my neighborhood.
- Change My neighborhood when I decide to move out.
- Only view details of a single neighborhood.


## Behaviour Driven Development

| Behavior                | Input description  | Output description                                    |
| ----------------------- | ------------------ | ----------------------------------------------------- |
| Login, Signup or Logout | Username, Password | User will be either loggedin, registered, loggedout   |
| upload a business       | name, desc, image  | The business will be posted to the Myhood page |
| Join hood |  N/A |  User wiil be added as a member  |
| Create a new hood | new hood  |Add hood details eg name, location, police number | 
| New notice | Whats new | Title and details of whats new in the neighbourhood |
| Check all members from your hood | name and location | members from your block |

## SetUp / Installation Requirements

### Prerequisites

- python3.10.4
- pip
- virtualenv

## Running the Application

- Creating the virtual environment

        $ python3.10.4 -m venv --without-pip env
        $ source env/bin/activate

- Installing Django

        $ python3.10.4 -m pip install Django
        $ python3.10.4 -m pip install djangorestframework
        $ python3.10.4 -m pip install psycopg2

## Technologies Used

- Python3.10.4
- Django
- Bootstrap4
- Javascript
- Html
- Css

Live Link: > https://django-7220app.herokuapp.com/

## Contact Information

For any questions or contributions Email at:
 > gichurugeorge092@gmail.com
 > wairimuapril@gmail.

License
MIT License

Copyright (c) [2022] [**George Gichuru**]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.