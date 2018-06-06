#! /usr/bin/env python2

import os
import sys
import psycopg2
DB_NAME = "news"

# 1.  The most popular three articles of all time?
query1 = ("SELECT articles.title, count(*) AS counting_view FROM log"
          ",articles WHERE log.status = '200 OK' AND substr(log.path,10,100)"
          "= articles.slug GROUP BY articles.title,log.path ORDER BY (counting_view)"  # noqa
          "DESC limit 3;")
# 2.  The most popular author of all time?
query2 = ("SELECT authors.name, count(*) AS counting_view1 FROM log"
          ",authors,articles WHERE substr(log.path,10,100) = articles.slug AND "       # noqa
          "authors.id = articles.author AND log.status = '200 OK'"
          "GROUP BY authors.name ORDER BY (counting_view1) DESC limit 3;")
# 3. Days that lead to more than 1% of requests lead to errors?
query3 = ("SELECT * FROM v8 WHERE Errorr > 1 ORDER BY Errorr DESC;")


def getresult(query):
    db = psycopg2.connect(database=DB_NAME)
    cur = db.cursor()
    cur.execute(query)
    output = cur.fetchall()
    db.close()
    return output


# get query result
q1_result = getresult(query1)
q2_result = getresult(query2)
q3_result = getresult(query3)


def printresult(query):
    n = len(query)
    for i in range(0, n):
        title = query[i][0]
        views = query[i][1]
        print ("\t %s || %d" % (title, views) + " views")
    print("\n")


def printsresult(query):
    n = len(query)
    for i in range(0, n):
        title = query[i][0]
        error = query[i][1]
        print ("\t %s || %.2f" % (title, error) + "% error")
    print("\n")

# displaying query's output

if __name__ == "__main__":
    print("What are the most popular three articles of all time?")
    printresult(q1_result)
    print("Who are the most popular article authors of all time?")
    printresult(q2_result)
    print("On which days did more than 1% of requests lead to errors?")
    printsresult(q3_result)
