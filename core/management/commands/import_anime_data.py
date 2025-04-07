import csv
from django.core.management.base import BaseCommand
from core.models import Anime

class Command(BaseCommand):
    help = 'Import anime data from a CSV file'

    def handle(self, *args, **kwargs):
        file_path = '/Users/rehmatgrewal/Desktop/anime/db_data/AnimeList.csv'  # Replace with your actual file path
        batch_size = 500  # Insert data in batches to prevent memory overload

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            anime_data = []

            for row in reader:
                # Parsing data from CSV and adding to the list
                anime_data.append(
                    Anime(
                        anime_id=row['anime_id'],
                        title=row['title'],
                        title_english=row['title_english'],
                        title_japanese=row['title_japanese'],
                        title_synonyms=row['title_synonyms'],
                        image_url=row['image_url'],
                        type=row['type'],
                        source=row['source'],
                        episodes=int(row['episodes']) if row['episodes'] else None,
                        status=row['status'],
                        airing=row['airing'] == 'True',  # Convert from string to boolean
                        aired_string=row['aired_string'],
                        aired=row['aired'],  # Assuming aired is a JSON field
                        duration=row['duration'],
                        rating=row['rating'],
                        score=float(row['score']) if row['score'] else None,
                        scored_by=int(row['scored_by']) if row['scored_by'] else None,
                        rank=int(row['rank']) if row['rank'] else None,
                        popularity=int(row['popularity']) if row['popularity'] else None,
                        members=int(row['members']) if row['members'] else None,
                        favorites=int(row['favorites']) if row['favorites'] else None,
                        background=row['background'],
                        premiered=row['premiered'],
                        broadcast=row['broadcast'],
                        related=row['related'],  # Assuming related is a JSON field
                        producer=row['producer'],
                        licensor=row['licensor'],
                        studio=row['studio'],
                        genre=row['genre'],
                        opening_theme=row['opening_theme'],
                        ending_theme=row['ending_theme']
                    )
                )

                # Insert data in batches
                if len(anime_data) >= batch_size:
                    Anime.objects.bulk_create(anime_data)
                    anime_data.clear()  # Reset the list for the next batch

            # Insert remaining data if any
            if anime_data:
                Anime.objects.bulk_create(anime_data)

            self.stdout.write(self.style.SUCCESS('Successfully imported anime data'))