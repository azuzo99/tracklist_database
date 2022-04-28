# tracklist_database
This repo contains project of my first created database using sqlite3. This database uses two files unique_tracks.txt and triplets_sample_20p.txt, but in case of memory exceed it was not possible to upload all the files.
## #1  Engine and connection between SQL database and table
This chapter was done by using simple sqlite3.connect. The database named Tracks.db was created, then I used simple SQL syntax CREATE TABLE with existing names and types of variables.
## #2 Preparing and oading data
The second chapter refers to the data loading to database. With method enable to operate on existing txt file ( in both cases method was the same ), then at first extracting variables separated by <SEP> was done by simple split method. Strip /n was done for skip new line syntax from txt. In last part SQL command INSERT helped to load data. Datetime was used to measure a time of loading data -> for unique_tracks.txt it was approximately 6 sec -> for triplets_sample_20p.txt it was approximately 2 mins and 30 sec
## #3 Top 5 played tracks
The scope of this part was to create a Query that will give us information about top5 played artists. The relation of two tables was found by SQL code
## #4 Top artist
Finding a top played artist was done by similar way, by find relation between two tables using Query. Then pandas helped me to groupby and find the top played artist
## #5 Execution
## #6 Close connection
