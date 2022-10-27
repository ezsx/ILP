-- Generated by Oracle SQL Developer Data Modeler 19.2.0.182.1216
--   at:        2022-10-25 13:47:02 MSK
--   site:      Oracle Database 12cR2
--   type:      Oracle Database 12cR2



CREATE TABLE car (
    id              NUMBER NOT NULL,
    brand           VARCHAR2(25),
    country         VARCHAR2(25),
    color           VARCHAR2(25),
    dealership_id   NUMBER(5) NOT NULL
);

ALTER TABLE car ADD CONSTRAINT car_pk PRIMARY KEY ( id );

CREATE TABLE car_in_action (
    id          NUMBER NOT NULL,
    car_id      NUMBER NOT NULL,
    rentdate    VARCHAR2(25),
    enddate     VARCHAR2(25),
    isback      VARCHAR2(25),
    penalty     VARCHAR2(25),
    leaser_id   NUMBER NOT NULL
);

ALTER TABLE car_in_action ADD CONSTRAINT car_in_action_pk PRIMARY KEY ( id );

CREATE TABLE dealership (
    id       NUMBER(5) NOT NULL,
    city     VARCHAR2(25),
    street   VARCHAR2(25)
);

ALTER TABLE dealership ADD CONSTRAINT dealership_pk PRIMARY KEY ( id );

CREATE TABLE leaser (
    id          NUMBER NOT NULL,
    name        VARCHAR2(25),
    surname     VARCHAR2(25),
    birthdate   VARCHAR2(25),
    address     VARCHAR2(25),
    tel         VARCHAR2(15)
);

ALTER TABLE leaser ADD CONSTRAINT leaser_pk PRIMARY KEY ( id );

ALTER TABLE car
    ADD CONSTRAINT car_dealership_fk FOREIGN KEY ( dealership_id )
        REFERENCES dealership ( id );

ALTER TABLE car_in_action
    ADD CONSTRAINT car_in_action_car_fk FOREIGN KEY ( car_id )
        REFERENCES car ( id );

ALTER TABLE car_in_action
    ADD CONSTRAINT car_in_action_leaser_fk FOREIGN KEY ( leaser_id )
        REFERENCES leaser ( id );



-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                             4
-- CREATE INDEX                             0
-- ALTER TABLE                              7
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
