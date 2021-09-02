# Baba Gifts

View the live project [here](http://babagifts.herokuapp.com/)

This is an eCommerce store with Stripe integrated payment processing. It is fully responsive and accessible on a range of devices, making it easy to navigate for potential clients. It was created using Django framework and hosted on Heroku.

## User Experience (UX)
### Developer's Goals
It is a final project of the Full Stack Web Development program provided by Code Institute. It's main purpose is to learn how to build e-commerce websites using Django.  

### Site Owner Goals
The primary goal of the site owner is to nicely present items for sale and subsequently sell them. Site owner would need an easy access
to product management in order to be able to add, update, or delete products. 

### Customers' goals
The main audience for this website consists of yound parents and their close family or friends who would like to purchase unique items 
for babies. They value quality and craftmanship and don't mind paying more for handmade products.

### User stories
As a/an .. | I want to be able to ..
--------|------------------------
First time user | easily understand the main purpose of the site and learn more about the company.
First time user | easily navigate throughout the site to find content.
Shopper | see a list of products available for purchase.
Shopper | see each product in more detail.
Shopper | add product or multiple products to basket.
Shopper | see products in my basket.
Shopper | easily see the total of my purchases at any time.
Shopper | update my basket (quantity, sizes, etc).
Shopper | delete products from basket.
Shopper | go to checkout and see a summary of the products I am buying.
Shopper | purchase products without creating an account.
Shopper | get confirmation of my purchase.
Shopper | save my details for future purchases.
Registered user | update my saved information.
Registered user | delete my account.
Registered user | see my previous purchases.
Registered user | save items to a wishlist.
Registered user | see my wishlist and delete items from it.
Admin | add new, edit or delete products.
Admin | add new, edit or delete categories.

### Design
* #### Color scheme
    The following color pallete was created using [Coolors](https://coolors.co/) I chose soft pinkish colors to emphasize 
    the theme and stimulate purchases.
    ![color-pallete](static/images/color-pallete.png)

* #### Typography
    This project uses Montserrat and Style Script fonts, provided by [Google Fonts](https://fonts.google.com/)

* #### Imagery 
    Most of the pictures are from private collections, while some were downloaded from [Pexels](https://www.pexels.com/)

* #### Icons
    Icons are used throughout this website in an attempt to increase UX design where possible. All icons were taken
    from [FontAwesome](https://fontawesome.com/)

### Wireframes
* Wireframes for large screens - [view](https://github.com/irasan/babagifts/blob/master/assets/wireframes/desktop_view.pdf)
* Wireframes for medium screens - [view](https://github.com/irasan/babagifts/blob/master/assets/wireframes/tablet_view.pdf)
* Wireframes for small screens - [view](https://github.com/irasan/babagifts/blob/master/assets/wireframes/phone_view.pdf)


## Features
### Existing Features
* The navbar contains a logo(name) on top left hand corner to redirect to the landing page. Different site sections (Home, Products, Subscriptions, About and Contact) are placed in the center. In the right corner three icons are displayed: profile, search and shopping bag. Profile icon has a dropdown submenu which 
changes depending on user being logged in or not. If the user is not logged the account submenu will show Register and Login links. If the user is logged in, he'll see Profile and Logout links. If a superuser is logged in, account submenu will show 3 links: Product Management,Profile, and Logout. Search input field will appear when clicking on search icon. It allows to search products and subscriptions. Shopping bag dispays quantity of the items currently put there.  
* The footer shows links to the following pages: Home, F.A.Q., Register, Login, Profile, and social media icons. 
* User authentication: users can register their profiles, log in and log out. 
* On the profile page users can see their default info if any and change it. Subscriptions and past orders will also be displayed. There's also a button to user's wishlist. 
* Any user can browse different products and subscriptions.
* Logged in users can save products to wishlist and see if those products have already been saved (red heart icon will indicate this)
* Any user can buy different products, while subscriptions are only available to registered users.
* Any user (logged in or not) can checkout securely.
* Any user can see confirmations / error messages when completing actions on the website.
* Any user can receive confirmation emails for order when compliting order form during checkout.
* The admin can add, update and remove products via admin page or via website.
* Any user can send a message to site owners through contact page.

### Other features include:
* Stripe Integration.
* Webhooks.
* Admin Panel.
* Error Handling.
* Payment Error Capturing - Checkout first creates an order instance in the database, before trying to checkout, this way a user will not get charged multiple times if checkout page is refreshed etc.
* Responsive Design.

### Features left to implement
* Product rating
* Additional info messages for users.


## Technologies used
### Languages:
* HTML
* CSS
* Python
* JavaScript.

### Tools 
* [GitPod](https://gitpod.io/) for creating the project;
* [GitHub](https://github.com/) for version control;
* [PIP](https://pypi.org/project/pip/) for installation of tools needed in this project;
* [Heroku](https://www.heroku.com/) and Postgres database for deployment;
* [Balsamiq](https://balsamiq.com/) was used to create wireframes for the project;
* [Favicon generator](https://www.favicon-generator.org/) was used to generate the favicon;
* [Am I Responsive](http://ami.responsivedesign.is/) to create the images in this readme file of each page displayed on different screen sizes.
* [Stripe](https://stripe.com/) is used to handle payments for the website.
* [AWS S3](https://aws.amazon.com/) for storing static files.

### Libraries
* [FontAwesome](https://fontawesome.com/) to provide icons;
* [Google Fonts](https://fonts.google.com/) to style website's fonts;
* [JQuery](https://jquery.com/) to simplify DOM manipulation;
* [Jinja](https://jinja.palletsprojects.com/) to simplify displaying data from the backend of this project smoothly and effectively in html;
* [Bootstrap](https://getbootstrap.com/) to simplify styling of the website and make it responsive easily;
* [Django](https://www.djangoproject.com/) to build the project.


## Information Architecture
### Database Choice
The site is linked with the SQlite3 database in development and PostgreSQL in production to allow users to easily obtain information needed. Static files are hosted on AWS.

### Collections Data Structure
This website relies on 2 different collections - Products and Subscriptions. 


## Testing
### Testing Using Validators
Upon completion of the writing process, developer used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/),
[W3C MarkUp Validation Service](https://validator.w3.org/), and [PEP8 online](http://pep8online.com/) to check the validity of the code. 
![CSS validation](https://github.com/irasan/read-to-me/blob/master/assets/readme-images/css-validated.png)
![JS validation](https://github.com/irasan/read-to-me/blob/master/assets/readme-images/js.png)
![PEP8 validation](https://github.com/irasan/read-to-me/blob/master/assets/readme-images/pep8.png)

### Manual Testing
The website was continuously tested on emulated large and small screens when writing the code. 
Manual testing was used to test navigation, responsiveness on different screen sizes, database operations 
(Create, Read, Update and Delete) and application functions.

### Client Stories Testing
All client stories developed in the beginning of the project were tested. Only two of them were not fulfilled:
* As a shopper I want easily see the total of my purchases at any time - the total quantity was replaced with items count
in the shopping bag. Its is always seen beside the bag icon in the navbar.
* As a registered user I want to be able to delete my account - this was left for future development.

#### Test cases
Here's a list of some test cases that were done (a small part of them):
1. A user can register an account with unique username - Pass;
1. A user cannot register an account with a username that already exists in the database - Pass;
1. Registered user can login and logout using their credentials - Pass;
1. Registered user can save their default info to profile - Pass;
1. User can see a list of products - Pass;
1. User can go to product page and see it's details - Pass; 
1. User can add products to shopping bag - Pass;
1. User can see items in the shopping bag - Pass;
1. User can update quantity or delete items from the shopping bag - Pass;
1. Delivery costs are calculated correctly - Pass;
1. Logged in user can make a purchase - Pass;
1. Anonymous user can make a purchase - Pass;
1. User can see a list of subscriptions - Pass;
1. Only registered users can buy a subscription - Pass;
1. Registered user can add products to a wishlist on the main product page or on the product details page - Pass;
1. Registered user can see what items on the main product page are already in the wishlist - Pass;
1. Registered user can see items in the wishlist on the wishlist page - Pass;
1. Anonymous user cannot create a wishlist, but can see such an option - Pass; 
1. User can send email using contact form - Pass;
1. Admin can add and update products/subscriptions through website - Pass;
1. Admin can add and update products/subscriptions in the admin panel - Pass;
1. Admin can delete products with a prompt for confirmation - Pass;
1. User can search products and subscriptions - Pass; 
1. All links are valid and redirect to the proper page - Pass.

### Testing on Different Browsers and Devices
The website was tested and proved to be issue-free on the following browsers:
* Chrome;
* Edge;
* Firefox;
* Safari.

The website was also tested on an IOS (Iphone 10) and Android (Pixel 4) devices. There were detected a few issues, in particular:
* contact form was not centered;
* Shop now button on the home page was too big;
* subscription page was not displayed nicely with some extra margins and poor centering;
All issues stated above were addressed and fixed.


## Credits
This project was created by following the Code Institute tutorials for the Boutique Ado Django Mini-Project, and customised to meet its unique requirements.

### Borrowed Code
Hint about removing up and down arrows from quantity input field in the shopping bag was taken [here](https://www.geeksforgeeks.org/how-to-disable-arrows-from-number-input/)

Tutorial on how to link to different section of the same page from [here](https://engineertodeveloper.com/a-better-way-to-route-back-to-a-section-ids-in-django/)

How to calculate some date in the [future](https://stackoverflow.com/questions/546321/how-do-i-calculate-the-date-six-months-from-the-current-date-using-the-datetime)

[Parallax effect](https://www.w3schools.com/howto/howto_css_parallax.asp)