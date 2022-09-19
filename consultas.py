import pymysql

def Pregunta1():
    conexion = pymysql.connect (host='localhost', database='api', user ='root', password='123')
    cursor = conexion.cursor()
    cursor.execute(
        '''SELECT YEAR(Fecha) AS Año, count(IdCarrera) AS Total
        FROM races
        GROUP BY YEAR(Fecha)
        ORDER BY Total DESC
        LIMIT 1;''')
    for dato in cursor:
        pass
    conexion.close()
    return("El año con mas carreras es el:"+' '+str(dato[0]))

def Pregunta2():
    conexion = pymysql.connect (host='localhost', database='api', user ='root', password='123')
    cursor = conexion.cursor()
    cursor.execute(
        '''SELECT q.IdPiloto, COUNT(q.IdCarrera) AS Total, d.Nombre, d.Apellido
        FROM qualifying q
        JOIN drivers d
        ON q.IdPiloto = d.IdPiloto
        WHERE Posicion = 1
        GROUP BY IdPiloto
        ORDER BY Total DESC
        LIMIT 1;''')
    for dato in cursor:
        pass
    conexion.close()
    return("El Piloto con más primeros puestos:"+' '+dato[2]+' '+dato[3])

def Pregunta3():
    conexion = pymysql.connect (host='localhost', database='api', user ='root', password='123')
    cursor = conexion.cursor()
    cursor.execute(
        '''SELECT c.IdCircuito, c.Nombre_Circuito, COUNT(r.IdCarrera) AS Total
        FROM races r
        JOIN circuits c
        ON r.IdCircuito = c.IdCircuito
        GROUP BY r.IdCircuito
        ORDER BY Total DESC
        LIMIT 1;''')
    for dato in cursor:
        pass
    conexion.close()
    return("El circuito más carreras es:"+' '+dato[1])

def Pregunta4():
    conexion = pymysql.connect (host='localhost', database='api', user ='root', password='123')
    cursor = conexion.cursor()
    cursor.execute(
        '''SELECT r.IdPiloto,  d.Nombre, d.Apellido, SUM(r.Puntos) AS Total
        FROM results r
        JOIN drivers d
        ON r.IdPiloto = d.IdPiloto
        WHERE Nacionalidad IN ('British', 'American')
        GROUP BY IdPiloto
        ORDER BY Total DESC
        LIMIT 1;''')
    for dato in cursor:
        pass
    conexion.close()
    return("El Piloto con más primeros puestos (Americano o Británico) es:"+' '+str(dato[1])+' '+str(dato[2]))

def query(query_):
    conexion = pymysql.connect (host='localhost', database='api', user ='root', password='123')
    cursor = conexion.cursor()
    cursor.execute(query_)
    for dato in cursor:
        salida = dato
    return (salida)