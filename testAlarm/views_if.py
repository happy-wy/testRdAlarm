from testAlarm.models import FileGz
from django.core.exceptions import ValidationError
import gzip, base64, os
import xml.etree.ElementTree as ET
from django.http import HttpResponse


def add_Alarm(request):
    myFile = request.body()
    print("myfile success")
    if not myFile:
        return HttpResponse("no files for upload!")

    # myFile = FileGz()
    # myFile.save()

    destination = open(os.path.join("file/", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
    for chunk in myFile.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()

    return HttpResponse({'status': 200, 'message': 'add alarm success'})
