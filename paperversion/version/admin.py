# from django.contrib import admin
#
# from PaperlessVersion.settings import BASE_DIR
# from .models import PaperlessVersion
# import hashlib
# import qrcode
# import time
# import image
#
#
# # admin.site.register(PaperlessVersion)
#
#
# @admin.register(PaperlessVersion)
# class PaperlessVersionAdmin(admin.ModelAdmin):
#     list_display = ('name',
#                     'type',
#                     'version',
#                     'md5',
#                     'qr_code',
#                     'test_report',
#                     'content',
#                     'datetime_modified',
#                     )
#
#     # list_per_page设置每页显示多少条记录，默认是100条
#     list_per_page = 50
#
#     # ordering设置默认排序字段，负号表示降序排序
#     ordering = ('-type',
#                 '-datetime_modified',)
#
#     # list_editable = [
#     #                  'version']
#
#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)
#         with open(obj.file_path.path, 'rb') as fp:
#             f_md5 = hashlib.md5(fp.read()).hexdigest()
#             obj.md5 = f_md5
#         create_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
#         path1 = '192.168.230.137:8000' + '/files/' + str(obj.file_path)
#         path2 = 'files/img/' + create_time + '.png'
#         img = qrcode.make(path1)
#         with open(path2, 'wb') as fp:
#             img.save(fp)
#         obj.qr_code = '/img/' + create_time + '.png'
#         obj.save()

from django.contrib import admin

from .models import PaperlessVersion
import hashlib
import qrcode
import time

# admin.site.register(PaperlessVersion)


@admin.register(PaperlessVersion)
class PaperlessVersionAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'type',
                    'version',
                    'md5',
                    'content',
                    'datetime_modified',
                    )

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-type',
                '-version',)

    list_editable = [
                     'version']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        img_name = str(time.time()).split('.')[0] + str(time.time()).split('.')[1]

        # image = qrcode.make('http://127.0.0.1:8000/files/'+ str(obj.file_path))
        url = 'http://127.0.0.1:8000/files/' + str(obj.file_path)
        # url = 'http://192.168.0.126:8095/getapk/' + str(obj.file_path).split('/')[1]
        print(type(url))
        image = qrcode.make(url)
        with open('files/qr_code/' + str(img_name) + '.png', 'wb') as f:
            image.save(f)

        a = obj.file_path.path
        b = obj.file_path
        c = str(b)
        # print(type(b))


        with open(obj.file_path.path, 'rb') as fp:
            print(obj.file_path.path)
            f_md5 = hashlib.md5(fp.read()).hexdigest()
            obj.md5 = f_md5
            # print(type(obj.qr_code))
            # print(obj.qr_code)
            obj.qr_code = 'qr_code/' + str(img_name) + '.png'
            # obj.qr_code = 'getqrcode/' + str(img_name) + '.png'
            obj.save()


