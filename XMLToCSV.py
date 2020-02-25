import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            try:
                value = (root.find('filename').text,
                         int(root.find('size')[0].text),
                         int(root.find('size')[1].text),
                         member[0].text,
                         int(member[4][0].text),
                         int(member[4][1].text),
                         int(member[4][2].text),
                         int(member[4][3].text)
                         )
                xml_list.append(value)
            except:
                continue
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    image_path = 'E:\\迅雷下载\\VOCtrainval_06-Nov-2007\\VOCdevkit\\VOC2007\\Annotations'#XML文件的位置
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv('E:\\迅雷下载\\VOCtrainval_06-Nov-2007\\VOCdevkit\\VOC2007\\Annotations.csv', index=None)#输出位置及输出的文件名
    print('Successfully converted xml to csv.')


main()