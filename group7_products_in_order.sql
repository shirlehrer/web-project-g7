create table group7.products_in_order
(
    p_name   varchar(50)   not null,
    order_id int           not null,
    quantity int default 1 not null,
    price int 			 not null,
    constraint products_in_order_orders_order_id_fk
        foreign key (order_id) references group7.orders (order_id),
    constraint products_in_order_products_p_name_fk
        foreign key (p_name) references group7.products (p_name)
);
