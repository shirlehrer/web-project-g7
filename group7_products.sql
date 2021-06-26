
create table group7.products
(
    p_name  varchar(50) not null,
    type    varchar(50) null,
    price   int         not null,
    picture varchar(50) null,
    constraint products_p_name_uindex
        unique (p_name)
);

alter table group7.products
    add primary key (p_name);


INSERT INTO group7.products (p_name, type, price, picture) VALUES ('Belly Silver Piercing', 'bellybutton_piercing', 15, 'pro1');
INSERT INTO group7.products (p_name, type, price, picture) VALUES ('Ears Flower Piercing', 'earring', 29, 'pro2');
INSERT INTO group7.products (p_name, type, price, picture) VALUES ('Lips Pearls Piercing', 'lips_piercing', 11, 'pro3');
INSERT INTO group7.products (p_name, type, price, picture) VALUES ('Tragos Heart Piercing', 'earring', 25, 'pro4');
INSERT INTO group7.products (p_name, type, price, picture) VALUES ('Star Piercing', 'nose_piercing', 19, 'pro5');
INSERT INTO group7.products (p_name, type, price, picture) VALUES ('Black Widow Piercing', 'nose_piercing', 23, 'pro6');
INSERT INTO group7.products (p_name, type, price, picture) VALUES ('Black Heart Piercing', 'earring', 19, 'pro7');
INSERT INTO group7.products (p_name, type, price, picture) VALUES ('The Big Diamond Piercing', 'bellybutton_piercing', 29, 'pro8');
