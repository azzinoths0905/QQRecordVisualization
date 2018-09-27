CREATE TABLE chat_log
(
    id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name varchar(20),
    qq varchar(20),
    content text,
    datetime DATETIME,
    `from` varchar(50)
);
CREATE UNIQUE INDEX table_name_id_uindex ON char_log (id);