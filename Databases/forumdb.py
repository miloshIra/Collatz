# "Database code" for the DB Forum.

import datetime, psycopg2

POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  return reversed(POSTS)

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect("dbname='forumdb' user='postgres' password='post' host='localhost' port='5432'")
  c=db.cursor()
  c.execute("CREATE TABLE IF NOT EXISTS POSTS (id INTEGER PRIMARY KEY, Opis TEXT)")
  c.execute("INSERT into posts values (%s)" % (content,))
  db.commit()
  db.close()
