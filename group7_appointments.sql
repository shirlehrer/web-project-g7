create table group7.appointments
(
    app_id      int auto_increment
        primary key,
    full_name   varchar(50) null,
    phone       varchar(50)         null,
    email       varchar(50) not null,
    description varchar(50)        null
);