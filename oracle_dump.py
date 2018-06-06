import cx_Oracle

# Enter connection info here
connstr = None
conn = cx_Oracle.connect(connstr)

cur = conn.cursor()
# cur.execute('SELECT owner,table_name FROM all_tables')
# cur.execute('SELECT table_name FROM user_tables')
# cur.execute("SELECT count (SOURCE_APP_FUNCTION), count( DISTINCT SOURCE_APP_FUNCTION), SOURCE_APP  FROM EDMI.PIWIK_METRICS WHERE ( YEAR>=2017 AND MONTH=3 AND URI NOT LIKE '%test%' AND URI NOT LIKE '%prod%') GROUP BY SOURCE_APP")
# cur.execute("SELECT DISTINCT SOURCE_APP_FUNCTION  FROM EDMI.PIWIK_METRICS WHERE ( YEAR>=2017 AND MONTH=3 AND URI NOT LIKE '%test%' AND URI NOT LIKE '%prod%' AND SOURCE_APP='RATS') ")
# cur.execute("SELECT"
#             " count( DISTINCT USERNAME),SOURCE_APP  FROM EDMI.PIWIK_METRICS WHERE "
#             "( YEAR>=2017 AND MONTH=3 AND URI NOT LIKE '%test%' AND URI NOT LIKE '%prod%' ) GROUP BY SOURCE_APP")
cur.execute("SELECT count(*) FROM EDMI.PIWIK_METRICS ")
# cur.execute("SELECT count(*) FROM EDMI.PIWIK_METRICS WHERE ( YEAR>=2017 AND URI LIKE '%prod%')")
# cur.execute("SELECT COLUMN_NAME from USER_TAB_COLUMNS where TABLE_NAME='EDMI.PIWIK_METRICS'")
# cur.execute('SELECT * FROM PIWIK_METRICSV2')
res = cur.fetchall()
# res = cur.fetchmany(numRows=4)
print res
cur.close()
conn.close()
