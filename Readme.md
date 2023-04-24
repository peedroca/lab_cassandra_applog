# Creating a database with Apache Cassandra

[Cassandra docs](https://cassandra.apache.org/doc/latest/)

## Configurations on Docker Desktop

#### Step 1 - Create our container with Cassandra.
After donwload and configuration of docker desktop in your machine, run the next commands:

```bash
# Download docker image Cassandra
docker pull cassandra

# Create a new container with image Cassandra
docker run --name applog-cassandra -p 9042:9042 -d cassandra
```

#### Step 2 - Create table structure
When you are inside container and accessing CassandraDB, run the following commands to create your KeyStore (similar to create database on relational databases) and configure ours tables. We'll use applications/bootstrap.py to configure that for us.

#### Step 3 - Run apps to populate logs
There are some applications on /Applications folder, to populate automatic log table, so you can run an data analyze software to get the date as PowerBI.