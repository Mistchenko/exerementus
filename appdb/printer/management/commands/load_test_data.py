import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from printer.models import Model, Printer, Part, PrinterCount


class Command(BaseCommand):
    help = 'Загрузка данных в базу с помощью генератора'

    def handle(self, *args, **kwargs):
        self.stdout.write("Start ")
        # self.gen_models()
        #self.gen_printers()
        self.gen_prcount()

    def gen_prcount(self):
        self.stdout.write("generations PrinterCount")


    def gen_printers(self):
        self.stdout.write("generations printers")
        for p in range(1, 10):
            printer = Printer(
                serial='A000{}000'.format(p),
                name='Printer {}'.format(p),
                page_count_total=6,
                page_count_color=0,
                model_id=random.choice((1, 2, 3,))
            )
            printer.save()
            self.stdout.write("new printer {}".format(p))

    def gen_models(self):
        self.stdout.write("generations models")
        for m in ['HP', 'Canon', 'Xerox']:
            model, new = Model.objects.get_or_create(name=m)
            if new:
                model.save()
                self.stdout.write("new model {}".format(m))



