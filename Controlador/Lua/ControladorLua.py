from OFS import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Globals import package_home

import os

global product_path

product_path = os.path.join(package_home(globals())) + '/'

class ControladorLua(SimpleItem.SimpleItem):
    """Controlador para buscar queries SQL"""
    
    def __init__(self, id):
        """Inicializa o produto"""
        self.id = id
        
    
    luas_html = PageTemplateFile('zpt/luas_html', globals())

    lua_html = PageTemplateFile('zpt/lua_html', globals())

    editar_lua_html = PageTemplateFile('zpt/editar_lua_html', globals())

    editar_lua_report_html = PageTemplateFile('zpt/editar_lua_report_html', globals())

    excluir_lua_confirma_html = PageTemplateFile('zpt/excluir_lua_confirma_html', globals())

    excluir_lua_report_html = PageTemplateFile('zpt/excluir_lua_report_html', globals())

    adicionar_lua_html = PageTemplateFile('zpt/adicionar_lua_html', globals())

    adicionar_lua_report_html = PageTemplateFile('zpt/adicionar_lua_report_html', globals())

    template = PageTemplateFile('../Planeta/zpt/template', globals())

    macro_header = PageTemplateFile('../Planeta/zpt/header', globals())

    macro_footer = PageTemplateFile('../Planeta/zpt/footer', globals())