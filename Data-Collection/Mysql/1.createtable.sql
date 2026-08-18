CREATE database college;
CREATE database if not exists college;

CREATE database if not exists instagram;
drop database instagram;
drop database if exists instagram;

show databases;

USE college;

CREATE TABLE student(
 rollno int,
 name varchar(50),
 age int
);

insert into student
values
(101,"adam", 12),
(102,"bob",14);

select * from student;



create database if not exists instagram;
use instagram;

create table user(
-- id int primary key,
id int,
age int,
name varchar(50) not null,
email varchar(100) unique,
followers int default 0,
following int,
constraint age_check CHECK (age >=13),
primary key(id)
);

create table posts(
id int primary key,
content text,
user_id int,
foreign key (user_id) references user(id)
);

