drop table VCSUsage;
drop table VCS;
drop table CourseUsage;
drop table Student;
drop table StudentGroup;
drop table Course;

create table StudentGroup (
  gid serial primary key,
  name varchar(64),
  email varchar(255)
);
create table Student (
  sid serial primary key,
  name varchar(64),
  surname varchar(64) not null,
  email varchar(255),
  gid serial,
  constraint gid_exists foreign key(gid) references StudentGroup(gid) on delete restrict
);
create table Course (
  cid serial primary key,
  name varchar(64),
  short_name varchar(64)
);
create table VCS (
  vid serial primary key,
  name varchar(64),
  url varchar(255)
);
create table VCSUsage (
  vuid serial primary key,
  sid serial,
  vid serial,
  login varchar(64),
  constraint sid_exists foreign key(sid) references Student(sid) on delete restrict,
  constraint vid_exists foreign key(vid) references VCS(vid) on delete restrict
);
create table CourseUsage (
  aid serial primary key,
  sid serial,
  cid serial,
  constraint sid_exists foreign key(sid) references Student(sid) on delete restrict,
  constraint cid_exists foreign key(cid) references Course(cid) on delete restrict
);

insert into StudentGroup (name, email) values ('K2-362', 'kib362_2012@mail.ru');
insert into StudentGroup (name, email) values ('K2-361', 'k361_2012@mail.ru');
insert into StudentGroup (name, email) values ('K7-361', 'k07.361@yandex.com');
insert into StudentGroup (name, email) values ('K5-361', 'kirichenkotm@gmail.com');

insert into Student (surname, name, email, gid) values ('Akhmetsafin', 'Vladislav', 'wlad008@rambler.ru', 1);
insert into Student (surname, name, email, gid) values ('Galkin', 'Alexander', 'dragon609@yandex.ru', 1);
insert into Student (surname, name, email, gid) values ('Golovko', 'Irina', 'irina.golovko.mephi@mail.ru', 1);
insert into Student (surname, name, email, gid) values ('Dzhumailo', 'Eugeny', 'froz5man@gmail.com', 1);
insert into Student (surname, name, email, gid) values ('Erokhin', 'Vladimir', 'erokhin94@gmail.com', 1);
insert into Student (surname, name, email, gid) values ('Katalkina', 'Viktoria', 'v.katalkina@mail.ru', 1);
insert into Student (surname, name, email, gid) values ('Levin', 'Andrey', 'bembi773@gmail.com', 1);
insert into Student (surname, name, email, gid) values ('Molochkov', 'Yaroslav', 'lestylolz@gmail.com', 1);
insert into Student (surname, name, email, gid) values ('Polstyankin', 'Konstantin', 'p-kot395@yandex.ru', 1);
insert into Student (surname, name, email, gid) values ('Purik', 'Yana', 'def4onka-yana@yandex.ru', 1);
insert into Student (surname, name, email, gid) values ('Razzhivin', 'Nikita', 'nrazzhivin@gmail.com', 1);
insert into Student (surname, name, email, gid) values ('Redyuk', 'Sergey', 'sergred@gmail.com', 1);
insert into Student (surname, name, email, gid) values ('Ryabov', 'Petr', 'agekor@yandex.ru', 1);
insert into Student (surname, name, email, gid) values ('Skok', 'Darya', 'skok-poskok0307@mail.ru', 1);
insert into Student (surname, name, email, gid) values ('Strekalov', 'Oleg', 'ostrekalov305@mail.ru', 1);
insert into Student (surname, name, email, gid) values ('Chukhnenko', 'Alexandra', 'chukhnenko.sasha@rambler.ru', 1);
insert into Student (surname, name, email, gid) values ('Moryashova', 'Viktoria', 'vika5050@mail.ru', 1);

insert into Student (surname, name, email, gid) values ('Anisimova', 'Natalya', 'anata1510@yandex.ru', 2);
insert into Student (surname, name, email, gid) values ('Bubenko', 'Kirill', 'virmant@mail.ru', 2);
insert into Student (surname, name, email, gid) values ('Dzheloukhova', 'Alena', 'alder333@mail.ru', 2);
insert into Student (surname, name, email, gid) values ('Zamanov', 'Ainur', 'zaman3915@mail.ru', 2);
insert into Student (surname, name, email, gid) values ('Kustov', 'Daniil', 'kustdan@gmail.com', 2);
insert into Student (surname, name, email, gid) values ('Mikheev', 'Denis', 'shelbyterlingua@mail.ru', 2);
insert into Student (surname, name, email, gid) values ('Osennova', 'Ulyana', 'osennova.ulyana@mail.ru', 2);
insert into Student (surname, name, email, gid) values ('Pivovarov', 'Alexander', 'killogram94@yandex.ru', 2);
insert into Student (surname, name, email, gid) values ('Samsonov', 'Artem', 'samsonov68rus@gmail.com', 2);
insert into Student (surname, name, email, gid) values ('Solovieva', 'Anna', '481727@mail.ru', 2);
insert into Student (surname, name, email, gid) values ('Sukhanova', 'Lyubov', 'lubovvs@mail.ru', 2);
insert into Student (surname, name, email, gid) values ('Tarmazakov', 'Eugeny', 'tarmazakov@mail.ru', 2);
insert into Student (surname, name, email, gid) values ('Titorenko', 'Alexey', 'letter@mephist.ru', 2);
insert into Student (surname, name, email, gid) values ('Ushakova', 'Alexandra', 'sashenka.94@inbox.ru', 2);
insert into Student (surname, name, email, gid) values ('Shtanko', 'Alexander', 'shtanko-mephi@yandex.ru', 2);

