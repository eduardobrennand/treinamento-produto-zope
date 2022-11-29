INSERT INTO luas(
            id_planeta, nome, descricao, distancia)
    VALUES (
    <dtml-sqlvar id_planeta type="int">,
    <dtml-sqlvar nome type="string">,
    <dtml-sqlvar descricao type="string">,
    <dtml-sqlvar distancia type="int">
    )