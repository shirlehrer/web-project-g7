create table group7.cart
(
    p_name   varchar(50)   not null,
    user_name varchar(50)	not null,
    quantity int default 1 null,
    price int not null,
    constraint cart_orders_user_name_fk
        foreign key (user_name) references group7.users (user_name),
    constraint cart_products_p_name_fk
        foreign key (p_name) references group7.products (p_name)
);