Functional requirements

Essentials:

Keep track of whose turn it is.
Register the list of participants.
The participant's list should be treated as a circular queue
End turn and display who is the next participant.

Desirable:

Display the queue in the current status
Clear the participants' list
Keep a history of the participants lists
Allow list shuffling

Non functional requirenments

Create an app in python + flask to listen for requests. 
Create POST method on `/circular` to allow participant's list creation with their names.
After the player takes his/her turn, he/she should be sent to the end of the queue. The next player to be shown is the next on the list.
Create GET method on `/circular/next` to end turn and display the name of the next player.
Create GET method on `/circular` to display the current status of the circular list.
Create DELETE method on `circular` to delete the current players list.


Expected endpoints:

POST /circular          <---> players names from json

GET  /circular/next     <---> next player on the players list

GET  /circular          <---> players list's current state 

DELETE  /circular     <---> delete the players list






