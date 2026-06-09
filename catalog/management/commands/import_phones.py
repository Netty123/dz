import csv
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from catalog.models import Phone

class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for row in reader:
                phone, created = Phone.objects.update_or_create(
                    id=int(row['id']),
                    defaults={
                        'name': row['name'],
                        'slug': slugify(row['name']),
                        'image': row['image'],
                        'price': float(row['price']),
                        'release_date': row['release_date'],
                        'lte_exists': row['lte_exists'].lower() == 'true',
                    }
                )
                
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Added: {phone.name}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Updated: {phone.name}'))
        
        self.stdout.write(self.style.SUCCESS('Import completed!'))