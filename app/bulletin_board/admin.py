from django.contrib import admin

from bulletin_board.models import (Ad, Category, CitiesDirectory, CustomUser,
                                   RegionDirectory)

admin.site.register(CustomUser)
admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(CitiesDirectory)
admin.site.register(RegionDirectory)
