INSERT INTO planetas(
            nome, descricao, curiosidades, massa, raio, 
            img_url)
    VALUES (
    <dtml-sqlvar nome type="string">,
    <dtml-sqlvar descricao type="string">,
    <dtml-sqlvar curiosidades type="string">,
    <dtml-sqlvar massa type="int">,
    <dtml-sqlvar raio type="float">,
    <dtml-sqlvar img_url type="string">);