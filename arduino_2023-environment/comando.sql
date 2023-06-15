CREATE TABLE persona (
	id serial PRIMARY KEY,
	name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL,
	email VARCHAR (150)
);

CREATE TABLE departamento (
	id serial PRIMARY KEY,
	name VARCHAR (50) NOT NULL,
	fk_persona integer,
	CONSTRAINT depto_frkey FOREIGN KEY (fk_persona) 
	REFERENCES persona (id)
);

CREATE TABLE sueldo (
	id serial PRIMARY KEY,
	monto integer,
	depto_fk integer,
	CONSTRAINT sueldo_frkey FOREIGN KEY (dpto_fk) 
	REFERENCES departamento (id)
);

alter table persona add column depto_fk int;
alter table persona add CONSTRAINT persona_frkey FOREIGN key (depto_fk) refences departamento (id)
update persona set depto_fk = valor where id = valor;
alter table persona alter column depto_fk set not null;

INSERT INTO persona (name, last_name) VALUES ('Juan', 'Saldivia');
INSERT INTO departamento (name, fk_persona) values ('compras', 1);
INSERT INTO sueldo (monto, depto_fk) VALUES (30000, 3);

SELECT * FROM persona;

SELECT * FROM persona WHERE id = 2;

DELETE FROM persona WHERE id = 2;

UPDATE persona SET email = 'algo@algo.com' WHERE id = 3;

select * from departamento d join persona p on (d.fk_persona = p.id) where p.id =1;
select * from sueldo s join departamento d on (s.depto_fk = d.id) where d.id =2;



mutation{
  createPersona(name: "Tito", lastName: "Ledesma", email: "asds@asd.asd"){
    persona{
      id
      name
      lastName
      email 
    }
  }
}