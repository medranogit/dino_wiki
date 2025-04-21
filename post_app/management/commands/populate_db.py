from django.core.management.base import BaseCommand
from django.db import transaction

from post_app.models import (
    DinoBioma, DinoEpoca, DinoTipoDeDino, DinoDieta, Dino, Post
)


class Command(BaseCommand):
    help = 'Popula o banco de dados com dados iniciais de dinossauros e referências'

    @transaction.atomic
    def handle(self, *args, **options):
        # Dados iniciais
        biomas = ['Floresta', 'Deserto', 'Pantanal', 'Planície']
        epocas = ['Triássico', 'Jurássico', 'Cretáceo']
        tipos = [
            'Theropoda', 'Sauropoda', 'Ornithopoda', 'Ankylosauria', 'Stegosauria',
            'Ceratopsia', 'Pachycephalosauria', 'Prosauropoda', 'Thyreophora',
            'Marginocephalia', 'Hadrosauridae', 'Coelurosauria', 'Carnosauria',
            'Spinosauria', 'Abelisauridae', 'Oviraptorosauria', 'Troodontidae',
            'Dromaeosauridae', 'Psittacosauridae', 'Nodosauridae'
        ]
        dietas = ['Carnívoro', 'Herbívoro', 'Onívoro']

        self.stdout.write('Criando Biomas...')
        for nome in biomas:
            DinoBioma.objects.get_or_create(nome=nome)

        self.stdout.write('Criando Épocas...')
        for nome in epocas:
            DinoEpoca.objects.get_or_create(nome=nome)

        self.stdout.write('Criando Tipos de Dinossauro...')
        for nome in tipos:
            DinoTipoDeDino.objects.get_or_create(nome=nome)

        self.stdout.write('Criando Dietas...')
        for nome in dietas:
            DinoDieta.objects.get_or_create(nome=nome)

        # Dinos iniciais
        exemplos = [
            {'nome': 'Tyrannosaurus Rex', 'tipo': 'Theropoda', 'dieta': 'Carnívoro','epoca': 'Cretáceo', 'descricao': 'Um dos maiores dinossauros carnívoros.','biomas': ['Floresta', 'Planície'], 'tamanho_min': 10.0, 'tamanho_max': 12.0,'peso_min': 7000, 'peso_max': 9000, 'image_path': 'images/Rex.png'},
            {'nome': 'Triceratops', 'tipo': 'Ceratopsia', 'dieta': 'Herbívoro','epoca': 'Cretáceo', 'descricao': 'Herbívoro de três chifres.','biomas': ['Planície'], 'tamanho_min': 8.0, 'tamanho_max': 9.0,'peso_min': 6000, 'peso_max': 8000, 'image_path': 'images/Triceratops.png'},
            {'nome': 'Velociraptor', 'tipo': 'Coelurosauria', 'dieta': 'Carnívoro', 'epoca': 'Cretáceo', 'descricao': 'Pequeno mas ágil predador.', 'biomas': ['Deserto', 'Planície'], 'tamanho_min': 2.0, 'tamanho_max': 3.0, 'peso_min': 15, 'peso_max': 20, 'image_path': 'images/Velociraptor.png'},
            {'nome': 'Brachiosaurus', 'tipo': 'Sauropoda', 'dieta': 'Herbívoro', 'epoca': 'Jurássico', 'descricao': 'Grande pescoçudo de patas dianteiras altas.', 'biomas': ['Floresta', 'Planície'], 'tamanho_min': 18.0, 'tamanho_max': 22.0, 'peso_min': 28000, 'peso_max': 56000, 'image_path': 'images/Brachiosaurus.png'},
            {'nome': 'Stegosaurus', 'tipo': 'Stegosauria', 'dieta': 'Herbívoro', 'epoca': 'Jurássico', 'descricao': 'Dino com placas ao longo do dorso.', 'biomas': ['Floresta', 'Planície'], 'tamanho_min': 7.0, 'tamanho_max': 9.0, 'peso_min': 2500, 'peso_max': 3500, 'image_path': 'images/Stegosaurus.png'},
            {'nome': 'Allosaurus', 'tipo': 'Carnosauria', 'dieta': 'Carnívoro', 'epoca': 'Jurássico', 'descricao': 'Predador ágil de médio porte.', 'biomas': ['Floresta'], 'tamanho_min': 8.0, 'tamanho_max': 12.0, 'peso_min': 1500, 'peso_max': 2200, 'image_path': 'images/Allosaurus.png'},
            {'nome': 'Diplodocus', 'tipo': 'Sauropoda', 'dieta': 'Herbívoro', 'epoca': 'Jurássico', 'descricao': 'Longa cauda e pescoço fino.', 'biomas': ['Planície'], 'tamanho_min': 24.0, 'tamanho_max': 27.0, 'peso_min': 10000, 'peso_max': 16000, 'image_path': 'images/Diplodocus.png'},
            {'nome': 'Spinosaurus', 'tipo': 'Spinosauria', 'dieta': 'Carnívoro', 'epoca': 'Cretáceo', 'descricao': 'Semi-aquático, com vela nas costas.', 'biomas': ['Pantanal', 'Deserto'], 'tamanho_min': 12.0, 'tamanho_max': 15.0, 'peso_min': 7000, 'peso_max': 9000, 'image_path': 'images/Spinosaurus.png'},
            {'nome': 'Ankylosaurus', 'tipo': 'Ankylosauria', 'dieta': 'Herbívoro', 'epoca': 'Cretáceo', 'descricao': 'Corpuzal blindado com clava caudal.', 'biomas': ['Planície'], 'tamanho_min': 6.0, 'tamanho_max': 8.0, 'peso_min': 6000, 'peso_max': 8000, 'image_path': 'images/Ankylosaurus.png'},
            {'nome': 'Iguanodon', 'tipo': 'Ornithopoda', 'dieta': 'Herbívoro', 'epoca': 'Cretáceo', 'descricao': 'Herbívoro bípedo/quadrúpede.', 'biomas': ['Floresta', 'Planície'], 'tamanho_min': 10.0, 'tamanho_max': 13.0, 'peso_min': 3500, 'peso_max': 5000, 'image_path': 'images/Iguanodon.png'},
            {'nome': 'Parasaurolophus', 'tipo': 'Hadrosauridae', 'dieta': 'Herbívoro', 'epoca': 'Cretáceo', 'descricao': 'Cresta alongada acima do crânio.', 'biomas': ['Planície'], 'tamanho_min': 10.0, 'tamanho_max': 12.0, 'peso_min': 2500, 'peso_max': 3000, 'image_path': 'images/Parasaurolophus.png'},
            {'nome': 'Pachycephalosaurus', 'tipo': 'Pachycephalosauria', 'dieta': 'Herbívoro', 'epoca': 'Cretáceo', 'descricao': 'Crânio espesso usado em disputas.', 'biomas': ['Floresta'], 'tamanho_min': 4.0, 'tamanho_max': 5.0, 'peso_min': 450, 'peso_max': 550, 'image_path': 'images/Pachycephalosaurus.png'},
            {'nome': 'Carnotaurus', 'tipo': 'Abelisauridae', 'dieta': 'Carnívoro', 'epoca': 'Cretáceo', 'descricao': 'Predador sul-americano com chifres curtos.', 'biomas': ['Deserto', 'Planície'], 'tamanho_min': 8.0, 'tamanho_max': 9.0, 'peso_min': 1500, 'peso_max': 2000, 'image_path': 'images/Carnotaurus.png'},
            {'nome': 'Oviraptor', 'tipo': 'Oviraptorosauria', 'dieta': 'Onívoro', 'epoca': 'Cretáceo', 'descricao': 'Famoso por suposto roubo de ovos.', 'biomas': ['Pantanal', 'Floresta'], 'tamanho_min': 1.0, 'tamanho_max': 2.0, 'peso_min': 30, 'peso_max': 35, 'image_path': 'images/Oviraptor.png'},
            {'nome': 'Troodon', 'tipo': 'Troodontidae', 'dieta': 'Carnívoro', 'epoca': 'Cretáceo', 'descricao': 'Dino pequeno e inteligente.', 'biomas': ['Floresta'], 'tamanho_min': 2.0, 'tamanho_max': 3.0, 'peso_min': 45, 'peso_max': 60, 'image_path': 'images/Troodon.png'},
            {'nome': 'Deinonychus', 'tipo': 'Dromaeosauridae', 'dieta': 'Carnívoro', 'epoca': 'Cretáceo', 'descricao': 'Garras afiadas em cada pé.', 'biomas': ['Floresta', 'Planície'], 'tamanho_min': 3.0, 'tamanho_max': 4.0, 'peso_min': 70, 'peso_max': 100, 'image_path': 'images/Deinonychus.png'},
            {'nome': 'Plateosaurus', 'tipo': 'Prosauropoda', 'dieta': 'Herbívoro', 'epoca': 'Triássico', 'descricao': 'Ancestral dos grandes sauropodes.', 'biomas': ['Planície'], 'tamanho_min': 8.0, 'tamanho_max': 10.0, 'peso_min': 1000, 'peso_max': 4000, 'image_path': 'images/Plateosaurus.png'},
            {'nome': 'Scelidosaurus', 'tipo': 'Thyreophora', 'dieta': 'Herbívoro', 'epoca': 'Jurássico', 'descricao': 'Um dos primeiros dinos blindados.', 'biomas': ['Floresta'], 'tamanho_min': 4.0, 'tamanho_max': 5.0, 'peso_min': 600, 'peso_max': 900, 'image_path': 'images/Scelidosaurus.png'},
            {'nome': 'Protoceratops', 'tipo': 'Marginocephalia', 'dieta': 'Herbívoro', 'epoca': 'Cretáceo', 'descricao': 'Pequeno com gola óssea.', 'biomas': ['Deserto', 'Planície'], 'tamanho_min': 1.0, 'tamanho_max': 2.0, 'peso_min': 180, 'peso_max': 240, 'image_path': 'images/Protoceratops.png'},
            {'nome': 'Argentinosaurus', 'tipo': 'Sauropoda', 'dieta': 'Herbívoro', 'epoca': 'Cretáceo', 'descricao': 'Possivelmente o maior de todos.', 'biomas': ['Planície'], 'tamanho_min': 30.0, 'tamanho_max': 35.0, 'peso_min': 60000, 'peso_max': 80000, 'image_path': 'images/Argentinosaurus.png'},
            {'nome': 'Psittacosaurus', 'tipo': 'Psittacosauridae', 'dieta': 'Herbívoro', 'epoca': 'Cretáceo', 'descricao': 'Um dos dinos mais comuns em fósseis.', 'biomas': ['Floresta'], 'tamanho_min': 1.0, 'tamanho_max': 2.0, 'peso_min': 20, 'peso_max': 25, 'image_path': 'images/Psittacosaurus.png'},
            {'nome': 'Maiasaura', 'tipo': 'Hadrosauridae', 'dieta': 'Herbívoro', 'epoca': 'Cretáceo', 'descricao': '"boa mãe" que cuidava filhotes.', 'biomas': ['Planície', 'Pantanal'], 'tamanho_min': 9.0, 'tamanho_max': 10.0, 'peso_min': 4000, 'peso_max': 6000, 'image_path': 'images/Maiasaura.png'},
            {'nome': 'Apatosaurus', 'tipo': 'Sauropoda', 'dieta': 'Herbívoro', 'epoca': 'Jurássico', 'descricao': 'Popular cerviz longo.', 'biomas': ['Planície'], 'tamanho_min': 21.0, 'tamanho_max': 23.0, 'peso_min': 15000, 'peso_max': 30000, 'image_path': 'images/Apatosaurus.png'},
        ]

        self.stdout.write('Criando exemplos de Post/Dino...')
        for data in exemplos:
            tipo_obj = DinoTipoDeDino.objects.get(nome=data['tipo'])
            dieta_obj = DinoDieta.objects.get(nome=data['dieta'])
            epoca_obj = DinoEpoca.objects.get(nome=data['epoca'])

            post, created = Post.objects.get_or_create(
                dinoNome=data['nome'],
                defaults={
                    'dinoTipo': tipo_obj,
                    'dinoDescricao': data['descricao'],
                    'dinoEpoca': epoca_obj,
                    'dinoDieta': dieta_obj,
                    'dinoTamanhoMin': data['tamanho_min'],
                    'dinoTamanhoMax': data['tamanho_max'],
                    'dinoPesoMin': data['peso_min'],
                    'dinoPesoMax': data['peso_max'],
                    'dinoImage': data['image_path'],
                }
            )

            for bnome in data['biomas']:
                bioma_obj = DinoBioma.objects.get(nome=bnome)
                post.biomas.add(bioma_obj)

            Dino.objects.get_or_create(
                nome=data['nome'],
                defaults={
                    'tipo': tipo_obj,
                    'dieta': dieta_obj,
                    'epoca': epoca_obj,
                    'descricao': data['descricao'],
                }
            )

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))
