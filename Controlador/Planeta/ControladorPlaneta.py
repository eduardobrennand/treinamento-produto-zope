from OFS import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Globals import package_home

import os

global product_path

product_path = os.path.join(package_home(globals())) + '/'

class ControladorPlaneta(SimpleItem.SimpleItem):
    """Controlador para buscar queries SQL"""
    
    def __init__(self, id):
        """Inicializa o produto"""
        self.id = id    

    index_html = PageTemplateFile('zpt/index_html', globals())  

    planeta_html = PageTemplateFile('zpt/planeta_html', globals())

    editar_planeta_html = PageTemplateFile('zpt/editar_planeta_html', globals())

    editar_report_html = PageTemplateFile('zpt/editar_report_html', globals())

    excluir_confirma_html = PageTemplateFile('zpt/excluir_confirma_html', globals())

    excluir_report_html = PageTemplateFile('zpt/excluir_report_html', globals())

    adicionar_planeta_html = PageTemplateFile('zpt/adicionar_planeta_html', globals())

    adicionar_report_html = PageTemplateFile('zpt/adicionar_report_html', globals())

    template = PageTemplateFile('zpt/template', globals())

    header = PageTemplateFile('zpt/header', globals())

    footer = PageTemplateFile('zpt/footer', globals())