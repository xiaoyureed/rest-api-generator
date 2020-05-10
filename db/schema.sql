create database dbtest;

create table product
(
	id serial not null
		constraint product_pk
			primary key,
	name text default '' not null,
	price decimal default 0 not null,
	create_date timestamp default now() not null
);

comment on table product is 'product';

comment on column product.name is 'product name';

comment on column product.price is 'product price
';

comment on column product.create_date is 'create date';

