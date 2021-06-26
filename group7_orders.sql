create table group7.orders
(
    order_id   int 					not null primary key,
    first_name varchar(50)                          null,
    last_name  varchar(50)                          null,
    email      varchar(50)                          null,
    CC         int                          	not null,
    CVV        int                                  not null,
	amount     int                               not null
);