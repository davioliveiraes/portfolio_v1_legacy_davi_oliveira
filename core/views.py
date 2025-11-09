from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import About, Technology, Project


class HomeTemplateView(TemplateView):
    """View principal de home"""

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.first()
        context["technologies"] = Technology.objects.all()
        context["projects"] = Project.objects.all()
        return context


def contato(request):
    """View de contato"""
    if request.method == "POST":
        nome = request.POST.get("name")
        email = request.POST.get("email")
        mensagem = request.POST.get("message")

        assunto = f"Mensagem de {nome}"
        corpo_mensagem = f"Nome: {nome}\nEmail: {email}\n\nMensagem:\n {mensagem}"

        try:
            send_mail(
                assunto,
                corpo_mensagem,
                email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            messages.success(request, "Mensagem enviada com sucesso!")
        except OSError as error:
            messages.error(request, f"Erro ao enviar mensagem: {error}")

        return redirect("contato")

    return render(request, "home.html")
