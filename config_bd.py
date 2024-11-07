import psycopg2

def connection():
    try:
        conn = psycopg2.connect(
            dbname='Atividade',
            user='postgres',
            password='post',
            host='localhost',
            port='5432'
        )

        return conn
    
    except Exception as e:
        print(f'ERROR: {e}')
        return None
    