from django.views.generic import TemplateView

# View para a pagina inicial com herança de TemplateView
class IndexView(TemplateView):
    template_name = "paginas/index.html"