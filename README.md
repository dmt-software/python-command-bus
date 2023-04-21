# Python CommandBus  

A simple commandBus for python3. 

## Usage

### Configure

Set up the command bus with all the command handlers.
The `HandlerMiddleware` maps the class name of a `Command` to the handler that handles it.

```python3
# file: setup.py

from command_bus import CommandBus, CommandHandler, HandlerMiddleware

class CarHandler(CommandHandler):
    def handle(self, car):
        # process the Car
        
class BikeHandler(CommandHandler):
    def handle(self, bike):
        # process the bike

command_bus = CommandBus([
    HandlerMiddleware({
        'Car': CarHandler(),
        'Bike': BikeHandler(),
    })
])
```

### Execute

To execute a `Command`, instantiate one and give it to the `CommandBus` to process it. 

```python3
from setup import command_bus

class Bike():
    def __init__(self, gears):
        self.gears = gears
        
command_bus.handle(Bike(21)) # BikeHandler is executed using Bike 
```

## Middleware

You can easily add extra functionalities that needs to be executed on some or all of the commands passed. 
Just create some `Middleware` and add it to the `CommandBus`

```python3
from command_bus import CommandBus, CommandHandler, HandlerMiddleware

class LoggingMiddleware(Middleware):
    def execute(self, command, next):
        print(command.__class__.__name__)
        return next(command)
        
command_bus = CommandBus([
    LoggingMiddleware(),
    HandlerMiddleware({})
])
```