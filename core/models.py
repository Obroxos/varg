from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Condominio(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Administrador", 
        blank=True,
    )
    rut = models.CharField(max_length=200, verbose_name="RUT", blank=True)
    direccion = models.CharField(max_length=200, verbose_name="Dirección", blank=True)
    comuna = models.CharField(max_length=200, verbose_name="Comuna", blank=True)
    region = models.CharField(max_length=200, verbose_name="Región", blank=True)
    fondo_reserva = models.CharField(max_length=200, verbose_name="Porcentaje de Fondo de Reserva", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "condominio"
        verbose_name_plural = "condominios"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Tarea(models.Model):
    ESTADOS = (
        ('P', 'Pendiente'),
        ('C', 'Completado'),
        ('E', 'Eliminado'),
        ('A', 'Archivado'),
    )
    PRIORIDADES = (
        ('U', 'Urgente'),
        ('R', 'Regular'),
    )
    name = models.CharField(max_length=200, verbose_name="Nombre")
    estado = models.CharField(max_length=1, choices=ESTADOS)
    prioridad = models.CharField(max_length=1, choices=PRIORIDADES)
    vencimiento = models.DateField()
    condominio = models.ForeignKey(Condominio, related_name='tareas', on_delete=models.CASCADE, verbose_name="Condominio",)
    asignado = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Administrador", 
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "tarea"
        verbose_name_plural = "tareas"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Acta(models.Model):
    TIPOS = (
        ('AO', 'Asamblea Ordinaria'),
        ('AEA', 'Asamblea Extraordinaria de Mayoría Absoluta'),
        ('AER', 'Asamblea Extraordinaria de Mayoría Reforzada'),
        ('RC', 'Reunión de Comité'),
        ('D', 'Documento'),
        ('O', 'Otro'),
    )
    comentarios = models.CharField(max_length=200, verbose_name="Comentarios")
    tipo = models.CharField(max_length=3, choices=TIPOS)
    fecha = models.DateField()
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, verbose_name="Condominio",)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "acta"
        verbose_name_plural = "actas"
        ordering = ['-created']

    def __str__(self):
        return self.tipo

class Administrador(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    rut = models.CharField(max_length=200, verbose_name="RUT")
    inicio =  models.DateField()
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, verbose_name="Condominio",)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "administrador"
        verbose_name_plural = "administradores"
        ordering = ['-created']

    def __str__(self):
        return self.rut

class Facultad(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    rut = models.CharField(max_length=200, verbose_name="RUT")
    inicio =  models.DateField()
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, verbose_name="Condominio",)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "facultad"
        verbose_name_plural = "facultades"
        ordering = ['-created']

    def __str__(self):
        return self.rut

class Comite(models.Model):
    CALIDADES = (
        ('P', 'Presidente'),
        ('T', 'Tesorero'),
        ('S', 'Secretario'),
        ('O', 'Otro'),
    )
    name = models.CharField(max_length=200, verbose_name="Nombre", blank=True)
    rut = models.CharField(max_length=200, verbose_name="RUT")
    calidad = models.CharField(max_length=1, choices=CALIDADES, blank=True)
    inicio =  models.DateField(blank=True)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, verbose_name="Condominio",)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "comite"
        verbose_name_plural = "comités"
        ordering = ['-created']

    def __str__(self):
        return self.rut



class Automatizacion(models.Model):
    LANZADORES = (
        ('C', 'Se completa tarea'),
        ('A', 'Se archiva tarea'),
        ('E', 'Se elimina tarea'),
        ('N', 'Se crea tarea nueva tarea'),
    )
    EFECTOS = (
        ('C', 'Crear una nueva tarea'),
        ('C', 'Enviar correo electrónico'),
    )
    lanzador = models.CharField(max_length=1, choices=LANZADORES, blank=True)
    codigo = models.CharField(max_length=200, verbose_name="Código")
    descripcion = models.CharField(max_length=200, verbose_name="Descripción", blank=True)
    efecto = models.CharField(max_length=1, choices=EFECTOS, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "automatizacion"
        verbose_name_plural = "automatizaciones"
        ordering = ['-created']

    def __str__(self):
        return self.codigo




















class Clase(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Autor",
    )
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo", blank=True)
    video = models.CharField(max_length=200, verbose_name="Video", blank=True)
    content = models.TextField(verbose_name="Contenido", blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="media", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "clase"
        verbose_name_plural = "clases"
        ordering = ['-created']

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Autor",
    )
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo", blank=True)
    content = models.TextField(verbose_name="Contenido", blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="media", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ['-created']

    def __str__(self):
        return self.title

class Reglamento(models.Model):
    condominio = models.CharField(max_length=200, verbose_name="Condominio")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Autor",
    )
    file = models.FileField(upload_to = "reglamentos", verbose_name="Documento")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "reglamento"
        verbose_name_plural = "reglamentos"
        ordering = ['-created']

    def __str__(self):
        return self.condominio