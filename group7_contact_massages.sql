create table group7.contact_massages
(
    first_name varchar(50)  null,
    last_name  varchar(50)  null,
    email      varchar(255) not null,
    massage    varchar(255) null,
    constraint contact_massages_email_uindex
        unique (email)
);

alter table group7.contact_massages
    add primary key (email);

INSERT INTO group7.contact_massages (first_name, last_name, email, massage) VALUES ('Annemarie', 'Benoy', 'abenoy2@cyberchimps.com', 'My new piercing got infected!');
INSERT INTO group7.contact_massages (first_name, last_name, email, massage) VALUES ('Adrianna', 'White', 'awhite3@parallels.com', 'Would like schedule an appointment for a very big tattoo');
INSERT INTO group7.contact_massages (first_name, last_name, email, massage) VALUES ('Kort', 'Valadez', 'kvaladez0@gov.uk', 'Would like schedule an appointment for next friday');
INSERT INTO group7.contact_massages (first_name, last_name, email, massage) VALUES ('Marketa', 'Tweddell', 'mtweddell1@nbcnews.com', 'Want to change my appointment for tattoo');
INSERT INTO group7.contact_massages (first_name, last_name, email, massage) VALUES ('Raven', 'McIlhatton', 'rmcilhatton4@taobao.com', 'When will the Clear piercing be back in stock?');