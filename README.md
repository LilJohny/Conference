#Conference

This is a Django app. To work appropriate some user groups should be created. To create these groups you should run.<br>
`python3 manage.py create_groups`
and<br>
`python3 migrate`


Presentation can be modified only by their presenters.<br>
A listener can sign up for an event only if it will happen in future and he is not already signed up.<br>
# This app contains pages:
* Profile page
This page contains information about the user: birthdate, username, events, he will visit, events, he will present, his first name and last name if specified.
* Edit profile page
This page gives ability to edit profile information.
* All events page
This page contains all created events, sorted by rooms.
* Recent events
This page contains ten events, that have not happened yet and will happen recent, sorted by time.
* My events
This page contains events, that was created by this user.
* Details about one event
This page give ability to view information about event. Only presenters can edit event.
* Edit event
This page gives ability to edit event. If you will select time and room, that is used, you will be prompted to change time or room.
* Create event
This page gives ability to create event. If you will select time and room, that is used, you will be prompted to change time ot room
* Registration page
This page gives the user the ability to register a profile.
* Login page
This page gives the user the ability to log in to the site.



To get schedule for some room with REST, you need to use link as this "schedules/room_number/". Also you need to do basic authentication <br>
with username and password.
