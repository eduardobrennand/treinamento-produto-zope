from OFS import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.SistemaSolar.Interface.Interface import Interface

class SistemaSolar(SimpleItem.SimpleItem):
    """Classe SistemaSolar"""

    interface = Interface('interface')
    
    meta_type = 'SistemaSolar'

    manage_options = (
        {'label': 'View', 'action': 'interface/home',},
    )

    def __init__(self, id):
        """Inicializa o produto"""
        self.id = id

def manage_addSistemaSolar(self, id):
   """Adiciona um SistemaSolar"""
   self._setObject(id, SistemaSolar(id))
   self.REQUEST.RESPONSE.redirect('interface/home')

manage_addSistemaSolarForm = PageTemplateFile('zpt/addSistemaSolarForm', globals())