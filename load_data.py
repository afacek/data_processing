import psycopg2 as psdb
from config import config

def connect():
	"""Connect to the Postgre database server"""
	conn = None
	try:
		# read connection parameters
		params = config()

		# connect to the database server
		conn = psdb.connect(**params)

		# create a cursor
		cur = conn.cursor()


		# SQL statements
		sql_querry = 'SELECT  report_count, COUNT(report_count) FROM rdt_facilities GROUP BY  report_count'

		# execute a statement
		cur.execute(sql_querry)
		print(cur.rowcount)

		# displaythe postgreSQL database server version
		report_status = cur.fetchall()
		print((report_status))

		# close the communication with postgreSQL
		cur.close()
	except (Exception, psdb.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print("Database connection closed: ")


connect()
