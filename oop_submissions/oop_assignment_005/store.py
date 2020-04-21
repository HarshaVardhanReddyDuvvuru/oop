class Item:
    def __init__(self,name,price,category):
        if price==0:
            raise ValueError('Invalid value for price, got 0')
        elif price<0:
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
        self._ops=['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
        if operation not in self._ops:
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
    
    sub_store=[]
    
    def __init__(self):
        self.store=[]
    
    def add_item(self,item):
        self.store.append(item)

        
    def __str__(self):
        things='\n'.join(map(str,self.store))
        if len(things)==0:
            return('No items')
        return things
        
    def filter(self,query):
        filter_store=Store()
        self._result=[]
        for item in self.store:
            if query._field=="category":
                if query._operation=="IN":
                    for value in query._value:
                        if item._category==value:
                            self._result.append(item)
                            
                elif query._operation=="EQ":
                    if item._category==query._value:
                        self._result.append(item)
                
                elif query._operation=="STARTS_WITH":
                    if item._category.startswith(query._value):
                        self._result.append(item)
                        
                elif query._operation=="ENDS_WITH":
                    if item._category.endswith(query._value):
                        self._result.append(item)
                        
                elif query._operation=="CONTAINS":
                    if query._value in item._category:
                        self._result.append(item)
                
            elif query._field=="price":
                if query._operation=="LT":
                    if item._price<query._value:
                        self._result.append(item)
                elif query._operation=="GT":
                    if item._price>query._value:
                        self._result.append(item)
                elif query._operation=="LTE":
                    if item._price<=query._value:
                        self._result.append(item)
                elif query._operation=="GTE":
                    if item._price>=query._value:
                        self._result.append(item)
                        
                elif query._operation=="EQ":
                    if item._price==query._value:
                        self._result.append(item)
                
                elif query._operation=="IN":
                    for value in query._value:
                        if item._price==value:
                            self._result.append(item)
                
                    
            elif query._field=="name":
                if query._operation=="IN":
                    for value in query._value:
                        if item._name==value:
                            self._result.append(item)
                            
                elif query._operation=="STARTS_WITH":
                    if item._name.startswith(query._value):
                        self._result.append(item)
                        
                elif query._operation=="ENDS_WITH":
                    if item._name.endswith(query._value):
                        self._result.append(item)
                        
                elif query._operation=="EQ":
                    if item._name==query._value:
                        self._result.append(item)
                        
                elif query._operation=="CONTAINS":
                    if query._value in item._name:
                        self._result.append(item)
                    
        for i in range(len(self._result)):
            filter_store.add_item(self._result[i])
            
        things='\n'.join(map(str,self._result))
        self.sub_store=things.split('\n')
            
        return filter_store

    def exclude(self,query):
        exclude_store=Store()
        self.filter(query)
        things='\n'.join(map(str,self.store))
        total_store=things.split('\n')
        for item in total_store:
            if not item in self.sub_store:
                exclude_store.add_item(item)
                
        return exclude_store
        
    def count(self):
        return len(self.store)
    