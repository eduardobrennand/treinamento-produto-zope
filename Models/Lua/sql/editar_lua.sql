UPDATE luas
SET 
nome = <dtml-sqlvar nome type=string>, 
descricao = <dtml-sqlvar descricao type=string>,
distancia = <dtml-sqlvar distancia type=int>
WHERE id_lua = <dtml-sqlvar id_lua type=int>