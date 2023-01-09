
-- Дамп структуры для таблица Countries
CREATE TABLE IF NOT EXISTS Countries (
  id serial primary key,
  name varchar(50) default null,
  population integer default null,
  gdp integer default null
 );

-- Дамп данных таблицы Countries
INSERT INTO Countries (id, name, population, gdp) values
  (1, 'Россия', 3000000, 500000000),
  (2, 'Узбекистан', 1000001, 200000000),
  (3, 'Китай', 100000000, 1000000000);


-- Дамп структуры для таблица Cities
CREATE TABLE IF NOT EXISTS Cities (
  id serial PRIMARY KEY,
  name varchar(50) not null,
  population integer default null,
  founded integer default null,
  country_id integer default null references Countries(id) -- 1:M. В одной стране много городов
);

-- Дамп данных таблицы Cities:
INSERT INTO Cities (id, name, population, founded, country_id) values
  (1, 'Ульяновск', 750000, 1648, 1),
  (2, 'Москва', 3000000, 1420, 1),
  (3, 'Ташкент', 2500000, 956, 2),
  (4, 'Урумчи', 900000, 205, 3),
  (5, 'Шанхай', 3000000, 20, 3);
  
-- Дамп структуры для таблицы Companies
CREATE TABLE IF NOT EXISTS Companies (
  id serial PRIMARY KEY,
  name varchar(50) not null, 
  city_id integer not null references Cities(id), -- 1:M. В одном городе может быть много штаб-квартир,
  revenue integer not null,
  labors integer not null
);

-- Дамп данных таблицы Companies: ~8 rows (приблизительно)
INSERT INTO Companies (id, name, city_id, revenue, labors) VALUES
  (1, 'Супер-софт', 1, 900000000, 900),
  (2, 'Мегасофт', 1, 500000000, 800),
  (3, 'Ковер-самолет', 3, 5000000, 3000),
  (4, 'Трах-Тибидох Development', 3, 1000000000, 5000),
  (5, 'Ур Ум Чи', 4, 300000, 1001),
  (6, 'ZBAA Dev', 5, 520000000, 2500),
  (7, 'IBS', 2, 500, 1200);

-- Дамп структуры для таблицы NEW_TABLE 
CREATE TABLE NEW_TABLE AS
  SELECT Con.NAME, COUNT(*)
  FROM COUNTRIES Con
  INNER JOIN CITIES Cit
  ON Cit.COUNTRY_ID = Con.ID
  INNER JOIN COMPANIES Comp
  ON Comp.CITY_ID = Cit.ID
  WHERE Comp.LABORS >= 1000
  GROUP BY Con.NAME;

 
 
 