insert into Student (surname, name, email, gid) values ('Alekseev', 'Dmitry', null, 3);
insert into Student (surname, name, email, gid) values ('Busanova', 'Viktoria', null, 3);
insert into Student (surname, name, email, gid) values ('Zhukov', 'Kirill', null, 3);
insert into Student (surname, name, email, gid) values ('Kazymova', 'Yulia', null, 3);
insert into Student (surname, name, email, gid) values ('Melnik', 'Leonid', null, 3);
insert into Student (surname, name, email, gid) values ('Ovchinnikov', 'Igor', null, 3);
insert into Student (surname, name, email, gid) values ('Rybnikov', 'Vitaly', null, 3);
insert into Student (surname, name, email, gid) values ('Sychugov', 'Alexey', null, 3);
insert into Student (surname, name, email, gid) values ('Tolstov', 'Dmitry', null, 3);
insert into Student (surname, name, email, gid) values ('Ukhobotova', 'Olga', null, 3);

insert into Student (surname, name, email, gid) values ('Vishtak', 'Tatyana', 'tmv529@mail.ru', 4);
insert into Student (surname, name, email, gid) values ('Volchkov', 'Pavel', 'pashteter@mail.ru', 4);
insert into Student (surname, name, email, gid) values ('Deineko', 'Alexey', 'deynekoaa@gmail.com', 4);
insert into Student (surname, name, email, gid) values ('Ivanov', 'Dmitry', 'ivadmi5@gmail.com', 4);
insert into Student (surname, name, email, gid) values ('Kirichenko', 'Tatyana', 'kirichenkotm@gmail.com', 4);
insert into Student (surname, name, email, gid) values ('Lubennikova', 'Anastasia', 'lav1946@mail.ru', 4);
insert into Student (surname, name, email, gid) values ('Ostroumov', 'Alexander', 'sashiksashik@yandex.ru', 4);
insert into Student (surname, name, email, gid) values ('Perceva', 'Ekaterina', 'catsvord@yandex.ru', 4);
insert into Student (surname, name, email, gid) values ('Ponomarev', 'Sergey', 'spsergey13@gmail.com', 4);
insert into Student (surname, name, email, gid) values ('Popova', 'Valeria', 'lera9436@mail.ru', 4);
insert into Student (surname, name, email, gid) values ('Semenikhin', 'Dmitry', 'semenikhindv@mail.ru', 4);
insert into Student (surname, name, email, gid) values ('Shamsutdinov', 'Rinat', 'shamsutdinovr7@gmail.com', 4);

insert into VCS (name, url) values ('bitbucket', 'bitbucket.org');
insert into VCS (name, url) values ('github', 'github.com');

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('alex609' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Galkin';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('igolovko' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Golovko';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('levinandrey' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Levin';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('molochkov' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Molochkov';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('kostikpolst' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Polstyankin';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('kostikpolst' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Polstyankin';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('achukhne' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Chukhnenko';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('ajeloukhova' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Dzheloukhova';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('anisimova' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Anisimova';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('apivovar' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Pivovarov';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('ashtanko' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Shtanko';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('asolovie' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Solovieva';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('atitorenko' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Titorenko';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('aushakova' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Ushakova';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('azamanov' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Zamanov';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('dskok' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Skok';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('hardrain' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Ryabov';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('kbubenko' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Bubenko';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('lsukhanova' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Sukhanova';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('nrazzhivin' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Razzhivin';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('o5win' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Erokhin';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('ostrekalov' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Strekalov';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('sergred' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Redyuk';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('vmoryashova' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Moryashova';

insert into VCSUsage (sid, vid, login)
  select S.sid, V.vid, cast('zhekon' as varchar(64)) as login from Student S,VCS V
  where V.name='bitbucket' and S.surname='Dzhumailo';

insert into Course (name, short_name) values ('Programming Course', 'pcourse');
insert into Course (name, short_name) values ('Databases', 'dbcourse');

insert into CourseUsage (sid, cid)
  select S.sid, C.cid from Student S, Course C
  where S.gid=1 and C.short_name='pcourse';

insert into CourseUsage (sid, cid)
  select S.sid, C.cid from Student S, Course C
  where S.gid=2 and C.short_name='pcourse';

insert into CourseUsage (sid, cid)
  select S.sid, C.cid from Student S, Course C
  where S.gid=3 and C.short_name='dbcourse';

insert into CourseUsage (sid, cid)
  select S.sid, C.cid from Student S, Course C
  where S.gid=4 and C.short_name='dbcourse';
