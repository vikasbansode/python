-- Example : create table

create table project(
	name text primary key,
	description text,
	deadline date
	);

-- Task are steps that can be taken to complete a project

create table task(
	id integer primary key autoincrement not null,
	priority integer default 1,
	details text,
	status text,
	deadline date,
	completed_on date,
	project text not null references project(name)
	);