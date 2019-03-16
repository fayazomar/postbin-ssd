# Postbin-ssd

Postbin is a web application based on Django web framework meant to implement similar functionality as the well known site pastebin.com

## Installation

Clone the project to your preferred environment and navigate to the directory /postbin-ssd/django-project/

Then run the following command on your terminal to run the application:

```bash
python3 manage.py runserver
```

## Project Layout/Organization & Usage

This application has three tiers of users, Administrators, Users and Visitors (unauthenticated visitors to the site).

The following screenshots will guide you on how to use the application and understand its layout

###Visitors & users

The Homepage:
Visitors can view public posts that are available on the website (First page showing 10 recent posts) and download them as raw text files if needed using the Download button.
![Homepage](/django_project/media/001.png)

Upon clicking the Register button, visitors can join the website by creating an account. The following form needs to be filled in order to do that.
![Register](/django_project/media/002.png)

After successfully creating an account, the visitor can login using the credentials chosen.
![Login](/django_project/media/003.png)

Once logged in, the user is directed back to the Homepage with access to create new posts.
![Homepage](/django_project/media/001.png)

For creating a new post, users can click on the button to create a new post which will direct them to the following page.
This page allows the user to enter a Post title, Content, Expiration Date, The option to invite other users and setting the post access to Private otherwise the default is Public.
![CreatePost](/django_project/media/004.png)

Each post created by a user has the options to Update, Delete and Download.
![UpdateDeletePost](/django_project/media/005.png)

Additionally, users have access to their profiles by clicking on the profile button on the navigation bar. This page allows them to update their profile picture and details.
![UserProfie](/django_project/media/006.png)

Finally, users can Logout by clicking on the logout button.
![UserLogout](/django_project/media/007.png)

Incase a user forgets their login password, the functionality to reset the password is available on the login page.
![Login](/django_project/media/003.png)

By clicking on Forgot password link, the page redirects to a Reset form.
![UserReset](/django_project/media/008.png)

###Administrator

Run the following command on your terminal to create an admin user

```bash
python3 manage.py createsuperuser
```

You will be guided to create a username and password for the Administrator account.

To access the special Administrator portal visit the website/admin url.
![Admin](/django_project/media/009.png)

After logging in with the Administrator credentials, you will then be redirected to the following Administrator Dashboard which is not visible to Users and Visitors
![AdminDashboard](/django_project/media/010.png)

Dashboard Functionality:
Administrators can list, search, create, edit, update, delete Users by clicking the link Users under authentication and auhtorization.
List & Search:
![AdminDashboardUsersL](/django_project/media/012.png)

Create & Edit:
![AdminDashboardUsersE](/django_project/media/013.png)

Administrators can list, search, enable and disable Posts by clicking the link Posts under Postbin.
![AdminDashboardPosts](/django_project/media/014.png)

Finally, Administrator can Logout by clicking on the logout button.
![AdminLogout](/django_project/media/011.png)

All users can make use of the search bar to find specific public posts on the website.
![Search](/django_project/media/015.png)
