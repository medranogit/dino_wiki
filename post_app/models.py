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
        verbose_name = 'Epoca'
        verbose_name_plural = 'Epocas'
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
    dinoNome = models.CharField(max_length=100)  # Nome do dinossauro, com limite de 100 caracteres.
    dinoTipo = models.ForeignKey(DinoTipoDeDino, on_delete=models.CASCADE)  # Associação com TipoDeDino, com chave estrangeira.
    dinoDescricao = models.TextField()  # Descrição detalhada do dinossauro.
    dinoEpoca = models.ForeignKey(DinoEpoca, on_delete=models.CASCADE)  # Associação com Epoca, com chave estrangeira.
    dinoDieta = models.ForeignKey(DinoDieta, on_delete=models.CASCADE)  # Associação com DinoDieta, com chave estrangeira.

    # Tamanho mínimo e máximo do dinossauro em metros
    dinoTamanhoMin = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.0)])  # Tamanho mínimo
    dinoTamanhoMax = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.0)])  # Tamanho máximo
    
    # Peso mínimo e máximo do dinossauro em quilogramas
    dinoPesoMin = models.IntegerField(validators=[MinValueValidator(0)])  # Peso mínimo
    dinoPesoMax = models.IntegerField(validators=[MinValueValidator(0)])  # Peso máximo
    
    biomas = models.ManyToManyField(DinoBioma)  # Associação muitos-para-muitos com o modelo Bioma.
    
    dinoImage = models.ImageField(upload_to='images/')  # Imagem do dinossauro, salva na pasta 'images/'.
    dinoCreateDate = models.DateTimeField(auto_now_add=True)  # Data e hora de criação do registro, definida automaticamente.

    def __str__(self):
        return self.dinoNome  # Exibe o nome do dinossauro como representação do objeto.

    def clean(self):
        # Validação para garantir que o tamanho mínimo não seja maior que o tamanho máximo
        if self.dinoTamanhoMin > self.dinoTamanhoMax:
            raise ValidationError('O tamanho mínimo não pode ser maior que o tamanho máximo.')

        # Validação para garantir que o peso mínimo não seja maior que o peso máximo
        if self.dinoPesoMin > self.dinoPesoMax:
            raise ValidationError('O peso mínimo não pode ser maior que o peso máximo.')

    class Meta:  # Classe interna usada para definir opções de metadados para o modelo.
        verbose_name = 'Criatura'  # Nome singular a ser exibido no admin do Django.
        verbose_name_plural = 'Criaturas'  # Nome plural a ser exibido no admin do Django.
        ordering = ['id']  # Define a ordenação padrão dos objetos desse modelo, pela ordem crescente do campo 'id'.
    
# Explicação dos Campos:
# dinoNome: Utiliza CharField, ideal para strings curtas, como o nome de um dinossauro. O parâmetro max_length=100 define o tamanho máximo que o nome pode ter.
# dinoEspecie: Utiliza TextField, adequado para armazenar a espécie do dinossauro, permitindo entradas de texto mais longas.
# dinoDescricao: Outro TextField, utilizado aqui para uma descrição detalhada do dinossauro, permitindo que você insira uma quantidade maior de texto.
# dinoImage: Utiliza ImageField para armazenar imagens relacionadas ao dinossauro. O parâmetro upload_to='images/' especifica que as imagens serão salvas na pasta images/ dentro do diretório de uploads.
# dinoCreateDate: Utiliza DateTimeField com auto_now_add=True, que automaticamente define o campo com a data e hora no momento em que o registro é criado. Isso é útil para rastrear quando o registro foi criado.