# Паттерн проектирования - Observer

from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Subject(ABC):
    """
    Интерфейс для наблюдателя
    """

    @abstractmethod
    def attach(self, observer):
        """
        Добавляет нового подписчика
        """
        pass

    @abstractmethod
    def detach(self, observer):
        """
        Удаляет подписчика
        """
        pass

    @abstractmethod
    def notify(self):
        pass


class ConcreteSubject(Subject):

    _state: int = None

    _observers: List = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self):
        self._state = randrange(0, 10)

        self.notify()


class Observer(ABC):

    @abstractmethod
    def update(self, subject):
        pass


class ConcreteObserverA(Observer):

    def update(self, subject):
        if subject._state < 3:
            print('Событие для конкретного подписчика А')


class ConcreteObserverB(Observer):

    def update(self, subject):
        if subject._state == 0 or subject._state >= 3:
            print('Событие для конкретного подписчика B')


subject = ConcreteSubject()

observer_a = ConcreteObserverA()
subject.attach(observer_a)

observer_b = ConcreteObserverB()
subject.attach(observer_b)

subject.some_business_logic()
print(subject._state)
