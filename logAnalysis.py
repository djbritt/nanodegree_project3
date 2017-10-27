import datetime
import psycopg2

DBNAME = "news"


def dbCall(query):
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    posts = c.fetchall()
    db.close()
    return posts

print "What are the most popular three articles of all time?"
q1 = dbCall("select title, count(slug) as views from articles join log on \
            replace(log.path, '/article/', '') = articles.slug group by title \
            order by count(slug) desc limit 3;")

for i in range(0, 3):
    print str(q1[i][0]) + " -- " + str(q1[i][1]) + " views"

print "------------------------"

print "Who are the most popular article authors of all time?"
q2 = dbCall("select name, count(slug) as views from articles join authors on \
            articles.author=authors.id join log on replace \
            (log.path, '/article/', '')=articles.slug group by name order \
            by views desc")

for i in range(0, len(q2)):
    print str(q2[i][0]) + " -- " + str(q2[i][1]) + " views"

print "------------------------"

print "On which days did more than 1% of requests lead to errors?"
q3 = dbCall("select date(time) as dayParsed, dayError.dError::float/count(*)\
            as percent from log join dayError on date(time) = dayError.day\
            group by dayParsed, dayError.dError order by percent desc\
            limit 1;")

print str(q3[0][0]) + " -- " + "{0:.0f}".format(q3[0][1] * 100) + "% errors"
