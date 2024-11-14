from django import forms  # Importa o módulo de formulários do Django.
from .models import Post  # Importa o modelo Posts do arquivo models.py.

class PostsForm(forms.ModelForm):  # Cria um formulário baseado no modelo Posts.

    UNIDADES_PESO = [
        ('kg', 'Kilogramas'),
        ('ton', 'Toneladas'),
    ]

    unidade_peso = forms.ChoiceField(choices=UNIDADES_PESO, label='Unidade de Peso')  # Campo para selecionar kg ou toneladas

    class Meta:
        model = Post  # Especifica que este formulário será baseado no modelo Posts.
        fields = [
            'dinoNome',          # Nome do dinossauro
            'dinoTipo',          # Tipo do dinossauro
            'dinoDescricao',     # Descrição do dinossauro
            'dinoEpoca',         # Época geológica do dinossauro
            'dinoTamanhoMin',    # Tamanho mínimo do dinossauro
            'dinoTamanhoMax',    # Tamanho máximo do dinossauro
            'unidade_peso',      # Adiciona o campo de unidade de peso acima dos outros campos de peso
            'dinoPesoMin',       # Peso mínimo do dinossauro
            'dinoPesoMax',       # Peso máximo do dinossauro
            'biomas',            # Biomas onde o dinossauro foi encontrado
            'dinoImage'          # Imagem do dinossauro
        ]# Define os campos do modelo que serão incluídos no formulário.

    def __init__(self, *args, **kwargs):  # Método de inicialização do formulário, usado para personalizar a instância do formulário.
        super().__init__(*args, **kwargs)  # Chama o método de inicialização da classe pai (ModelForm).
        for field_name, field in self.fields.items():  # Itera sobre todos os campos do formulário.
            field.widget.attrs['class'] = 'form-control'  # Adiciona a classe CSS 'form-control' a cada campo do formulário para estilização.

        # Ajusta o incremento do campo dinoTamanhoMin para aumentar de 1.0 em 1.0
        self.fields['dinoTamanhoMin'].widget.attrs['step'] = 1.0
        self.fields['dinoTamanhoMax'].widget.attrs['step'] = 1.0

    def clean(self):
        cleaned_data = super().clean()
        unidade_peso = cleaned_data.get('unidade_peso')
        peso_min = cleaned_data.get('dinoPesoMin')
        peso_max = cleaned_data.get('dinoPesoMax')

        if unidade_peso == 'ton':
            # Converte toneladas para kg
            cleaned_data['dinoPesoMin'] = peso_min * 1000 if peso_min else None
            cleaned_data['dinoPesoMax'] = peso_max * 1000 if peso_max else None
        
        return cleaned_data
