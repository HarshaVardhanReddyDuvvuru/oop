class Item:
    def __init__(self,name,price,category):
        if price==0:
            raise ValueError('Invalid value for price, got 0')
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
    
    store=[]
        
    def add_item(self,item):
        self.store.append(item)
        
    def __str__(self):
        things='\n'.join(map(str,self.store))
        return things
        
    def filter(self,query):
        filtered_store=Store()
        
        for item in self.store:
            if query.operation=="IN":
                if query.field=="category":
                    if query.value==item.category:
                        filtered_store.add_item(item)
                        
                if query.field=="price":
                    if query.value==item.price:
                        filtered_store.add_item(item)
                
                if query.field=="category":
                    if query.value==item.category:
                        filtered_store.add_item(item)
                
                                
                
            '''elif query._field=="price":
                if query._operation=="LT":
                    if item._price<query._value:
                        filtered_store.add_item(item)
                elif query._operation=="GT":
                    if item._price>query._value:
                        filtered_store.add_item(item)
                elif query._operation=="LTE":
                    if item._price<=query._value:
                        filtered_store.add_item(item)
                elif query._operation=="GTE":
                    if item._price>=query._value:
                        filtered_store.add_item(item)
                        
                elif query._operation=="EQ":
                    if item._price==query._value:
                        filtered_store.add_item(item)
                    
            elif query._field=="name":
                if query._operation=="IN":
                    for value in query._value:
                        if item._name==value:
                            filtered_store.add_item(item)
                            
                elif query._operation=="STARTS_WITH":
                    if item._name.startswith(query._value):
                        filtered_store.add_item(item)
                        
                elif query._operation=="ENDS_WITH":
                    if item._name.endswith(query._value):
                        filtered_store.add_item(item)
                        
                elif query._operation=="EQ":
                    if item._name==query._value:
                        filtered_store.add_item(item)'''
                    
        return filtered_store
        
        
        
        
        
        
store = Store()  
item = Item(name="Oreo Biscuits", price=30, category="Food")  
store.add_item(item)  
item = Item(name="Boost Biscuits", price=20, category="Food")  
store.add_item(item)  
item = Item(name="Butter", price=10, category="Grocery")  
store.add_item(item)
query = Query(field="category", operation="EQ", value=["Food"])  
results = store.filter(query) 
print(type(results))
print(results)  