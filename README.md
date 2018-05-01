# Social Messaging Application
# LiSSMessageApp

# Objectives
1. Understand the design, implementation and use of an application backed by a database system.
2. Understand the use of the E-R model for database application design.
3. Gain experience by implementing applications using layers of increasing complexity and fairly complex data structures.
4. Gain further experience with Web programming concepts including REST and HTTP.

# General Overview
Simple UI and the backend of an application used for messaging in a social context. The application allows these operations, backed by a database engine:
   1. Register a user with the application
   2. Create a chat group with a given name
   3. Add a user to your contacts list based on name, last name, and either 1) phone or 2) email address
   4. Add a contact to a chat group
   5. Remove a user from a chat group
   6. Remove a user from the contacts list
   7. Remove a chat group (only the owner)
   8. Post a message to a chat group
   9. Read the messages from a chat group
   10. Like a message posted on a chat group
   11. Dislike a message posted on a chat group
   12. Reply to a message posted on a chat group

Optionally, the application can support the following for extra credit:
   1. Post an image to a group
   2. Post a video to a group
   
In addition, develop a web-based dashboard that will provide statistics suchas as:
   1. Trending topics via #hashtags
   2. Number of message per day
   3. Number of replies per day
   4. Number of likes
   5. Number of dislikes
   6. Active users
   
The data in the application is managed by a relational database system, and exposed to client
applications through a REST API. 
