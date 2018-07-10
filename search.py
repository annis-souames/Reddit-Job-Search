import datetime

import praw


def connect(cl_id, cl_secret):
    return praw.Reddit(client_id = cl_id, client_secret = cl_secret, user_agent = "Job Finder by Hugeburger")

def search_reddit(query):
    red = connect(client,secret)
    # Generating the string for keywords
    keys = query.split(",")
    subs = ["jobbit","forhire"]

    # Generate string for keys
    str_keys = "(title : \"" +keys[0]+ "\""
    for k in keys[1:]:
        str_keys = str_keys + " OR title:\"" + k + "\""
    str_keys = str_keys + ")"

    #Generate string for subs
    str_subs = "(subreddit:hiring"
    for sub in subs:
        str_subs = str_subs + " OR subreddit:" + sub
    str_subs = str_subs + ") "

    full_str = "(title:\"hiring\" OR flair:Hiring) AND  " + str_keys + " AND " + str_subs

    #making the call
    all = red.subreddit("all")
    """
    for post in all.search(query = full_str, sort = "new"):
        print post.title
        post_date = datetime.datetime.utcfromtimestamp(post.created_utc)
        print str(post_date.month) + ", " + str(post_date.day) + " in " + str(post_date.year)
    """
    return all.search(query = full_str, sort = "new")








