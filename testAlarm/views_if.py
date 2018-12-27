from testAlarm.models import Image
from django.core.exceptions import ValidationError
import gzip, base64, os
import xml.etree.ElementTree as ET


def add_Alarm(request):
    resp = request.FILES.get()
    data = gzip.decompress(resp).decode("utf-8")

    alarmData = ET.parse(data)

    timeStr = alarmData.find('.//time').text
    # createTime = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(timeStr)))

    # 获取图片视频信息至本地缓冲区
    pictTag = alarmData.find('.//media')
    pictName = pictTag.get('name')

    # 定义运行时数据缓冲区
    runtimeDir = os.path.join(os.pardir, 'runtimeData')
    pictFile = os.path.join(runtimeDir, pictName)
    with open(pictFile, 'wb') as file:
        # 取出picture的base64加密数据
        b64PictData = pictTag.text
        pictData = base64.decodebytes(b64PictData)
        file.write(pictData)

    # 获取速度信息
    speedTag = alarmData.getroot().find('.//speed')

