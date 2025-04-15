from django.db import models

class Gestores(models.Model):
    nome = models.CharField(max_length=255)
    ni = models.IntegerField()
    cargo = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    is_superUser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

class Responsaveis(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    ni = models.IntegerField()
    gestor = models.ForeignKey( Gestores, on_delete=models.SET_NULL, null=True, blank=True)
    is_superUser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

class Manutentores(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    gestor = models.ForeignKey(Gestores, on_delete=models.SET_NULL, null=True, blank=True)
    is_superUser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

class Patrimonios(models.Model):
    localizacao = models.IntegerField()
    ni = models.IntegerField()
    descricao = models.TextField()

class Ambientes(models.Model):
    sig = models.IntegerField()
    descricao = models.CharField(max_length=255)
    ni = models.IntegerField()
    responsavel = models.ForeignKey(Responsaveis, on_delete=models.SET_NULL, null=True, blank=True)

class OrdemServico(models.Model):
    descricao_servico = models.TextField()
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_encerramento = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    prioridade = models.CharField(max_length=255)
    patrimonio = models.ForeignKey(Patrimonios, on_delete=models.SET_NULL, null=True, blank=True)
    ambiente = models.ForeignKey(Ambientes, on_delete=models.SET_NULL, null=True, blank=True)
    responsavel = models.ForeignKey(Responsaveis, on_delete=models.SET_NULL, null=True, blank=True)
    manutentor = models.ForeignKey(Manutentores, on_delete=models.SET_NULL, null=True, blank=True)