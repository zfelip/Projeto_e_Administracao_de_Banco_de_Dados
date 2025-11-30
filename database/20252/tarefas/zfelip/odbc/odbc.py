import pyodbc

conn = pyodbc.connect(
    "DRIVER={PostgreSQL Unicode};"
    "SERVER=localhost;"
    "PORT=5432;"
    "DATABASE=atividade_db;"
    "UID=postgres;"
    "PWD=12345;"
)
cursor = conn.cursor()

print("Conectado realizada")

cursor.execute("""
    INSERT INTO atividade (descricao, projeto, data_inicio, data_fim)
    VALUES ('Atividade via ODBC', 1, '2024-01-01', '2024-02-01');
""")
conn.commit()

cursor.execute("""
    UPDATE projeto SET responsavel = 3 WHERE codigo = 1;
""")
conn.commit()

cursor.execute("""
    SELECT p.nome, a.descricao
    FROM projeto p
    LEFT JOIN atividade a ON a.projeto = p.codigo
    ORDER BY p.codigo;
""")

rows = cursor.fetchall()
for r in rows:
    print(r)

cursor.close()
conn.close()
