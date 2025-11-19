from typing import List
import model
import db
import re

TITLE_LIMIT = 30
TEXT_LIMIT = 200


class LogicException(Exception):
    pass


class EventLogic:
    def __init__(self):
        self._event_db = db.EventDB()

    @staticmethod
    def _validate_date(date: str):
        # Проверяем формат даты ГГГГ-ММ-ДД
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
            raise LogicException("invalid date format, expected: YYYY-MM-DD")

        # Проверяем валидность даты
        try:
            year, month, day = map(int, date.split('-'))
            if month < 1 or month > 12 or day < 1 or day > 31:
                raise ValueError
        except ValueError:
            raise LogicException("invalid date")

    @staticmethod
    def _validate_event(event: model.Event):
        if event is None:
            raise LogicException("event is None")

        if event.date is None:
            raise LogicException("date is required")
        EventLogic._validate_date(event.date)

        if event.title is None or len(event.title) > TITLE_LIMIT:
            raise LogicException(f"title length > MAX: {TITLE_LIMIT}")

        if event.text is None or len(event.text) > TEXT_LIMIT:
            raise LogicException(f"text length > MAX: {TEXT_LIMIT}")

    def create(self, event: model.Event) -> str:
        self._validate_event(event)
        try:
            return self._event_db.create(event)
        except Exception as ex:
            raise LogicException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[model.Event]:
        try:
            return self._event_db.list()
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> model.Event:
        try:
            return self._event_db.read(_id)
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, _id: str, event: model.Event):
        self._validate_event(event)
        try:
            return self._event_db.update(_id, event)
        except Exception as ex:
            raise LogicException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._event_db.delete(_id)
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")

    def get_by_date(self, date: str) -> model.Event:
        self._validate_date(date)
        try:
            return self._event_db.get_by_date(date)
        except Exception as ex:
            raise LogicException(f"failed GET_BY_DATE operation with: {ex}")