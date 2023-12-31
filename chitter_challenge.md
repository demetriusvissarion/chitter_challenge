# Chitter Challenge

We are going to write a small Twitter clone that will allow the users to post
messages to a public stream.

## User Stories

```
STRAIGHT UP

As a Maker
So that I can let people know what I am doing
I want to post a message (peep) to chitter
 => each peep display will have: content, by user (handle)

As a maker
So that I can see what others are saying
I want to see all peeps in reverse chronological order

As a Maker
So that I can better appreciate the context of a peep
I want to see the time at which it was made
 => display time for each peep (TDD)

As a Maker
So that I can post messages on Chitter as me
I want to sign up for Chitter
 => check that username and email are unique.

HARDER

As a Maker
So that only I can post messages on Chitter as me
I want to log in to Chitter

As a Maker
So that I can avoid others posting messages on Chitter as me
I want to log out of Chitter

ADVANCED

As a Maker
So that I can stay constantly tapped in to the shouty box of Chitter
I want to receive an email if I am tagged in a Peep
 => build Tags 
 => build Notifications class and setup API to send emails
```

## Additional Notes

* You don't have to be logged in to see the peeps.
* Users sign up to chitter with their email, password, name and a username (e.g.
  samm@makersacademy.com, password123, Sam Morgan, sjmog).
* The username and email are unique.
* Peeps (posts to chitter) have the name of the user and their user handle.
* Your README should indicate the technologies used, and give instructions on
  how to install and run the tests.

## Technical Approach

In the last two weeks, you integrated a database using the `psycopg` package and
Repository classes. You also implemented small web applications using Flask,
Pytest, HTML and Jinja templates to make dynamic webpages. You can continue to
use this approach when building the Chitter Challenge.

If you'd like a more technical challenge now, try using an Object Relational
Mapper as the database interface, instead of implementing your own Repository
classes. You can research Python ORMs to decide which to use, but
[Peewee](https://github.com/coleifer/peewee) is a popular choice.


Action plan:
- change login to store full name as well (big change!!!) => DB => MCV
    => 
- create seeding system and seed hard coded data before tests
- add to each peep display: content, by full_name + (@username), time posted
- build Notifications class and setup API to send emails, and record action on db
- add logged in user name next to log out, maybe on the same button
- db: connection, create, read, update, delete (CRUD)
- visitor: view of homepage, read-only access
- user signup: uniques(username and email), db ✅
- user login and logout: session ✅
- peep: CRUD, display(x3)
- email notification: email sent, db recorded
- write README.md with complete project setup

TDD:
- db: connection, create, read, update, delete (CRUD)
- visitor: view of homepage, read-only access
- user signup: uniques(username and email), db 
- user login and logout: session 
- peep: CRUD, display(x3)
- email notification: email sent, db recorded
- write README.md with complete project setup
