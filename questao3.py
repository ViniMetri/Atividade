from config_bd import connection

conn = connection()
filtro = '%k%'

try:
    cursor = conn.cursor()
    query = 'SELECT titulo, subtitulo FROM jogos WHERE titulo ILIKE %s OR subtitulo ILIKE %s'
    cursor.execute(query, (filtro, filtro))
    resultado = cursor.fetchall()
    for i in range(len(resultado)):
        print(resultado[i])

except Exception as e:
    print(f"ERROR: {e}")

finally:
    cursor.close()
    conn.close()