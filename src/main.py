from database import get_connection

def test_connection():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT NOW() AS now;")
    result = cur.fetchone()
    hora = result["now"]
    hora_formatada = hora.strftime("%d-%m-%Y %H:%M:%S")
    print("Conectado com sucesso!")
    print("Hora do servidor:", hora_formatada)
    cur.close()
    conn.close()

if __name__ == "__main__":
    test_connection()
