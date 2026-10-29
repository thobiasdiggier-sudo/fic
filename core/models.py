from django.db import models

class Area(models.Model):
    nome = models.CharField('Nome', max_length=100)

class Publico(models.Model):
    nome = models.CharField('Nome', max_length=100)

class Curso(models.Model):
    titulo = models.CharField('Título', max_length=200)
    descricao = models.TextField('Descrição', blank=True, null=True)
    vagas = models.IntegerField('Vagas')
    carga_horaria = models.IntegerField('Carga Horária')
    data = models.DateField('Data de Início')
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    publico = models.ManyToManyField(Publico)


'''
Estamos trabalhando com ORM
- Modelagem Objeto-Relacional
- Modelar o banco de dados diretamente
na aplicação através de classes e 
objetos
'''
