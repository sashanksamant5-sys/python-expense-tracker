import psycopg2

def get_connection():
    conn=psycopg2.connect(
       host="localhost",
       database="expenseDB",
       user="postgres",
       password="sekhar@2006"  
    )
    return conn

if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Connection successful!")
        conn.close()
    except Exception as e:
        print("Connection failed:", e)