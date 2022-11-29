import SistemaSolar

def initialize(context):
    """Inicializa o produto, fazendo-o aparecer na lista do Zope"""
    context.registerClass(
        SistemaSolar.SistemaSolar,
        constructors = (
            SistemaSolar.manage_addSistemaSolarForm,
            SistemaSolar.manage_addSistemaSolar
        )
    )