import sys
import logging
import rds_config
import pymysql
#rds settings
rds_host  = "aurorademodb.cluster-czcivhqqc3vl.us-east-1.rds.amazonaws.com"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    print("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
def lambda_handler(event, context):
    user=event['user']
    team=event['team']
    feedback=event['feedback']
    rating=event['rating']  
    s="Insert into `AuroraDemoDB`  values ('{}','{}','{}','{}')".format(user,team,feedback,rating)

    with conn.cursor() as cur:
      cur.execute(s)
      conn.commit()
        
    conn.commit()

    return "Your Feedback has been updated"
    