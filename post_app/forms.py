from django import forms  # Importa o módulo de formulários do Django.
from .models import Post, DinoTipoDeDino, DinoEpoca, DinoDieta, DinoBioma  # Altere para Post se você estiver usando esse modelo

class PostsForm(forms.ModelForm):  # Cria um formulário baseado no modelo Posts.

    UNIDADES_PESO = [
        ('kg', 'Kilogramas'),
        ('ton', 'Toneladas'),
    ]

    # Sobrescrevendo os campos para adicionar queryset
    dinoTipo = forms.ModelChoiceField(
        queryset=DinoTipoDeDino.objects.all(),
        empty_label="Selecione um tipo",
        label="Tipo do Dinossauro"
    )
    
    dinoEpoca = forms.ModelChoiceField(
        queryset=DinoEpoca.objects.all(),
        empty_label="Selecione uma época",
        label="Época"
    )
    
    dinoDieta = forms.ModelChoiceField(
        queryset=DinoDieta.objects.all(),
        empty_label="Selecione uma dieta",
        label="Dieta"
    )
    
    biomas = forms.ModelMultipleChoiceField(
        queryset=DinoBioma.objects.all(),
        label="Biomas",
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    unidade_peso = forms.ChoiceField(
        choices=UNIDADES_PESO, 
        label='Unidade de Peso', 
        required=True
    )

    class Meta:
        model = Post  # Especifica que este formulário será baseado no modelo Posts.
        fields = [
            'dinoNome',
            'dinoTipo',
            'dinoDescricao',
            'dinoEpoca',
            'dinoDieta',
            'dinoTamanhoMin',
            'dinoTamanhoMax',
            'unidade_peso',
            'dinoPesoMin',
            'dinoPesoMax',
            'biomas',
            'dinoImage'
        ]
        labels = {
            'dinoNome': 'Nome do Dinossauro',
            'dinoDescricao': 'Descrição',
            'dinoTamanhoMin': 'Tamanho Mínimo (m)',
            'dinoTamanhoMax': 'Tamanho Máximo (m)',
            'dinoPesoMin': 'Peso Mínimo',
            'dinoPesoMax': 'Peso Máximo',
            'dinoImage': 'Imagem do Dinossauro'
        }

    def __init__(self, *args, **kwargs):  # Método de inicialização do formulário, usado para personalizar a instância do formulário.
        super().__init__(*args, **kwargs)  # Chama o método de inicialização da classe pai (ModelForm).
        for field_name, field in self.fields.items():  # Itera sobre todos os campos do formulário.
            field.widget.attrs['class'] = 'form-control'  # Adiciona a classe CSS 'form-control' a cada campo do formulário para estilização.
            
            # Adiciona placeholders específicos
            if field_name == 'dinoNome':
                field.widget.attrs['placeholder'] = 'Digite o nome do dinossauro'
            elif field_name == 'dinoDescricao':
                field.widget.attrs['placeholder'] = 'Digite a descrição do dinossauro'
                field.widget.attrs['rows'] = 4

        # Configuração dos campos numéricos
        self.fields['dinoTamanhoMin'].widget.attrs.update({
            'step': '0.1',
            'min': '0'
        })
        self.fields['dinoTamanhoMax'].widget.attrs.update({
            'step': '0.1',
            'min': '0'
        })
        self.fields['dinoPesoMin'].widget.attrs.update({
            'min': '0'
        })
        self.fields['dinoPesoMax'].widget.attrs.update({
            'min': '0'
        })

    def clean(self):
        cleaned_data = super().clean()
        
        # Validação de tamanho
        tamanho_min = cleaned_data.get('dinoTamanhoMin')
        tamanho_max = cleaned_data.get('dinoTamanhoMax')
        if tamanho_min and tamanho_max and tamanho_min > tamanho_max:
            raise forms.ValidationError('O tamanho mínimo não pode ser maior que o máximo.')

        # Validação e conversão de peso
        peso_min = cleaned_data.get('dinoPesoMin')
        peso_max = cleaned_data.get('dinoPesoMax')
        unidade_peso = cleaned_data.get('unidade_peso')

        if peso_min and peso_max and peso_min > peso_max:
            raise forms.ValidationError('O peso mínimo não pode ser maior que o máximo.')

        if unidade_peso == 'ton':
            # Converte toneladas para kg
            cleaned_data['dinoPesoMin'] = peso_min * 1000 if peso_min else None
            cleaned_data['dinoPesoMax'] = peso_max * 1000 if peso_max else None

        return cleaned_data

class DinoForm(forms.ModelForm):
    class Meta:
        model = Post  # Ou o modelo que você deseja usar
        fields = [
            'dinoNome',
            'dinoTipo',
            'dinoDescricao',
            'dinoEpoca',
            'dinoDieta',
            'dinoTamanhoMin',
            'dinoTamanhoMax',
            'dinoPesoMin',
            'dinoPesoMax',
            'biomas',
            'dinoImage'
        ]
