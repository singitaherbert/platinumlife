CREATE DATABASE cars;
USE cars;

CREATE TABLE Table1(
	make varchar(50),
	Model varchar(50),
	manufacture_date date,
	model_id int primary key
);


CREATE TABLE Table2(
	manufacture varchar(50),
	model_id int FOREIGN KEY REFERENCES Table1(model_id),
	parts varchar(50),
	Warranty_Expiry_date date,
	city varchar(50)
);

INSERT INTO Table1
VALUES('BMW','M3','2023-10-03',1),
	('AUDI','RS4','2022-10-03',2),
	('TOYOTA','YARIS','2023-10-03',3)
;

INSERT INTO Table2
VALUES('BMW Autos',1,'Steering','2023-10-03','Pretoria'),
	('AUDI parts and spare',2,'Exhaust','2023-11-03','Sandton'),
	('AUDI parts and spare',2,'Exhaust','2022-10-04','Tokyo'),
	('TOYOTA  Mccarthy',3,'winsScreen','2022-10-30','Pretoria')
;
 --5.1
 CREATE TABLE #temporary_table(
		make varchar(50),
		Model varchar(50),
		manufacture_date date,
		parts varchar(50),
		Warranty_Expiry_date date)
		insert into #temporary_table
		select make,Model,manufacture_date,parts,Warranty_Expiry_date
		from table1
		join table2 on
		Table1.model_id = Table2.model_id;
select * from #temporary_table;

--5.2
--you need not to duplicate the objects in the database
--which we need change the name of the object or create another one 
--of different name or delete the old one before creating a a new one