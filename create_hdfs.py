import subprocess

cmd = 'start-hdfs.sh'
subprocess.call(cmd, shell = True)

cmd = 'hdfs dfsadmin -safemode leave'
subprocess.call(cmd, shell = True)

cmd = 'hdfs dfs -mkdir - p /datalake/platforms'
subprocess.call(cmd, shell = True)

cmd = 'hdfs dfs -put prime_video.csv /datalake/platforms/'
subprocess.call(cmd, shell = True)

cmd = 'hdfs dfs -mkdir - p /datalake/cartelera'
subprocess.call(cmd, shell = True)

cmd = 'hdfs dfs -put cartelera.csv /datalake/cartelera/'
subprocess.call(cmd, shell = True)

