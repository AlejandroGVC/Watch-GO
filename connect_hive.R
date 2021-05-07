# Copyright 2018 Cloudera, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# first install the Hive JDBC driver
# from https://www.cloudera.com/downloads/connectors/hive/jdbc.html

# set jdbc_path to the path to the folder containing the JAR files
# extracted from the JDBC41 zip file in the JDBC driver package
jdbc_path <- "PATH TO FOLDER CONTAINING JAR FILES HERE"

# set the Hive JDBC connection string
jdbc_conn_str <- "jdbc:hive2://HOSTNAME:10000"

# install the RJDBC package if it's not already installed
if(!"RJDBC" %in% rownames(installed.packages())) {
  install.packages("RJDBC")
}

# initialize rJava
hive_classpath <- list.files(path = jdbc_path, pattern = "\\.jar$", full.names = TRUE)
rJava::.jinit(classpath = hive_classpath)

# connect to HiveServer2
library(DBI)
drv <- RJDBC::JDBC("com.cloudera.hive.jdbc41.Driver", hive_classpath, "`")
hive <- dbConnect(drv, jdbc_conn_str)

# now you can run SELECT queries and return the results to R
# using the dbGetQuery() function

# for example:
dbGetQuery(
  hive,
  "SELECT origin,
    COUNT(*) AS num_departures,
    AVG(dep_delay) AS avg_dep_delay
  FROM flights
  WHERE dest = 'LAS'
  GROUP BY origin
  ORDER BY avg_dep_delay")

# disconnect from Hive
dbDisconnect(hive)