INSERT INTO pi3_usuario VALUES ('Edgard', '000.000.000-01', 'edgard@gmail.com', '31 90000 0001','00000-001','Nada a declarar',TRUE);
INSERT INTO pi3_usuario VALUES ('Raissa', '000.000.000-02', 'raissa@gmail.com', '31 90000 0002','00000-002','Nada a declarar',TRUE);
INSERT INTO pi3_usuario VALUES ('Iolanda', '000.000.000-03', 'iolanda@gmail.com', '31 90000 0003','00000-003','Nada a declarar',TRUE);
INSERT INTO pi3_usuario VALUES ('Jonas', '000.000.000-04', 'jonas@gmail.com', '31 90000 0004','00000-004','Nada a declarar',TRUE);

INSERT INTO pi3_editora(nome) VALUES ('Veneta');
INSERT INTO pi3_editora(nome) VALUES ('WMF Martins Fontes');

INSERT INTO pi3_autor(nome) VALUES ('Karl Marx');
INSERT INTO pi3_autor(nome) VALUES ('J.R.R. Tolkien');

SET @HOJE = '';
SELECT CURRENT_DATE() INTO @HOJE;
INSERT INTO pi3_livro(isbn, titulo, data_aquisicao, estado, autor_id, editora_id, status) VALUES ('978-8563137272','O Capital', @HOJE, 'Usado - Bom estado de conservação',1,1,TRUE);
INSERT INTO pi3_livro(isbn, titulo, data_aquisicao, estado, autor_id, editora_id, status) VALUES ('978-6555480184','O Manifesto Comunista', @HOJE, 'Usado - Mau estado de conservação',1,1,TRUE);
INSERT INTO pi3_livro(isbn, titulo, data_aquisicao, estado, autor_id, editora_id, status) VALUES ('978-8578271121','O Hobbit', @HOJE, 'Novo',2,2,TRUE);
INSERT INTO pi3_livro(isbn, titulo, data_aquisicao, estado, autor_id, editora_id, status) VALUES ('978-8595083653','A Queda de Gondolin', @HOJE, 'Novo',2,2,TRUE);