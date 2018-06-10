# LOG ANALYSIS PROJECT

> Harsimar Singh

-----------------------------------------------------------

* The live streaming of [project](https://harsimarsingh8.github.io/Log_Analysis/result_output.txt).
* Project can be viewed at my [Github Repository](https://github.com/harsimarsingh8/Log_Analysis).

------------------------------------------------------------
### About

This is the project of Udacity NanoDegree. This project includes large database professes to be designed for newspaper  site that includes 3 tables viz. **articles**, **authors** and **log** with millions of rows by SQL queries. This database contains the data of articles read, authors of the articles and web server log for the newspaper site.This data is used for conclusion for different results.

### Prerequisites

* Python
* Vagrant
* VirtualBox

### Installing

1.Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
2.Download or clone from github [fullstack-nandegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm)
3.Now we got newsdata.sql in our vagrant directory and now we are good to go.


### Downloading

* Download the [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) file.


### Running the tests

* Launch Vagrant VM by running `vagrant up`, you can the log in with `vagrant ssh`
* Load the data into databse named *news*, use the command `psql -d news -f newsdata.sql` only once.<br>
    -use **\c** to connect to database="news"<br>
    -use **\dt** to see the tables in database<br>
    -use **\dv** to see the views in database<br>
    -use **\q** to quit the database<br>
* Connect to databse, run the command `psql -d news`.
* Create a *view* , use the command psql -d news and then run the SQL statement as mentioned below.

    * SQL query for creating view: CREATE VIEW v8:
```
create view v8 as select date(time) as Date,
round(sum(case when status not like '%200%' AND status like '%404%' then 1 else 0 end)*100.0/count(status),2) as Errorr from log group by Date;
```

* To execute the program, run `python Log_Analysis.py` from the command line.
