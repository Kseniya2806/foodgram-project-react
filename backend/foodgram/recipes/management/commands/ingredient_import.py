import csv

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загрузка данных из списка в формате CSV в базу данных.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', help='foodgram.data.ingridients.csv')

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        try:
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file, delimiter=',')
                for row in reader:
                    your_model_instance = Ingredient(
                        name=row['name'],
                        measurement_unit=row['measurement_unit'],
                    )
                    your_model_instance.save()

                self.stdout.write(self.style.SUCCESS(
                    'Данные успешно загружены в базу данных.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Произошла ошибка: {str(e)}'))
