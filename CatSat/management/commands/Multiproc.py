

import time
import os
import csv
import asyncio
import queue
import threading


from asgiref.sync import sync_to_async
from django.core.management.base import BaseCommand, CommandError
from Reader_XML.settings import BASE_DIR
from django.apps import apps

class Command(BaseCommand):
    help = 'Multi processing csv'
    list_csv: list
    q = queue.Queue()
    lock = threading.RLock()
    
    


    def  add_arguments(self, parser):
        parser.add_argument('-p', '--path_csv', type=str, help='indicate the path of CSV files', )

    def handle(self, *args, **kwargs ):
        res =kwargs['path_csv']
        if not res:
            self.stdout.write('No se agrego la ruta de los archivos se tomara de la ruta default. Se usara {res}'.format(res=BASE_DIR / 'CSV'))
            res = BASE_DIR / 'CSV'
        if os.path.exists(res):
            self.list_csv = os.listdir(BASE_DIR/'CSV')
        def get_(path:str, model_name:str):
            lis = []
            
            with open(path) as f:
                reader = csv.DictReader(f, delimiter=',',dialect="excel")
                next(reader, None)
                for row in reader:
                    row['model']=model_name
                    lis.append(row)                                
            yield lis

        processed_list: list=[]
        async def read_csv():
            start_time = time.perf_counter()
            ten =  [ await sync_to_async(get_, thread_sensitive=True)(res/x[1], x[1].split('.')[0] ) for x in enumerate(self.list_csv)]
            processed_list.append([next(t) for t in ten])
            finish_time = time.perf_counter()
            print(f"proccessed list finished: {finish_time-start_time} seconds")
            
        asyncio.run(read_csv())        
        self.main(processed_list)
    """ handle method ends"""



    def add_todb(self,dic:dict):
        m = dic.pop('model')
        
        model = apps.get_model('CatSat', m)
        keyVal= list(dic.items())[0]
        print(keyVal)
        keyVal ={ keyVal[0]:keyVal[1]}
        
        obj,created = model.objects.get_or_create(**keyVal, defaults=dic)
        if created:
            print(f'El {keyVal} con valor {keyVal}  se a creado correctamente')
        else:
            print(f'error: {keyVal}')
        

    def main(self, listA: list):
        start_time = time.perf_counter()
        """ outer for(listA) first and then inner for(lis) to the rigth,
        the result arg in this case 'l' goes first 
        """
        
        
        lis = [ll for lis in listA for l in lis for ll in lis ]
        
        for li in lis:            
            for l in li:
                self.add_todb(l)
                
        finish_time = time.perf_counter()
        print(f"proccessed insert: {finish_time-start_time} seconds")





        
        