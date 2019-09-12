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
        #self.gen_prcount()
        #self.gen_part()
        self.select()


    def select(self):
        self.stdout.write('Select result')
        printer_list = Printer.objects.all()
        for row in printer_list:
            res = '{name}: {pg}'.format(
                name=row.name,
                pg=row.page_count_total
            )
            self.stdout.write(res)

    def gen_part(self):
        self.stdout.write("generations Part")
        for i in range(1, 60):
            part = Part(
                name='Запчасть {}'.format(i),
                model_id=random.choice((1, 2, 3,)),
                resource=random.choice((150, 270, 300, 1500, 10000,))
            )
            part.save()

    def gen_prcount(self):
        self.stdout.write("generations PrinterCount")
        today = date.today()
        for i in range(1, 60):
            date_getting = today - timedelta(days=i)
            # print('\t', date_getting)
            for pid in range(1, 10):
                pc = PrinterCount(
                    date_getting=date_getting,
                    printer_id=pid,
                    page_count_total=random.choice(range(1,20))+(i*100)
                )
                pc.save()

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



