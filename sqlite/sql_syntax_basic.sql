----Создать таблицы
CREATE TABLE students (

	name TEXT,
	surname TEXT,
	age INTEGER

);

CREATE TABLE employees (

	name TEXT,
	surname TEXT,
	age INTEGER

);

--=======================================================================
--CRUD - Создать, считать, редактировать и удалить.
--=======================================================================

--=======================================================================
--Поместить данные в таблицы (Создать)
--=======================================================================

INSERT INTO employees (name, surname, age) VALUES ('Arkady', 'Counter', 25);
INSERT INTO employees (name, surname, age) VALUES ('Daniil', 'Krost', 20);
INSERT INTO employees (name, surname, age) VALUES ('Jack', 'Black', 25);
INSERT INTO employees (name, surname, age) VALUES ('Jane', 'White', 20);
INSERT INTO employees (name, surname, age) VALUES ('Arkady', 'Counter', 25);
INSERT INTO employees (name, surname, age) VALUES ('Daniil', 'Krost', 20);
INSERT INTO employees (name, surname, age) VALUES ('Jack', 'Black', 25);
INSERT INTO employees (name, surname, age) VALUES ('Jane', 'White', 20);

--=======================================================================
--.read - считать инфу из файла
--=======================================================================

----Сделать запрос всех данных
SELECT * FROM employees;
-- * - все столбцы

SELECT name FROM employees;
SELECT name, age FROM employees;

--Выбрать записи с условиями = или is
SELECT name, age FROM employees WHERE name = 'Arkady';
SELECT name, age FROM employees WHERE name is 'Arkady';

--Условие нет
SELECT name, age FROM employees WHERE name is not 'Daniil';

--Условие и
SELECT name, age FROM employees WHERE name is not 'Daniil' and age is not 20;
SELECT name, age FROM employees WHERE age < 18;

--% - любое количество любых символов
--Условие в начале
SELECT name, age FROM employees WHERE name LIKE 'Ar%';

--Условие в конце
--Условие или
SELECT * FROM employees WHERE name LIKE '%t' or surname LIKE '%t';

--Условие посередине
SELECT * FROM employees WHERE name LIKE '%i%';

--=======================================================================
--редактировать
--=======================================================================

--ОБЫНОЙ ПО ID
--Но можно и по-другому
--Изменить по условию
UPDATE employees SET name='Danil' WHERE name='Daniil';

--Изменить все
UPDATE employees SET age=20;
UPDATE employees SET name='Daniil', age=19 WHERE name='Danil';
UPDATE employees SET age=18 WHERE name='Jane' or surname='Black';

--=======================================================================
--Удалить
--=======================================================================
-- Удалить по условию
DELETE FROM employees WHERE name='Jane' or surname='Black';
DELETE FROM employees WHERE age=19 AND surname='Krost';

-- Удалить всё, кроме названий столбцов и таблицы
DELETE FROM employees;

--Удалить таблицу
DROP TABLE employees;
