from django.contrib import admin
from printer.models import Model, Printer, Part, PrinterCount


@admin.register(Model)
class AdminModel(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Printer)
class AdminPrinter(admin.ModelAdmin):
    list_display = ('name', 'serial', 'page_count_total', 'page_count_color', 'model',)
    search_fields = ('name', 'serial',)

@admin.register(PrinterCount)
class AdminPrinterCount(admin.ModelAdmin):
    list_display = ('date_getting', 'printer', 'page_count_total', 'page_count_color',)
    search_fields = ('printer',)


@admin.register(Part)
class AdminPart(admin.ModelAdmin):
    list_display = ('name', 'model', 'resource',)
    search_fields = ('name', 'model__name',)

