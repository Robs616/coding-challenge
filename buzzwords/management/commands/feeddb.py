from django.core.management.base import BaseCommand
from buzzwords.models import Buzzword, BuzzwordCategory
import csv

#feed the database from  csv in buzzwords/data
class Command(BaseCommand):
    help = 'Feed the database from csv datasource'

    def handle(self, *args, **options):
            try:
                #feed table buzzword_category
                with open("buzzwords/data/buzzwordcategory.csv") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        obj_buzzword_category, created = BuzzwordCategory.objects.get_or_create(
                		name=row[0].strip(),
						)

                        try:
                            #feed table buzzword with category
                            with open("buzzwords/data/buzzword_{}.csv".format(obj_buzzword_category).lower().replace(" ", "_")) as k:
                                reader = csv.reader(k)
                                for row in reader:
                                    split_name = row[0].split("-",1)
                                    if len(split_name) >= 2:
                                        x_name = split_name[0]
                                        x_description = split_name[1]
                                    else:
                                        x_name = split_name[0]
                                        x_description = ''

                                    obj_buzzword, created = Buzzword.objects.get_or_create(
									
                			        name=x_name.strip(),
							        description =  x_description.strip(),
							        category = obj_buzzword_category
                			        )
                        except IOError:
                            #raise CommandError(e)
                            print("file is missing: {}.csv".format(obj_buzzword_category).lower());
           
            except IOError:
                print("file is missing: buzzwordcategory.csv");
                #raise CommandError(e)
            self.stdout.write(self.style.SUCCESS('Successfully added data'))