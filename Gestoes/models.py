from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    matricula = models.CharField(max_length=10)
    data_de_ingresso = models.DateField(auto_now_add=True)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    genero = models.CharField(max_length=20)

    class Meta:
        ordering = ['data_de_ingresso']


class Professor(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    formacao = models.CharField(max_length=100)
    data_de_contratacao = models.DateField(auto_now_add=True)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    genero = models.CharField(max_length=20)

    class Meta:
        ordering = ['data_de_contratacao']
        
class Curso(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    carga_horaria = models.PositiveIntegerField()  # Carga horária do curso em horas
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Aula(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    dia_da_semana = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    alunos = models.ManyToManyField(Aluno)

    def __str__(self):
        return f"Aula de {self.nome} - Curso: {self.curso.nome}"
