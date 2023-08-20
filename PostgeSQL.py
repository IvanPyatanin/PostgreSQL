create table Jenres
(
	Jenres_id int primary key,
	Jenresname not null
)

create table Musiciants
(
	Musiciant_id int primary key,
	Musicianname varchar(64) not null,
	Nickname nvarchar(64) not null
)

create table J_M
(
	Musiciant_id int foreign key references Musiciants(Musiciant_id),
	Jenres_id integer references Jenres(Jenres_id),
	primary key(Musiciant_id, Jenres_id)
)

create table Albums
(
	Album_id int primary key,
	Albumname varchar(64) not null,
	Albumdata int not null
)

create table M_A
(
	Musiciant_id integer references Musiciants(Musiciant_id),
	Album_id integer references Albums(Album_id)
)

create table Tracks
(
	Track_id int primary key,
	Trackname varchar(64) not null,
	Album_id integer references Albums(Album_id)
)

create table Collection
(
	Collection_id int primary key,
	Collectionname varchar(64) not null,
	Collectindata int not null
)

create table T_C
(
	Track_id integer references Tracks(Track_id),
	Collection_id integer references Collections(Collection_id)
)