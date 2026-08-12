#Comandos de criação da database caso não exista 
create database if not exists SAEP;

use SAEP;

#Tabela de Produtos

create table if not exists produtos(
	id_produto INT primary key auto_increment,
    nome_produto VARCHAR(100),
    valor_unitario DECIMAL(10,2),
    categoria VARCHAR(100),
    unidade_medida VARCHAR(100),
    quantidade_produto INT
);


#Tabela de entradas

create table if not exists entradas(
	id_entrada INT primary key auto_increment,
    id_produto INT,
    data_entrada DATETIME,
    quantidade_entrada int,
    
    foreign key(id_produto) references produtos(id_produto)
);

#Tabela de saidas

create table if not exists saidas(
	id_saida INT primary key auto_increment,
    id_produto INT,
    data_saida DATETIME,
    quantidade_saida int,
    
    foreign key(id_produto) references produtos(id_produto)
);



#Insercao de valores na tabela de produtos

INSERT INTO produtos(nome_produto,valor_unitario,categoria,unidade_medida,quantidade_produto)
VALUES
	("pano xadrez",5.00,"panos","cm",5),
    ("limpador veja",8.00,"limpadores","ml",30),
    ("sabonete nivea",2.99,"sabonetes","g",45),
    ("sacos de lixo",2.00,"sacos","L",80),
    ("cera liqida incolor 5L",80,"ceras liquidas","L",15),
    ("balde plastico 15L",15,"baldes","L",20);
    

INSERT INTO entradas(id_produto,data_entrada,quantidade_entrada)
VALUES
	(1,"2026-01-05 07:50:00",2),
    (2,"2025-05-06 07:50:00",3),
    (3,"2026-07-05 07:50:00",20),
    (4,"2026-07-05 07:50:00",15),
    (5,"2024-12-05 07:50:00",10);
    

INSERT INTO saidas(id_produto,data_saida,quantidade_saida)
VALUES
	(1,"2026-02-05 08:50:00",5),
    (2,"2025-05-07 08:50:00",3),
    (3,"2026-07-06 08:50:00",10),
    (4,"2026-09-05 09:50:00",5),
    (5,"2025-11-05 10:20:00",2);



#Criação da VIEW vw_estoque

create view vw_estoque as
	select
		id_produto,
		nome_produto,
        quantidade_produto,
        valor_unitario,
        (valor_unitario * quantidade_produto) as "Valor Total"
	from produtos;
    
select * from vw_estoque;
        
	
	
    

    
    
    
	







