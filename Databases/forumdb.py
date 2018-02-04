# "Database code" for the DB Forum.

import datetime, psycopbg2

POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  return reversed(POSTS)

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopbg2.connect(database='forum.db')
  c=db.cursor
  c.execute("INSERT into posts values ('%s')" % content)
  db.commit()
  db.close()
