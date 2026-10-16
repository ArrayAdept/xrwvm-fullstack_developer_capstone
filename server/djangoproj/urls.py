from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),

    # Frontend single-page app routes
    path('', TemplateView.as_view(template_name="Home.html"), name='home'),
    path('login/', TemplateView.as_view(template_name="index.html"), name='login_page'),
    path('register/', TemplateView.as_view(template_name="index.html"), name='register_page'),
    path('dealers/', TemplateView.as_view(template_name="index.html"), name='dealers_page'),
    path('dealer/<int:dealer_id>', TemplateView.as_view(template_name="index.html"), name='dealer_detail_page'),
    path('postreview/<int:dealer_id>', TemplateView.as_view(template_name="index.html"), name='post_review_page'),

    # Static pages
    path('about/', TemplateView.as_view(template_name="About.html"), name='about'),
    path('contact/', TemplateView.as_view(template_name="Contact.html"), name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)