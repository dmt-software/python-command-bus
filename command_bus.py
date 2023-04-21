from abc import ABC, abstractmethod
from typing import Dict, List

class Middleware(ABC):
    @abstractmethod
    def execute(self, command, next = None):
        pass

class CommandHandler(ABC):
    @abstractmethod
    def handle(self, command):
        pass

class CommandBus:
    def __init__(self, middlewares: List[Middleware]):
        self.middlewares = middlewares

    def handle(self, command = None):
        middlewares = self.middlewares.copy()
        middlewares.reverse()

        def call(middleware, next = None):
            return lambda command: middleware.execute(command, next)

        next = None
        for middleware in middlewares:
            next = call(middleware, next)

        return next(command)

class HandlerMiddleware(Middleware):
    def __init__(self, commandToHandlerMapping: Dict[str, CommandHandler]):
        self.commandToHandlerMapping = commandToHandlerMapping

    def execute(self, command, next):
        className = command.__class__.__name__
        if not self.commandToHandlerMapping.get(className):
            raise Exception('No handler for ' + className)

        handler = self.commandToHandlerMapping.get(className)
        return handler.handle(command)

