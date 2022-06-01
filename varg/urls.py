from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# Login decorathor
from django.contrib.auth.decorators import login_required
# Staff decorathor
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path('', core_views.LandingView.as_view(), name='landing'),
    path('ley/', core_views.ley, name='ley'),
    path('asambleas/', core_views.asambleas, name='asambleas'),
    path('plan/', core_views.plan, name='plan'),
    path('completado/', core_views.completado, name='completado'),
    path('fallido/', core_views.fallido, name='fallido'),
    path('blog/', core_views.PostListView.as_view(), name='blog'),
    path('blog/<pk>/', core_views.PostDetailView.as_view(), name='post'),
    path('clase/', core_views.ClaseListView.as_view(), name='clases'),
    path('clase/<pk>/', core_views.ClaseDetailView.as_view(), name='clase'),

    path('condominio/', core_views.CondominioListView.as_view(), name='condominios'),
    path('condominio/<pk>/', core_views.CondominioDetailView.as_view(), name='condominio'),

    path('automatizacion/', core_views.AutomatizacionListView.as_view(), name='automatizaciones'),
    path('automatizacion/<pk>/', core_views.AutomatizacionDetailView.as_view(), name='automatizacion'),

    path('django/', admin.site.urls),
    path('dashboard/', staff_member_required(core_views.dashboard), name='dashboard'),
    path('admin/entradas/', staff_member_required(core_views.PostListView.as_view(template_name="core/admin_entradas.html")), name='admin_entradas'),
    path('admin/entradas/crear/', staff_member_required(core_views.PostCreate.as_view()), name='admin_entradas_crear'),
    path('admin/entradas/<pk>', staff_member_required(core_views.PostUpdateView.as_view())),
    path('admin/entradas/<pk>/eliminar/', staff_member_required(core_views.PostDeleteView.as_view())),   
    path('admin/clases/', staff_member_required(core_views.ClaseListView.as_view(template_name="core/admin_clases.html")), name='admin_clases'),
    path('admin/clases/crear/', staff_member_required(core_views.ClaseCreate.as_view()), name='admin_clases_crear'),
    path('admin/clases/<pk>', staff_member_required(core_views.ClaseUpdateView.as_view())),
    path('admin/clases/<pk>/eliminar/', staff_member_required(core_views.ClaseDeleteView.as_view())),   

    path('admin/condominios/', staff_member_required(core_views.CondominioListView.as_view(template_name="core/admin_condominios.html")), name='admin_condominios'),
    path('admin/condominios/crear/', staff_member_required(core_views.CondominioCreate.as_view()), name='admin_condominios_crear'),
    path('admin/condominios/<pk>', staff_member_required(core_views.CondominioUpdateView.as_view())),
    path('admin/condominios/<pk>/eliminar/', staff_member_required(core_views.CondominioDeleteView.as_view())),   

    path('admin/automatizaciones/', staff_member_required(core_views.AutomatizacionListView.as_view(template_name="core/admin_automatizacion.html")), name='admin_automatizaciones'),
    path('admin/automatizaciones/crear/', staff_member_required(core_views.AutomatizacionCreate.as_view()), name='admin_automatizacion_crear'),
    path('admin/automatizaciones/<pk>', staff_member_required(core_views.AutomatizacionUpdateView.as_view())),
    path('admin/automatizaciones/<pk>/eliminar/', staff_member_required(core_views.AutomatizacionDeleteView.as_view())),   




    path('perfil/', login_required(core_views.perfil), name='perfil'),
    path("registro/", users_views.SignUpView.as_view(), name="registro"),

    path('cuenta/', include('django.contrib.auth.urls')),
    path('salir/', auth_views.LogoutView.as_view(), name='salir'),
    path('ingreso/', auth_views.LoginView.as_view(), name='ingreso'),
    path('password/', auth_views.PasswordChangeView.as_view()),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)