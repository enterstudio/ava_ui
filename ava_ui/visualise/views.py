from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from ava_ui.abstract.views import ObjectIndex


def graph_data(request, pk):
    """
    Generates a JSON object containing the nodes to display on a D3 graph.
    :param request: The current HTTP request.
    :param pk: The identifier of the LDAP configuration to be graphed.
    """
    parameters = get_object_or_404(LDAPConfiguration, pk=pk)
    exp = ExportLDAP()
    json_data = exp.generate_graph(parameters)
    return JsonResponse(json_data)


class GraphIndex(ObjectIndex):
    template_name = 'visualise/visualise_index.html'
    url_suffix = '/organize/people/'

    def get(self, request):
        return super(GraphIndex, self).get(template_name=self.template_name, request=request,
                                           url_suffix=self.url_suffix)
