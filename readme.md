# Web Services Engineering - Assignment 2
## CRUD Operations with Flask and SQLite
## Created by John Foster

### What is this?
This project is a small web app that creates a SQL database and lets users interact with it through a HTML web page displaying it in a table.

### How to Run
The simplest way to run is the `run_app.bat` file used to start the Flask server. This will create a new database.db file if you don't have one or deleted it. It will also provide an IP address (for me its http://127.0.0.1:5000/) to access the client.html template file and interact with the database.
If you have an IDE, you can set up a python virtual environment with Flask downloaded, and run app.py to also launch the program. The URL that's generated should be the same.

### Original Assignment Instructions
For this assignment, you will practice building a simple web service, from client to server and back. "CRUD" stands for Create, Read, Update, and Delete - while not my favorite acronym, it's a common phrase to describe an application that can read information from a database, create new content, update existing information, and delete entries. We'll talk about security and other required features for a production level application later - for now, let's make sure we have a handle on the basics.

For this assignment, you will make a basic client (using your web design skills) and server-side web services to interact with a database. If you're already a pro with a particular framework, use a different one for this assignment (e.g. If you use React at work, try using Django or Laravel).

Specifically:

- When the client page loads, display information in an HTML table from at least one SQL table in the database
- At the top of the client table, have a row with text boxes and other inputs. There should also be a button that when pressed, sends the data from that row to the database and then refreshes the page to reload the information
You can also do this dynamically without a page refresh, but it's not required
- Allow the user to edit at least one column in the HTML table on the client, and automatically sent a request to the server to update the database table
- Have a button in the last column of each row that when pressed, deletes that row from the database table. The page should refresh as well.

Your client and web services may be focused on any topic that interests you, as long as it is meaningful (aka: Don't just have a table with only an ID field - it should have multiple columns and each row should sufficiently represent some kind of "object"). The client should also be styled nicely with CSS.

Submission

Code files for your web client and server-side web service
SQL database file
Essentially, SQL queries I can run to automatically recreate your database with some sample data filled in
Instructions on how to build and run your application
NOTE: Do NOT use SQL concatenation to pass parameters to your SQL queries. This is an incredibly bad habit that I have personally seen exploited to do terrible things to a company's database. Use stored procedures or other features of your SQL set-up instead. If you need help with this, let me know.