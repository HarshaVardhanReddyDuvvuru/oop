class Item:
    def __init__(self,name,price,category):
        if price<=0:
            raise ValueError(f'Invalid value for price, got {price}')
        self._price=price
        if not isinstance(name,str):
            raise ValueError('Invalid value for name')
        self._name=name
        if not isinstance(category,str):
            raise ValueError('Invalid value for category')
        self._category=category
        
    @property
    def price(self):
        return self._price
        
    @property
    def name(self):
        return self._name
        
    @property
    def category(self):
        return self._category
        
    def __str__(self):
        return f'{self._name}@{self._price}-{self._category}'
        
class Query:
    def __init__(self,field,operation,value):
        self._field=field
        ops=['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
        if operation not in ops:
            raise ValueError('Invalid value for operation, got random')
        self._operation=operation
        self._value=value
    
    @property
    def field(self):
        return self._field
        
    @property
    def operation(self):
        return self._operation
    
    @property
    def value(self):
        return self._value
        
    def __str__(self):
        return f'{self._field} {self._operation} {self._value}'
        
class Store:
    def __init__(self):
        self.store=[]
    
    def add_item(self,item):
        self.store.append(item)

    def __str__(self):
        if len(self.store)==0:
            return('No items')
        return '\n'.join(map(str,self.store))    
    
    @staticmethod
    def output(operation,operand1,operand2):
        if operation == "IN" or operation=="EQ":
            if not isinstance(operand2,list):
                operand2=[operand2]
            
            if operand1 in operand2:
                return True
                        
        elif operation=="STARTS_WITH" or operation=="ENDS_WITH" or operation=="CONTAINS" :
            if operand2 in operand1:
                return True
            
        elif operation=="LT" and operand1<operand2:
            return True
                    
        elif operation=="GT" and operand1>operand2:
            return True
                    
        elif operation=="LTE" and operand1<=operand2:
            return True
                    
        elif operation=="GTE" and operand1>=operand2:
            return True
                
    def filter(self,*argv):
        if len(argv)==1:
            for query in argv:
                filter_store=Store()
                for item in self.store:
                    if query.field=="category" and self.output(query._operation,item._category,query._value):
                        filter_store.add_item(item)
                                    
                    elif query.field=="price" and self.output(query._operation,item._price,query._value):
                        filter_store.add_item(item)
                                    
                    elif query.field=="name" and self.output(query._operation,item._name,query._value):
                        filter_store.add_item(item)
                        
                return filter_store
            
        else:
            values=[]
            for query in argv:
                filter='\n'.join(map(str,self.filter(query).store)).split('\n')
                values.append(set(filter))        
            
            and_operation_filter=Store()
            a=values[0]
            for item in values:
                a=a&item
                
            for item in a:
                and_operation_filter.add_item(item)
            
            return and_operation_filter
        
    def __add__(self,other):
        filter_1='\n'.join(map(str,self.store)).split('\n')
        filter_2='\n'.join(map(str,other.store)).split('\n')
        filter_1=set(filter_1)
        filter_2=set(filter_2)
        filter_3=Store()
        union=filter_1|filter_2
        union=sorted(union)
        for item in union:
            filter_3.add_item(item)
        
        return filter_3
                
    def exclude(self,*argv):
        if len(argv)==1:
            for query in argv:
                exclude_store=Store()
                for item in self.store:
                    if not item in self.filter(query).store:
                        exclude_store.add_item(item)
                    
                return exclude_store
            
        else:
            values=[]
            for query in argv:
                filter='\n'.join(map(str,self.exclude(query).store)).split('\n')
                values.append(set(filter))        
            
            and_operation=Store()
            a=values[0]
            for item in values:
                a=a&item
                
            for item in a:
                and_operation.add_item(item)
            
            return and_operation
        
    def count(self):
        return len(self.store)
      
      
