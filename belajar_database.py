import psycopg2

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
password = 'admin'
port_id ='5432'
connection = None
cur = None

""" membuat koneksi """
try:
    connection = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = password,
            port = port_id)
    print("Koneksi ke database berhasil")
    cur = connection.cursor()    
except Exception as error:
    print(f"Koneksi ke database gagal: {error}")
finally:
    if cur is not None:
        cur.close()
    if connection is not None:
        connection.close()
print("Koneksi ke database ditutup.")

