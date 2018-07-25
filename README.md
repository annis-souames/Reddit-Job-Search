# Reddit-Job-Search
Junter is a simple to use, free and open source web application to find job opportunities on Reddit.

I built this when I was looking for a job as a python developer, Reddit is a great place to find jobs, but there are a lot of subreddits to check for
and it's hard to search all these subs, and filter jobs by keywords. 

Junter uses Reddit API through PRAW and Flask on the backend, standard Jinja 2 is used for rendering (moving to VueJS/React/Angular) would make it faster

So I decided to build Junter to make this easier for everyone, enjoy :D 

## Screenshots:
![Homepage](https://i.imgur.com/1Q567qQ.png)
![Results page](https://i.imgur.com/p9UYjao.png)


## Setting Up:

First, create a Reddit app and get the client ID and secret key, clone this project (or fork to add other features).

Install the requirements : `pip install -r requirements.txt` , main dependencies are Flask and PRAW .

## Authentication:

Grab the client ID and secret key, and put it in the search.py file, you will find two strings : client and secret (should be on the 20th and 21st line), paste your keys there

## Launching:

You should be ready, just fire up the terminal and run `python server.py` and the web app should work .

## Some Suggestion:

- Add craiglist scraping

- Search jobs on Twitter

- Search jobs on facebook groups

- Make it automated and store jobs in a database to make search faster, scraper should run every hour to get up-to date results



