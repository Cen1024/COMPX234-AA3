import threading
import socket
import time

class Tuplespace:
    def __init__(self):
        self.tuples = {}
        self.lock = threading.Lock()
        self.key = self.tuples[0]
        self.value = self.tuples[1]
        self.numClient = 0
        self.numOperation = 0
        self.numRead = 0
        self.numGet = 0
        self.numPut = 0
        self.numErr = 0
    def READ(self,key):
         with self.lock:
             if key in self.tuples:
                 return self.value         
                 print("OK（", self.key,self.value, ")read")
             else:
                  print("ERR", self.key, "does not exist")
    def GET(self,key):
        with self.lock:
            if self.key == None:
                print("ERR", self.key, "does not exsits")
                self.value = None
                return self.value 
            else:
                del self.tuples
                print("OK(", self.key,self.value,")removed")
                return self.value            
            
    def PUT(self,key,value):
        with self.lock:
            if self.key == None:
                e = 0
                print("OK(", self.key, self.value, ")")
                return e            
            else:
                e = 1
                return e
    def start(self):
        with self.lock:
            num_tuples = len(self.tuples)
            total_key_size = sum(len(key) for key in self.tuples.keys())
            total_value_size = sum(len(value) for value in self.tuples.values())
            avg_tuple_size = (total_key_size + total_value_size) / num_tuples if num_tuples != 0 else 0
            avg_key_size = total_key_size / num_tuples if num_tuples != 0 else 0
            avg_value_size = total_value_size / num_tuples if num_tuples != 0 else 0
            return {
                'num_tuples': num_tuples,
                'avg_tuple_size': avg_tuple_size,
                'avg_key_size': avg_key_size,
                'avg_value_size': avg_value_size,
                'client_count': self.client_count,
                'total_operations': self.total_operations,
                'read_count': self.read_count,
                'get_count': self.get_count,
                'put_count': self.put_count,
                'error_count': self.error_count
            }



        
           
            
            
                
            
        

        
            