-- Crea la tabla de usuarios
create table historial (
  usuario text not null,
  code_decode text not null,
  frase text not null,
  diccionario json  not null,
  huffman text not null
); 