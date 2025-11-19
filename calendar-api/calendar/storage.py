from typing import List
import model


class StorageException(Exception):
    pass


class LocalStorage:
    def __init__(self):
        self._id_counter = 0
        self._storage = {}
        self._date_index = {}  # Индекс для проверки уникальности дат

    def create(self, event: model.Event) -> str:
        # Проверяем уникальность даты
        if event.date in self._date_index:
            raise StorageException(f"Event already exists for date: {event.date}")

        self._id_counter += 1
        event.id = str(self._id_counter)
        self._storage[event.id] = event
        self._date_index[event.date] = event.id
        return event.id

    def list(self) -> List[model.Event]:
        return list(self._storage.values())

    def read(self, _id: str) -> model.Event:
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")
        return self._storage[_id]

    def update(self, _id: str, event: model.Event):
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")

        old_event = self._storage[_id]

        # Если дата изменилась, проверяем уникальность новой даты
        if old_event.date != event.date and event.date in self._date_index:
            raise StorageException(f"Event already exists for date: {event.date}")

        # Обновляем индексы
        if old_event.date in self._date_index:
            del self._date_index[old_event.date]
        self._date_index[event.date] = _id

        event.id = _id
        self._storage[event.id] = event

    def delete(self, _id: str):
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")

        event = self._storage[_id]
        if event.date in self._date_index:
            del self._date_index[event.date]
        del self._storage[_id]

    def get_by_date(self, date: str) -> model.Event:
        if date not in self._date_index:
            return None
        return self._storage[self._date_index[date]]