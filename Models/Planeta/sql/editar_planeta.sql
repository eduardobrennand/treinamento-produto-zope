UPDATE public.planetas
SET 
nome = <dtml-sqlvar nome type=string>, 
descricao = <dtml-sqlvar descricao type=string>, 
curiosidades = <dtml-sqlvar curiosidades type=string>, 
massa=<dtml-sqlvar massa type=int>, 
raio=<dtml-sqlvar raio type=float>
WHERE id_planeta=<dtml-sqlvar id_planeta type=int>