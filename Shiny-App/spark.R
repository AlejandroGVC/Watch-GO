library(sparklyr)
# Sesion y contexto
sc <- spark_connect(master = 'local')

spark_read_csv(sc, 'hdfs://namenode:8020/family.csv')
