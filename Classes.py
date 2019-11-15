import pandas as pd
from dataclasses import dataclass
from decorators import open_close_connection

@dataclass
class Datos():

    path:str

    def read_data(self,sep=","):
        data = pd.read_csv(self.path, sep=sep)
        return data
    
    def unique_values(self,data,column):
        values = data[column].unique()    
        return values

    def get_values(self, dataframe, column):
        valid_columns = ['dia_semana', 'mes_cierre', 'delegacion_inicio']
        if column in valid_columns:
            agg_values = dataframe.gropby(column).agg({'folio':'count'})
            values = agg_values.to_dict()
        else:
            values = []
        return 

@dataclass
class ClaseMongo():

    JSON:str
    db_name:str
    column_name: str
    
    @open_close_connection
    def find(self,conn):
        response = list(conn.DBMongoTG.collection_prueba[self.db_name][self.column_name].find(self.JSON))        
        response = pd.DataFrame(response)
        return response
        
    @open_close_connection
    def insert(self,conn=None):
        conn.DBMongoTG.collection_prueba.insert(self.JSON)
    
    @open_close_connection
    def update(self,JSET, conn=None):
        conn.DBMongoTG.collection_prueba.update(self.JSON,{"$set":JSET})
