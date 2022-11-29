from OFS import SimpleItem
from Products.SistemaSolar.Controlador.Planeta.ControladorPlaneta import ControladorPlaneta
from Products.SistemaSolar.Controlador.Lua.ControladorLua import ControladorLua
from Products.SistemaSolar.Models.Planeta.ModelPlaneta import ModelPlaneta
from Products.SistemaSolar.Models.Lua.ModelLua import ModelLua


class Interface(SimpleItem.SimpleItem):
    """Interface do Site SistemaSolar"""

    def __init__(self, id):
        """Inicializando"""
        self.id = id
        self.control_plnt = ControladorPlaneta('control_plnt')
        self.model_plnt = ModelPlaneta('model_plnt')
        self.control_lua = ControladorLua('control_lua')
        self.model_lua = ModelLua('model_lua')
        

    def home(self):
        """Classe Controlador busca os dados a partir de uma query SQL e retorna um ZPT"""
        conteudo = self.model_plnt.listar_planetas()
        
        return self.control_plnt.index_html(planetas=conteudo)

    def planeta(self, id_planeta):
        """Busca um planeta especifico no SQL e retorna o ZPT com os argumentos do planeta"""
        conteudo = self.model_plnt.buscar_planeta(id_planeta=id_planeta)

        return self.control_plnt.planeta_html(planeta=conteudo)

    def editar_planeta(self, id_planeta):
        """Chama a query de buscar planeta e retorna um ZPT com um formulario de edicao ja preenchido"""
        conteudo = self.model_plnt.buscar_planeta(id_planeta=id_planeta)

        return self.control_plnt.editar_planeta_html(planeta=conteudo)

    def editar_report(self, nome, descricao, curiosidades, massa, raio, id_planeta):
        """Chama a query de editar planeta e retorna um ZPT com os dados do formulario"""
        self.model_plnt.editar_planeta(nome=nome, descricao=descricao, curiosidades=curiosidades, massa=massa, raio=raio, id_planeta=id_planeta)

        conteudo = self.model_plnt.buscar_planeta(id_planeta=id_planeta)

        return self.control_plnt.editar_report_html(planeta=conteudo)

    def excluir_confirma(self, id_planeta):
        """Tela para confirmar exclusao do planeta"""
        conteudo = self.model_plnt.buscar_planeta(id_planeta=id_planeta)

        return self.control_plnt.excluir_confirma_html(planeta=conteudo)

    def excluir_planeta(self, id_planeta):
        """Query para excluir planeta"""
        conteudo = self.model_plnt.buscar_planeta(id_planeta=id_planeta)

        self.model_plnt.excluir_planeta(id_planeta=id_planeta)

        return self.control_plnt.excluir_report_html(planeta=conteudo)

    def adicionar_planeta_form(self):
        """Formulario para adicionar novo planeta"""
        return self.control_plnt.adicionar_planeta_html()

    def adicionar_report(self):
        """Adiciona novo planeta e retorna um ZPT confirmando a adicao"""
        self.model_plnt.adicionar_planeta()

        return self.control_plnt.adicionar_report_html()    

    def luas(self, id_planeta):
        """Busca as luas de um determinado planeta e retorna um ZPT."""
        conteudo_planeta = self.model_plnt.buscar_planeta(id_planeta=id_planeta)

        template = self.control_lua.template.macros['template_principal']

        header = self.control_lua.macro_header.macros['header_principal']

        footer = self.control_lua.macro_footer.macros['footer_principal']

        conteudo_lua = self.model_lua.buscar_luas(id_planeta=id_planeta)

        return self.control_lua.luas_html(planeta=conteudo_planeta, luas=conteudo_lua, template=template, header=header, footer=footer)

    def lua(self, id_lua):
        """Busca uma lua especifica e retorna um ZPT com suas informacoes"""
        conteudo = self.model_lua.buscar_lua(id_lua=id_lua)

        template = self.control_lua.template.macros['template_principal']

        header = self.control_lua.macro_header.macros['header_principal']

        footer = self.control_lua.macro_footer.macros['footer_principal']

        return self.control_lua.lua_html(lua=conteudo, template=template, header=header, footer=footer)
    
    def editar_lua(self, id_lua):
        """Chama a query de editar planeta e retorna um ZPT com formulario ja preenchido"""
        conteudo = self.model_lua.buscar_lua(id_lua=id_lua)

        template = self.control_lua.template.macros['template_principal']

        header = self.control_lua.macro_header.macros['header_principal']

        footer = self.control_lua.macro_footer.macros['footer_principal']

        return self.control_lua.editar_lua_html(lua=conteudo, template=template, footer=footer, header=header)

    def editar_lua_report(self, nome, descricao, distancia, id_lua):
        """Edita a lua com os parametros dos formularios"""
        self.model_lua.editar_lua(nome=nome, descricao=descricao, distancia=distancia, id_lua=id_lua)

        conteudo = self.model_lua.buscar_lua(id_lua=id_lua)

        template = self.control_lua.template.macros['template_principal']

        header = self.control_lua.macro_header.macros['header_principal']

        footer = self.control_lua.macro_footer.macros['footer_principal']

        return self.control_lua.editar_lua_report_html(lua=conteudo, template=template, footer=footer, header=header)

    def excluir_lua_confirma(self, id_lua):
        """Tela para confirmar exclusao da Lua"""
        conteudo = self.model_lua.buscar_lua(id_lua=id_lua)

        template = self.control_lua.template.macros['template_principal']

        header = self.control_lua.macro_header.macros['header_principal']

        footer = self.control_lua.macro_footer.macros['footer_principal']

        return self.control_lua.excluir_lua_confirma_html(lua=conteudo, template=template, footer=footer, header=header)

    def excluir_lua(self, id_lua):
        """Tela que confirma a exclusao da lua desejada"""
        conteudo = self.model_lua.buscar_lua(id_lua=id_lua)

        template = self.control_lua.template.macros['template_principal']

        header = self.control_lua.macro_header.macros['header_principal']

        footer = self.control_lua.macro_footer.macros['footer_principal']

        self.model_lua.excluir_lua(id_lua=id_lua)

        return self.control_lua.excluir_lua_report_html(lua=conteudo, template=template, footer=footer, header=header)

    def adicionar_lua(self, id_planeta):
        """Formulario para adicionar nova lova, com id_planeta ja preenchido"""
        conteudo = self.model_plnt.buscar_planeta(id_planeta=id_planeta)

        template = self.control_lua.template.macros['template_principal']

        header = self.control_lua.macro_header.macros['header_principal']

        footer = self.control_lua.macro_footer.macros['footer_principal']

        return self.control_lua.adicionar_lua_html(lua=conteudo, template=template, footer=footer, header=header)

    def adicionar_lua_report(self):
        """Adiciona uma nova lua e retorna um ZPT confirmando a adicao"""
        self.model_lua.adicionar_lua()

        template = self.control_lua.template.macros['template_principal']

        header = self.control_lua.macro_header.macros['header_principal']

        footer = self.control_lua.macro_footer.macros['footer_principal']

        return self.control_lua.adicionar_lua_report_html(template=template, footer=footer, header=header)
    
    


    