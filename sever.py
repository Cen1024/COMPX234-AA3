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


def handle_client(client_socket, tuple_space):
    
    try:
        while True:
            request = client_socket.recv(1024).decode('utf-8')
            if not request:
                break

            # Parse the request
            msg_len = int(request[:3])
            cmd = request[3]
            key = request[4:].split()[0]
            value = ' '.join(request[4:].split()[1:]) if len(request[4:].split()) > 1 else None

            tuple_space.total_operations += 1
            response = ''

            if cmd == 'R':
                tuple_space.read_count += 1
                result, err = tuple_space.read(key)
                if err == 0:
                    response = f"OK ({key}, {result}) read"
                else:
                    response = f"ERR {key} does not exist"
                    tuple_space.error_count += 1
            elif cmd == 'G':
                tuple_space.get_count += 1
                result, err = tuple_space.get(key)
                if err == 0:
                    response = f"OK ({key}, {result}) removed"
                else:
                    response = f"ERR {key} does not exist"
                    tuple_space.error_count += 1
            elif cmd == 'P':
                tuple_space.put_count += 1
                err = tuple_space.put(key, value)
                if err == 0:
                    response = f"OK ({key}, {value}) added"
                else:
                    response = f"ERR {key} already exists"
                    tuple_space.error_count += 1
            else:
                response = "Invalid command"
                tuple_space.error_count += 1

            # Send the response
            client_socket.sendall(response.encode('utf-8'))

    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        tuple_space.client_count -= 1
        client_socket.close()



        
           
            
            
                
            
        

        
            