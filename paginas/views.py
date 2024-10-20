from django.views.generic import TemplateView
from cadastros.models import Produto, Prefeitura, OrdemDeCompra

# View para a pagina inicial com herança de TemplateView
class IndexView(TemplateView):
    template_name = "paginas/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # Listar os últimos 10 produtos
        context['ultimos_produtos'] = Produto.objects.all().order_by('-id')[:5]
        
        # Contar a quantidade total de produtos
        context['quantidade_total_produtos'] = Produto.objects.count()
        
        # Contar a quantidade total de prefeituras
        context['quantidade_total_prefeituras'] = Prefeitura.objects.count()
        
        # Obter a última prefeitura cadastrada
        context['ultima_prefeitura'] = Prefeitura.objects.all().order_by('-id').first()
        
        # Contar a quantidade total de ordens de compra
        context['quantidade_total_ordens_de_compra'] = OrdemDeCompra.objects.count()

        return context


class SobreView(TemplateView):
    template_name = "paginas/sobre.html"