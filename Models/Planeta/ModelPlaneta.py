from OFS import SimpleItem
from Products.ZSQLMethods.SQL import SQL
from Globals import package_home

import os

global product_path

product_path = os.path.join(package_home(globals())) + '/'

class ModelPlaneta(SimpleItem.SimpleItem):
    """Classe Model para planetas"""
    
    def __init__(self, id):
        """Inicializa o produto"""
        self.id = id
    
    listar_planetas = SQL(id='listar_panetas', title='',
                          connection_id='Psycopg2_database_connection',
                          arguments='',
                          template=open(product_path + 'sql/listar_planetas.sql').read()  
                        )
    
    buscar_planeta = SQL(id='buscar_planeta', title='',
                         connection_id='Psycopg2_database_connection',
                         arguments='id_planeta',
                         template=open(product_path + 'sql/buscar_planeta.sql').read()
                        )
    
    editar_planeta = SQL(id='editar_planeta', title='',
                        connection_id='Psycopg2_database_connection',
                        arguments='nome descricao curiosidades massa raio id_planeta',
                        template=open(product_path + 'sql/editar_planeta.sql').read()
                        )
    
    excluir_planeta = SQL(id='excluir_planeta', title='',
                        connection_id='Psycopg2_database_connection',
                        arguments='id_planeta',
                        template=open(product_path + 'sql/excluir_planeta.sql').read()
                        )

    adicionar_planeta = SQL(id='adicionar_planeta', title='',
                            connection_id='Psycopg2_database_connection',
                            arguments='nome descricao curiosidades massa raio img_url',
                            template=open(product_path + 'sql/adicionar_planeta.sql').read()
                            )