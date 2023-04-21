from command_bus import CommandBus, Middleware, CommandHandler, HandlerMiddleware

class LoggingMiddleware(Middleware):
    def execute(self, command, next):
        print(command.__class__.__name__)
        return next(command)

class CarHandler(CommandHandler):
    def handle(self, car):
        return ' - ' + car.make + ' ' + car.model

class BikeHandler(CommandHandler):
    def handle(self, bike):
        return ' - ' + str(bike.gears) + ' gears'

command_bus = CommandBus([
    LoggingMiddleware(),
    HandlerMiddleware({
        'Car': CarHandler(),
        'Bike': BikeHandler(),
    })
])
