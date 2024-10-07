
CREATE TABLE Categoria
(
  id_categoria integer     NOT NULL GENERATED ALWAYS AS IDENTITY,
  nombre       varchar(50) NOT NULL UNIQUE,
  PRIMARY KEY (id_categoria)
);

CREATE TABLE Categoria_museo
(
  id_categoria integer NOT NULL,
  id_museo     integer NOT NULL,
  PRIMARY KEY (id_categoria, id_museo)
);

CREATE TABLE Dia
(
  id_dia integer     NOT NULL GENERATED ALWAYS AS IDENTITY,
  nombre varchar(20) NOT NULL UNIQUE,
  PRIMARY KEY (id_dia)
);

CREATE TABLE Dia_atencion
(
  id_museo integer NOT NULL,
  id_dia   integer NOT NULL,
  PRIMARY KEY (id_museo, id_dia)
);

CREATE TABLE Dia_concurrido
(
  id_museo integer NOT NULL,
  id_dia   integer NOT NULL,
  PRIMARY KEY (id_museo, id_dia)
);

CREATE TABLE Distrito
(
  id_distrito integer     NOT NULL GENERATED ALWAYS AS IDENTITY,
  nombre      varchar(50) NOT NULL UNIQUE,
  PRIMARY KEY (id_distrito)
);

CREATE TABLE Museo
(
  id_museo              integer      NOT NULL GENERATED ALWAYS AS IDENTITY,
  nombre                varchar(200) NOT NULL UNIQUE,
  id_distrito           integer      NOT NULL,
  direccion             varchar(300) NOT NULL,
  puntaje_resena        numeric(2,1) NOT NULL,
  ha_inicio             time         NOT NULL,
  ha_fin                time         NOT NULL,
  hc_inicio             time        ,
  hc_fin                time        ,
  tarifa_normal         numeric(5,2) NOT NULL,
  tarifa_ninos          numeric(5,2),
  tarifa_ancianos       numeric(5,2),
  tarifa_discapacitados numeric(5,2),
  reserva_entrada       boolean      NOT NULL,
  servicio_restaurante  boolean      NOT NULL,
  servicio_cafeteria    boolean      NOT NULL,
  servicio_guiado       boolean      NOT NULL,
  servicio_biblioteca   boolean      NOT NULL,
  venta_objetos         boolean      NOT NULL,
  accesibilidad         boolean      NOT NULL,
  permiso_foto          boolean      NOT NULL,
  estacionamiento       boolean      NOT NULL,
  visita_virtual        boolean      NOT NULL,
  n_restaurantes_prox   int         ,
  n_atracciones_prox    int         ,
  telefono              varchar(9)   UNIQUE,
  anexo                 varchar(5)  ,
  email                 varchar(250) UNIQUE,
  sitio_web             text        ,
  pag_facebook          text        ,
  pag_instagram         text        ,
  pag_tiktok            text        ,
  notas                 text        ,
  PRIMARY KEY (id_museo)
);

COMMENT ON COLUMN Museo.puntaje_resena IS 'reseña';

COMMENT ON COLUMN Museo.ha_inicio IS 'hora atención';

COMMENT ON COLUMN Museo.ha_fin IS 'hora atención';

COMMENT ON COLUMN Museo.hc_inicio IS 'hora concurrencia';

COMMENT ON COLUMN Museo.hc_fin IS 'hora concurrencia';

COMMENT ON COLUMN Museo.tarifa_normal IS 'soles';

COMMENT ON COLUMN Museo.tarifa_ninos IS 'soles';

COMMENT ON COLUMN Museo.tarifa_ancianos IS 'soles';

COMMENT ON COLUMN Museo.tarifa_discapacitados IS 'soles';

ALTER TABLE Museo
  ADD CONSTRAINT FK_Distrito_TO_Museo
    FOREIGN KEY (id_distrito)
    REFERENCES Distrito (id_distrito);

ALTER TABLE Dia_atencion
  ADD CONSTRAINT FK_Museo_TO_Dia_atencion
    FOREIGN KEY (id_museo)
    REFERENCES Museo (id_museo);

ALTER TABLE Dia_atencion
  ADD CONSTRAINT FK_Dia_TO_Dia_atencion
    FOREIGN KEY (id_dia)
    REFERENCES Dia (id_dia);

ALTER TABLE Dia_concurrido
  ADD CONSTRAINT FK_Museo_TO_Dia_concurrido
    FOREIGN KEY (id_museo)
    REFERENCES Museo (id_museo);

ALTER TABLE Dia_concurrido
  ADD CONSTRAINT FK_Dia_TO_Dia_concurrido
    FOREIGN KEY (id_dia)
    REFERENCES Dia (id_dia);

ALTER TABLE Categoria_museo
  ADD CONSTRAINT FK_Categoria_TO_Categoria_museo
    FOREIGN KEY (id_categoria)
    REFERENCES Categoria (id_categoria);

ALTER TABLE Categoria_museo
  ADD CONSTRAINT FK_Museo_TO_Categoria_museo
    FOREIGN KEY (id_museo)
    REFERENCES Museo (id_museo);
