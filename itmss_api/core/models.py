from django.db import models

# Create your models here.

class HeadQuarter(models.Model):
    cnpj = models.CharField('CNPJ', max_length=18)
    address = models.CharField('Logradouro', max_length=150)
    city = models.CharField('Cidade', max_length=100)
    country = models.CharField('País', max_length=50)


    def __str__(self) -> str:
        return self.cnpj

class Department(models.Model):
    cost_center = models.CharField("Centro de Custos", max_length=20)
    name = models.CharField("Nome", max_length=25)

    def __str__(self) -> str:
        return self.name

class Employee(models.Model):
    name = models.CharField('Nome completo', max_length=100)
    email = models.EmailField('E-mail de contato', max_length=120)
    phone = models.CharField('Telefone', max_length=15)
    birth = models.DateField('Data de nascimento', auto_now=False, auto_now_add=False)
    admission = models.DateField('Data de Ingresso', auto_now=False, auto_now_add=False)
    shutdown = models.DateField('Data de Desligamento', auto_now=False, auto_now_add=False)
    active = models.BooleanField('Ativo', default=True)
    city = models.CharField('Cidade', max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='departments'
    )
    headquarter = models.ForeignKey(
        HeadQuarter,
        on_delete=models.CASCADE,
        related_name='headquarters'
    )