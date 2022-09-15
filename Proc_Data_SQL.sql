ALTER TABLE circuits ADD PRIMARY KEY(IdCircuito);

ALTER TABLE constructors ADD PRIMARY KEY(IdConstructor);

ALTER TABLE drivers ADD PRIMARY KEY(IdPiloto);
ALTER TABLE drivers ADD INDEX(Nacimiento);

ALTER TABLE qualifying ADD PRIMARY KEY(IdCalificacion);
ALTER TABLE qualifying ADD INDEX(IdCarrera);
ALTER TABLE qualifying ADD INDEX(IdPiloto);
ALTER TABLE qualifying ADD INDEX(IdConstructor);

ALTER TABLE races ADD PRIMARY KEY(IdCarrera);
ALTER TABLE races ADD INDEX(IdCircuito);
ALTER TABLE races ADD INDEX(Fecha);

ALTER TABLE results ADD PRIMARY KEY(IdResultado);
ALTER TABLE results ADD INDEX(IdCarrera);
ALTER TABLE results ADD INDEX(IdPiloto);
ALTER TABLE results ADD INDEX(IdConstructor);
ALTER TABLE results ADD INDEX(IdEstado);

ALTER TABLE stops ADD PRIMARY KEY(IdParada);
ALTER TABLE stops ADD INDEX(IdCarrera);
ALTER TABLE stops ADD INDEX(IdPiloto);

ALTER TABLE laptimes ADD INDEX(IdCarrera);
ALTER TABLE laptimes ADD INDEX(IdPiloto);

ALTER TABLE results_notnull ADD PRIMARY KEY(IdResultado);
ALTER TABLE results_notnull ADD INDEX(IdCarrera);
ALTER TABLE results_notnull ADD INDEX(IdPiloto);
ALTER TABLE results_notnull ADD INDEX(IdConstructor);
ALTER TABLE results_notnull ADD INDEX(IdEstado);


ALTER TABLE qualifying ADD CONSTRAINT qua_fk_races FOREIGN KEY (IdCarrera) REFERENCES races (IdCarrera) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE qualifying ADD CONSTRAINT qua_fk_drivers FOREIGN KEY (IdPiloto) REFERENCES drivers (IdPiloto) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE qualifying ADD CONSTRAINT qua_fk_constructors FOREIGN KEY (IdConstructor) REFERENCES constructors (IdConstructor) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE races ADD CONSTRAINT races_fk_circuits FOREIGN KEY (IdCircuito) REFERENCES circuits (IdCircuito) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE results ADD CONSTRAINT results_fk_races FOREIGN KEY (IdCarrera) REFERENCES races (IdCarrera) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE results ADD CONSTRAINT results_fk_drivers FOREIGN KEY (IdPiloto) REFERENCES drivers (IdPiloto) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE results ADD CONSTRAINT results_fk_constructors FOREIGN KEY (IdConstructor) REFERENCES constructors (IdConstructor) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE stops ADD CONSTRAINT stops_fk_races FOREIGN KEY (IdCarrera) REFERENCES races (IdCarrera) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE stops ADD CONSTRAINT stops_fk_drivers FOREIGN KEY (IdPiloto) REFERENCES drivers (IdPiloto) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE results_notnull ADD CONSTRAINT resultsnn_fk_races FOREIGN KEY (IdCarrera) REFERENCES races (IdCarrera) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE results_notnull ADD CONSTRAINT resultsnn_fk_drivers FOREIGN KEY (IdPiloto) REFERENCES drivers (IdPiloto) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE results_notnull ADD CONSTRAINT resultsnn_fk_constructors FOREIGN KEY (IdConstructor) REFERENCES constructors (IdConstructor) ON DELETE RESTRICT ON UPDATE RESTRICT;