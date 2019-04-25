from pyramid.view import view_config


@view_config(route_name='home', renderer="templates/mytemplate.pt")
def my_view(request):
    return {'project': 'Vue2'}


@view_config(route_name='vue2', renderer="templates/template_vue2.pt")
def view_vue2(request):
    return {'project': 'Vue2'}
