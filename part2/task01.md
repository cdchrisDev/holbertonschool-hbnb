# What are the steps involved in this web application ?
1. instante the Flask App Object on `app.__init__`
    * By doing `Flask(__name__)` this tells flask that we are going to use the app as the __name__ special method set. But, we can also create a function to actually make our app be born
    * app instante from `Flask` Module
    * api instante a class called `Api` from `flask_restx` which takes as the first argument the `Flask` instance and the rest of the arguments are meta 
```
app = Flask(__name__)
api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')
```
2. For now, database will be `Repository` so we'll need a few functions to deal with storage management, but first where is our storage? we're gonna set it by default doing `def __init__(self): self._storage = {}`
    * Using abstract classes we set up the basic functionality like an empty function with the arguments that will use that specific function, for example `def update(self, obj_id, data)`
    * Then we create a storage handler class that will inheret all the op-func made in the `repository` abstract class: `InMemoryRepository(Repository)` this class will implement those functions to work as intended. For example:
```
def delete(self, obj_id):
    if obj in self._storage:
        del self._storage[obj_id]
```
3. Now, to implement good facade pattern we import our "database handler" into a file which serve
as individual entity management
```python
class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
```
4. We instante the Facade class
```python
from app.services.facade import HBnBFacade

facade = HBnBFacade()
```
5. set the script to run the entire app in `run.py` on root
```python
from app import create_app

app = create_app() #it does not truncate variables because there not in the same scope

if __name__ == '__main__':
    app.run(debug=True)
```
6. Basic config
```py
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
```