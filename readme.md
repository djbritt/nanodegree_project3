# Project e - PostgreSQL Log Analysis - Full Stack Nanodegree :file_folder:
## By Daniel Britt

# Purpose
This is a program that pulls information and creates log reports from a database filled with records of where useers have gone, authors, and their articles.

# Views
I only used one view, and it is called dayError
```python
create view dayError as select date(time) as day, count(*) as dError from log where status not like '200%' group by date(time);
```

# Running
To run this code, you need a certain vagrant virtual system that the udacity nanodegree offers. But once you have that, and have imported the news.sql file, you can simply run
```python
python logAnalysis.py
```

# Technologies
This project uses Python, and PostgreSQL.
