// El año con más carreras realizadas

SELECT YEAR(Fecha) AS Año, count(IdCarrera) AS Total
FROM races
GROUP BY YEAR(Fecha)
ORDER BY Total DESC
LIMIT 1;


// El piloto que gano mas carreras

SELECT q.IdPiloto, COUNT(q.IdCarrera) AS Total, d.Nombre, d.Apellido
FROM qualifying q
JOIN drivers d
ON q.IdPiloto = d.IdPiloto
WHERE Posicion = 1
GROUP BY IdPiloto
ORDER BY Total DESC
LIMIT 1;


// Nombre del circuito con mas cantidad de carreras

SELECT c.IdCircuito, c.Nombre_Circuito, COUNT(r.IdCarrera) AS Total
FROM races r
JOIN circuits c
ON r.IdCircuito = c.IdCircuito
GROUP BY r.IdCircuito
ORDER BY Total DESC
LIMIT 1;


// Piloto con mayor cantidad de puntos y que sea American or British

SELECT r.IdPiloto,  d.Nombre, d.Apellido, SUM(r.Puntos) AS Total
FROM results r
JOIN drivers d
ON r.IdPiloto = d.IdPiloto
WHERE Nacionalidad IN ('British', 'American')
GROUP BY IdPiloto
ORDER BY Total DESC
LIMIT 1;





