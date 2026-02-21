class cola_circular():
    def __init__(self):
        self.data_queue = [0] * 10 
        self.queue_pointer = 0 
        
        
    def enqueue(self): 
        if self.queue_pointer < 10:
            