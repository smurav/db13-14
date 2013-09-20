/* Delete the tables if they already exist */
drop table if exists University;
drop table if exists Student;
drop table if exists Apply;

/* Create the schema for our tables */
create table University(uName varchar(255), region varchar(255), enrollment int);
create table Student(sID int, sName varchar(255), GPA float, sizeHS int);
create table Apply(sID int, uName varchar(255), major varchar(255), decision varchar(1));

/* Populate the tables with our data */
insert into University values ('MEPhI', 'Moscow', 9000);
insert into University values ('MSU', 'Moscow', 40000);
insert into University values ('NSU', 'Novosibirsk', 6500);
insert into University values ('MSTU', 'Moscow', 18800);
insert into University values ('NSTU', 'Novosibirsk', 25000);
insert into University values ('DVFU', 'Vladivostok', 40000);
insert into University values ('SSU', 'Saratov', 27000);
insert into University values ('RUDN', 'Moscow', 25000);

insert into Student values (1, 'Tschingis Khan', 4.2, 1000);
insert into Student values (2, 'Petr I', 4.1, 1000);
insert into Student values (5, 'Elena Vaenga', 4.4, 3000);
insert into Student values (6, 'Dima Bilan', 4.1, 2000);
insert into Student values (8, 'Dmitry Medvedev', 4.7, 5000);
insert into Student values (9, 'Evelina Khromchenko', 4.0, 3000);
insert into Student values (13, 'Vasya Sidorov', 5.0, 1500);
insert into Student values (14, 'Alexander Gradskiy', 4.8, 4000);
insert into Student values (17, 'Alexander Makedonsky', 4.9, 1);
insert into Student values (18, 'Al-Horezmi', 5.0, 1);
insert into Student values (19, 'Vladimir Lenin', 5.0, 500);
insert into Student values (20, 'Nikola Tesla', 5.0, 50);
insert into Student values (21, 'Albert Einstein', 4.9, 500);
insert into Student values (22, 'Boris Godunov', 3.5, 2);
insert into Student values (23, 'Stas Mikhailov', 3.3, 100);
insert into Student values (24, 'Jason Statham ', 4.0, 100);

insert into Apply values (1, 'MEPhI', 'CS', 'Y');
insert into Apply values (1, 'SSU', 'BE', 'Y');
insert into Apply values (1, 'MSTU', 'Mathematics', 'N');
insert into Apply values (1, 'NSU', 'History', 'Y');

insert into Apply values (2, 'MEPhI', 'CS', 'N');
insert into Apply values (2, 'MSU', 'History', 'Y');
insert into Apply values (2, 'SSU', 'History', 'Y');

insert into Apply values (5, 'MEPhI', 'CS', 'N');
insert into Apply values (5, 'NSTU', 'Physics', 'N');
insert into Apply values (5, 'NSU', 'History', 'N');
insert into Apply values (5, 'MSU', 'Sociology', 'Y');

insert into Apply values (6, 'MEPhI', 'CS', 'Y');
insert into Apply values (6, 'MEPhI', 'EE', 'N');
insert into Apply values (6, 'MSU', 'CS', 'N');
insert into Apply values (6, 'DVFU', 'History', 'N');
insert into Apply values (6, 'DVFU', 'Music', 'Y');
insert into Apply values (6, 'SSU', 'History', 'N');
insert into Apply values (6, 'SSU', 'Music', 'Y');

insert into Apply values (18, 'MEPhI', 'CS', 'Y');
insert into Apply values (18, 'MEPhI', 'History', 'Y');
insert into Apply values (18, 'MEPhI', 'EE', 'N');
insert into Apply values (18, 'SSU', 'CS', 'Y');
insert into Apply values (18, 'NSU', 'History', 'N');
insert into Apply values (18, 'NSTU', 'EE', 'Y');

insert into Apply values (19, 'MEPhI', 'History', 'Y');
insert into Apply values (19, 'MEPhI', 'EE', 'N');
insert into Apply values (19, 'MSU', 'History', 'Y');
insert into Apply values (19, 'NSU', 'History', 'N');
insert into Apply values (19, 'SSU', 'Music', 'Y');

insert into Apply values (20, 'MEPhI', 'CS', 'Y');
insert into Apply values (20, 'MSU', 'CS', 'Y');
insert into Apply values (20, 'NSU', 'CS', 'Y');
insert into Apply values (20, 'DVFU', 'CS', 'Y');
insert into Apply values (20, 'NSU', 'BE', 'N');
insert into Apply values (20, 'DVFU', 'History', 'N');

insert into Apply values (21, 'MEPhI', 'CS', 'N');
insert into Apply values (21, 'MSU', 'CS', 'Y');
insert into Apply values (21, 'MSU', 'Mathematics', 'Y');
insert into Apply values (21, 'MSU', 'Physics', 'Y');
insert into Apply values (21, 'NSTU', 'CS', 'N');
insert into Apply values (21, 'DVFU', 'CS', 'Y');
insert into Apply values (21, 'DVFU', 'Physics', 'Y');
insert into Apply values (21, 'MSU', 'BE', 'N');
insert into Apply values (21, 'SSU', 'History', 'N');

insert into Apply values (22, 'MEPhI', 'BE', 'N');
insert into Apply values (22, 'MSU', 'CS', 'N');
insert into Apply values (22, 'NSU', 'History', 'Y');
insert into Apply values (22, 'MSTU', 'Physics', 'N');
insert into Apply values (22, 'NSTU', 'BE', 'N');
insert into Apply values (22, 'DVFU', 'History', 'Y');
insert into Apply values (22, 'SSU', 'History', 'N');

insert into Apply values (23, 'SSU', 'History', 'N');
insert into Apply values (23, 'SSU', 'Music', 'Y');
