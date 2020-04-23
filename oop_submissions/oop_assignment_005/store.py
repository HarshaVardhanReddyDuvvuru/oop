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
        things='\n'.join(map(str,self.store))
        if len(things)==0:
            return('No items')
        return things
    
    @staticmethod
    def output(operation,operand1,operand2):
        from operator import lt,gt,le,ge
        operation_dict={"LT":lt,"LTE":le,"GT":gt,"GTE":ge}
        
        if operation == "IN" or operation=="EQ":
            if not isinstance(operand2,list):
                operand2=[operand2]
            
            if operand1 in operand2:
                return True
                        
        elif operation=="STARTS_WITH" or operation=="ENDS_WITH" or operation=="CONTAINS" :
            if operand2 in operand1:
                return True
        else:
            if operation_dict[operation](operand1,operand2):
                return True
                
    def filter(self,query):
        filter_store=Store()
        for item in self.store:
            if query.field=="category" and self.output(query._operation,item._category,query._value):
                    filter_store.add_item(item)
                            
            elif query.field=="price" and self.output(query._operation,item._price,query._value):
                    filter_store.add_item(item)
                            
            elif query.field=="name" and self.output(query._operation,item._name,query._value):
                    filter_store.add_item(item)
                    
        return filter_store
                
    def exclude(self,query):
        exclude_store=Store()
        for item in self.store:
            if not item in self.filter(query).store:
                exclude_store.add_item(item)
            
        return exclude_store
        
    def count(self):
        return len(self.store)