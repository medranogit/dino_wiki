from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

# Os Models no Django são a maneira como você define a estrutura dos dados da sua aplicação. 
# Eles representam as tabelas no banco de dados e cada model é uma classe Python que herda de django.db.models.Model. 
# Dentro dessa classe, você define os campos do seu modelo, que correspondem às colunas da tabela no banco de dados.

# Modelo Bioma
class DinoBioma(models.Model):
    nome = models.CharField(max_length=100)  # Nome do bioma, com limite de 100 caracteres.

    def __str__(self):
        return self.nome  # Exibe o nome do bioma como representação do objeto.

    class Meta:
        verbose_name = 'Bioma'
        verbose_name_plural = 'Biomas'
        ordering = ['nome']  # Ordena os biomas por nome.

class DinoEpoca(models.Model):
    nome = models.CharField(max_length=100)  # Nome da época geológica, com limite de 100 caracteres.

    def __str__(self):
        return self.nome  # Exibe o nome da época como representação do objeto.

    class Meta:
        verbose_name = 'Época'
        verbose_name_plural = 'Épocas'
        ordering = ['nome']  # Ordena as épocas por nome.

# Modelo TipoDeDino
class DinoTipoDeDino(models.Model):
    nome = models.CharField(max_length=100)  # Nome do tipo de dinossauro, com limite de 100 caracteres.

    def __str__(self):
        return self.nome  # Exibe o nome do tipo de dinossauro como representação do objeto.

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['nome']  # Ordena os tipos de dinossauros por nome.

# Modelo DinoDieta
class DinoDieta(models.Model):
    nome = models.CharField(max_length=100)  # Nome do tipo de dinossauro, com limite de 100 caracteres.

    def __str__(self):
        return self.nome  # Exibe o nome do tipo de dinossauro como representação do objeto.

    class Meta:
        verbose_name = 'Dieta'
        verbose_name_plural = 'Dietas'
        ordering = ['nome']  # Ordena os tipos de dinossauros por nome.

# Create your models here.
class Post(models.Model):
    dinoNome = models.CharField(max_length=100)
    dinoTipo = models.ForeignKey(DinoTipoDeDino, on_delete=models.CASCADE)
    dinoDescricao = models.TextField()
    dinoEpoca = models.ForeignKey(DinoEpoca, on_delete=models.CASCADE)
    dinoDieta = models.ForeignKey(DinoDieta, on_delete=models.CASCADE)
    dinoTamanhoMin = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.0)])
    dinoTamanhoMax = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.0)])
    dinoPesoMin = models.IntegerField(validators=[MinValueValidator(0)])
    dinoPesoMax = models.IntegerField(validators=[MinValueValidator(0)])
    biomas = models.ManyToManyField(DinoBioma)
    dinoImage = models.ImageField(upload_to='images/', blank=True, null=True)
    dinoCreateDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dinoNome

    def clean(self):
        if self.dinoTamanhoMin > self.dinoTamanhoMax:
            raise ValidationError('O tamanho mínimo não pode ser maior que o tamanho máximo.')
        if self.dinoPesoMin > self.dinoPesoMax:
            raise ValidationError('O peso mínimo não pode ser maior que o peso máximo.')

    class Meta:
        verbose_name = 'Dinossauro'
        verbose_name_plural = 'Dinossauros'
        ordering = ['id']

class Dino(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.ForeignKey(DinoTipoDeDino, on_delete=models.CASCADE)
    dieta = models.ForeignKey(DinoDieta, on_delete=models.CASCADE)
    epoca = models.ForeignKey(DinoEpoca, on_delete=models.CASCADE)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.nome