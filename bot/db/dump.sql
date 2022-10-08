DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS menu_buttons_table;
DROP TABLE IF EXISTS config;
DROP TABLE IF EXISTS accesses;
CREATE TABLE IF NOT EXISTS users(user_id integer NOT NULL,date timestamp NOT NULL,command text NOT NULL);
CREATE TABLE IF NOT EXISTS menu_buttons_table(user_id INT NOT NULL, button TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS config(user_id integer NOT NULL,keyboard_buttons text NOT NULL,is_writing boolean NOT NULL,button_to_write text NOT NULL);
CREATE TABLE IF NOT EXISTS accesses(user_id integer NOT NULL,full_admin_panel BOOLEAN NOT NULL,	semi_admin_panel BOOLEAN NOT NULL,headman_panel BOOLEAN NOT NULL,stream_group TEXT);

-- Старосты бвт
INSERT INTO accesses VALUES(255632502, False, False, True, 'бвт2101');
INSERT INTO accesses VALUES(228506651, False, False, True, 'бвт2102');
INSERT INTO accesses VALUES(355129349, False, False, True, 'бвт2103');
INSERT INTO accesses VALUES(116008591, False, False, True, 'бвт2104');
INSERT INTO accesses VALUES(237079184, False, False, True, 'бвт2105');
INSERT INTO accesses VALUES(216653267, False, False, True, 'бвт2106');
INSERT INTO accesses VALUES(230880631, False, False, True, 'бвт2107');
INSERT INTO accesses VALUES(228882211, False, False, True, 'бвт2108');

-- Я, Ваня, Саня, Оксана, Макс
INSERT INTO accesses VALUES(210481885, True, True, True, 'бвт2103');
INSERT INTO accesses VALUES(162956112, True, True, True, 'бвт2103');
INSERT INTO accesses VALUES(213304238, False, True, False, NULL);
INSERT INTO accesses VALUES(528860991, False, True, False, NULL);
INSERT INTO accesses VALUES(278233695, False, True, False, NULL);

-- Старосты бфи
INSERT INTO accesses VALUES(284518456, False, False, True, 'бфи2102');
INSERT INTO accesses VALUES(553894671, False, False, True, 'бфи2101');
