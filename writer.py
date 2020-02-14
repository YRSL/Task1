from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as xml

class Writer(ABC):

    @abstractmethod
    def write(self, *args):
        pass


class JSON_Writer(Writer):

    @staticmethod
    def write(list_objects):
        data_result = [i.to_dict() for i in list_objects]
        with open("result.json", 'w', encoding='UTF-8') as file:
            json.dump(data_result, file, ensure_ascii=False)


class XML_Writer(Writer):

    @staticmethod
    def write(root):
        tree = xml.ElementTree(root)
        with open("result.xml", 'wb') as f:
            tree.write(f, encoding="utf-8")
