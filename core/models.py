from django.db import models


class About(models.Model):
    """Informações sobre você"""

    short_description = models.TextField(verbose_name="Descrição curta")
    description = models.TextField(verbose_name="Descrição completa")
    image = models.ImageField(upload_to="about/", verbose_name="Foto de perfil")

    class Meta:
        verbose_name = "Sobre Mim"
        verbose_name_plural = "Sobre Mim"

    def __str__(self):
        return "Sobre Mim"


class Technology(models.Model):
    """Tecnologias que você domina"""

    name = models.TextField(max_length=100, verbose_name="Nome da tecnologia")
    description = models.TextField(verbose_name="Sobre a tecnologia")

    class Meta:
        verbose_name = "Tecnologia"
        verbose_name_plural = "Tecnologias"

    def __str__(self):
        return str(self.name)


class Project(models.Model):
    """Projeto do porfólio"""

    title = models.CharField(max_length=100, verbose_name="Título do projeto")
    image = models.ImageField(upload_to="projects/", verbose_name="Imagem do projeto")
    github_link = models.URLField(verbose_name="Link do GitHub", blank=True)

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self):
        return str(self.title)


class Experience(models.Model):
    """Experiencia profissionais"""

    name = models.CharField(max_length=100, verbose_name="Empresa/Cargo")
    description = models.TextField(verbose_name="Descricao da experiencia")
    image = models.ImageField(
        upload_to="experiences/", verbose_name="Logo", blank=True, null=True
    )

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"

    def __str__(self):
        return str(self.name)
