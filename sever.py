import threading
import socket

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