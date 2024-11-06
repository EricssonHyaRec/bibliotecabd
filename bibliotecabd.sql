create database if not exists biblioteca;
use biblioteca;

create table if not exists Generos(
	id_genero int auto_increment primary key,
    nombre_categoria  varchar(50) not null
);

create table if not exists Autores(
	id_autor int auto_increment primary key,
    nombre_autor varchar(120) not null
);

create table if not exists Libros(
	id_libro int auto_increment primary key,
    titulo varchar(100) not null,
    id_autor int not null,
    editorial varchar(100) not null,
    anio_publicacion date,
    id_genero int not null,
    cantidad_disponible int,
	foreign key (id_autor) references Autores(id_autor),
    foreign key (id_genero) references Generos(id_genero)
);

create table if not exists Usuarios(
	id_usuario int auto_increment primary key,
    nombre varchar(100) not null,
    apellido varchar(100) not null,
    email varchar(100) not null,
    telefono int not null,
    direccion varchar(120) not null,
    tipo_usuario varchar(50) not null 
);

create table if not exists Prestamos(
	id_prestamo  int auto_increment primary key,
    id_libro  int not null,
    id_usuario  int not null,
    fecha_prestamo date not null,
    fecha_devolucion date,
    estado varchar(120) not null,
	foreign key (id_libro) references Libros(id_libro),
    foreign key (id_usuario) references Usuarios(id_usuario)
);

create table if not exists Multas(
	id_multa int auto_increment primary key,
    id_usuario int not null,
    monto double not null,
    descripcion varchar(120) not null,
    fecha_multa date not null,
    foreign key (id_usuario) references Usuarios(id_usuario)
);


