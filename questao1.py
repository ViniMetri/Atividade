from config_bd import connection

user= input("Digite algo para listar os jogos: ")
user = f"%{user}%"

conn = connection()
try:
    cursor = conn.cursor()
    query = 'SELECT titulo, subtitulo FROM jogos WHERE titulo ILIKE %s OR subtitulo ILIKE %s'
    cursor.execute(query, (user, user))
    resultado = cursor.fetchall()
    for i in range(len(resultado)):
        print(resultado[i])

except Exception as e:
    print(f"ERROR: {e}")

finally:
    cursor.close()
    conn.close()