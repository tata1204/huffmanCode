-- Crea la tabla de usuarios
create table usuarios (
  nombre text not null,
  apellido text not null,
  id text NOT NULL,
  correo text not null,
  usuario text PRIMARY KEY not null,
  contraseña text not null
); 