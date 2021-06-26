create table group7.users
(
    first_name varchar(50)  not null,
    last_name  varchar(50)  not null,
    user_name  varchar(50)  not null,
    email      varchar(255) not null
        primary key,
    password   varchar(20)  not null,
    constraint users_user_name_uindex
        unique (user_name)
);

INSERT INTO group7.users (first_name, last_name, user_name, email, password) VALUES ('Brant', 'Watchorn', 'brantt', 'bwatchorn2q@cdc.gov', 'g1tr61');
INSERT INTO group7.users (first_name, last_name, user_name, email, password) VALUES ('Elsinore', 'Bickerton', 'els635', 'ebickerton2m@foxnews.com', 't6w4t1');
INSERT INTO group7.users (first_name, last_name, user_name, email, password) VALUES ('roger', 'michal', 'mic', 'george.bluth@reqres.in', '456');
INSERT INTO group7.users (first_name, last_name, user_name, email, password) VALUES ('Ginnifer', 'Herche', 'Gen123', 'gherche2r@163.com', '156311');
INSERT INTO group7.users (first_name, last_name, user_name, email, password) VALUES ('Joelle', 'Ponton', 'jolllenne', 'jponton2p@hp.com', '456h1dfrt');
INSERT INTO group7.users (first_name, last_name, user_name, email, password) VALUES ('Joanna', 'Salasar', 'joannnaa', 'jsalasar2o@accuweather.com', 'g4t65');
INSERT INTO group7.users (first_name, last_name, user_name, email, password) VALUES ('Kelcy', 'Burress', 'kel79', 'kburress2l@nationalgeographic.com', '4fr6');
INSERT INTO group7.users (first_name, last_name, user_name, email, password) VALUES ('chir', 'lehrer', 'chir', 'leh@post.bgu.ac.il', '951');
INSERT INTO group7.users (first_name, last_name, user_name, email, password) VALUES ('Michele', 'Poupard', 'michel123', 'mpoupard2n@ox.ac.uk', 'gtr654');
