from OFS import SimpleItem
from Products.ZSQLMethods.SQL import SQL
from Globals import package_home

import os

global product_path

product_path = os.path.join(package_home(globals())) + '/'

class ModelLua(SimpleItem.SimpleItem):
    """Classe Model para luas"""
    
    def __init__(self, id):
        """Inicializa o produto"""
        self.id = id
    
    buscar_luas = SQL(id='buscar_luas', title='',
                    connection_id='Psycopg2_database_connection',
                    arguments='id_planeta',
                    template=open(product_path + 'sql/buscar_luas.sql').read()
                    )   
    
    buscar_lua = SQL(id='buscar_lua', title='',
                    connection_id='Psycopg2_database_connection',
                    arguments='id_lua',
                    template=open(product_path + 'sql/buscar_lua.sql').read()
                    ) 

    editar_lua = SQL(id='editar_lua', title='',
                    connection_id='Psycopg2_database_connection',
                    arguments='nome descricao distancia id_lua',
                    template=open(product_path + 'sql/editar_lua.sql').read()
                    ) 

    excluir_lua = SQL(id='excluir_lua', title='',
                    connection_id='Psycopg2_database_connection',
                    arguments='id_lua',
                    template=open(product_path + 'sql/excluir_lua.sql').read()
                    ) 
    
    adicionar_lua = SQL(id='adicionar_lua', title='',
                            connection_id='Psycopg2_database_connection',
                            arguments='id_planeta nome descricao distancia',
                            template=open(product_path + 'sql/adicionar_lua.sql').read()
                            )