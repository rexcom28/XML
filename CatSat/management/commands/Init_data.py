import csv
import os
from queue import Queue
from threading import Thread
from django.core.management.base import BaseCommand, CommandError
from Reader_XML.settings import BASE_DIR
from django.apps import apps




class Command(BaseCommand):

    help ="a ver a ver"

    NUM_THREADS = 0 
    list_csv = []
    len_list = 0
    q = Queue()
    flag: bool

    def delete_model(self, table_name):
        model = apps.get_model('CatSat', table_name)
        if self.flag:
            model.objects.all().delete()

    def Add_Data_Models(self, table_name=None, row_to_insert= dict):
        model = apps.get_model('CatSat', table_name)
        keyVal= list(row_to_insert.items())[0]
        keyVal ={ keyVal[0]:keyVal[1]}
        
        obj,created = model.objects.get_or_create(**keyVal, defaults=row_to_insert)
        if created:
            print(f'El {keyVal} con valor {keyVal}  se a creado correctamente')
        else:
            print(f'error: {keyVal}')


    def csv_queue(self, pat,t):
        global q
        while True:
            proc_list = self.q.get()
            #print(pat/proc_list ,f'     {t}', proc_list)
            with open (pat/proc_list, 'r') as f:
                    reader = csv.DictReader(f, delimiter=',',dialect="excel")
                    next(reader, None)                    
                    for row in reader:
                        if '' not in row.values():
                            self.Add_Data_Models(proc_list.split('.')[0], row)
            print(f'end print {proc_list}')
            self.q.task_done()

    def  add_arguments(self, parser):
        parser.add_argument('-p', '--path_csv', type=str, help='indicate the path of CSV files', )
        parser.add_argument('-rd', '--replace_data', type=bool, help='if true all data in model will be remove before insertion csv.')

    def handle(self, *args, **kwargs ):
        res =kwargs['path_csv']
        self.flag = kwargs['replace_data']

        if not res :        
            #raise CommandError("naaaaaaaaaaaa te equivocastessssssssssssss!") 
            self.stdout.write('No se agrego la ruta de los archivos se tomara de la ruta default. Se usara {res}'.format(res=BASE_DIR / 'CSV'))
            res = BASE_DIR / 'CSV'    
        if os.path.exists(res):
            #print('res', os.path.exists(res))    
            list_csv = os.listdir(BASE_DIR/ 'CSV') 
            #print(list_csv) 
            for lis in list_csv:                
                self.q.put(lis)
                print(lis)

            for t in range(len(list_csv)):
                
                worker = Thread(target=self.csv_queue, args=(res,t))
                worker.daemon = True
                worker.start()
            self.q.join()

            

