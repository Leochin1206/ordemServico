from django.db import models

class Gestores(models.Model):
    nome = models.CharField(max_length=255)
    ni = models.IntegerField()
    cargo = models.CharField(max_length=255)
    area = models.CharField(max_length=255)

class Responsaveis(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    ni = models.IntegerField()
    gestor = models.ForeignKey( Gestores, on_delete=models.SET_NULL, null=True, blank=True)

class Manutentores(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    ni = models.IntegerField()
    area = models.CharField(max_length=255)

class Patrimonios(models.Model):
    localizacao = models.IntegerField()
    ni = models.IntegerField()
    descricao = models.TextField()

class Ambientes(models.Model):
    num_sala = models.IntegerField()
    num_sig = models.IntegerField()
    descricao_sig = models.CharField(max_length=255)
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

class Historico(models.Model):
    ordem = models.ForeignKey(OrdemServico, on_delete=models.SET_NULL, null=True, blank=True)
    descricao_manutencao = models.TextField()