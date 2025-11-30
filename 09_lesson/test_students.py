import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URI = "postgresql://myuser:mypassword@localhost:5432/mydatabase"
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()


@pytest.mark.usefixtures("session")
def test_add_student(session):
    from models import Student  # Импортируем модель студента

    # Создаем нового студента
    new_student = Student(full_name="Иванов Петр")
    session.add(new_student)
    session.commit()

    # Проверяем, что студент появился в базе
    added_student = session.query(Student).filter_by(full_name="Иванов Петр").first()
    assert added_student is not None
    assert added_student.full_name == "Иванов Петр"

    # Удаляем студента из базы после теста
    session.delete(added_student)
    session.commit()


def test_update_student(session):
    from models import Student

    # Получаем первого студента
    existing_student = session.query(Student).first()
    old_full_name = existing_student.full_name

    # Меняем ФИО
    existing_student.full_name = "Смирнов Василий"
    session.commit()

    # Проверяем, что данные изменились
    updated_student = session.query(Student).filter_by(student_id=existing_student.student_id).first()
    assert updated_student.full_name != old_full_name
    assert updated_student.full_name == "Смирнов Василий"

    # Возвращаем обратно старое значение
    updated_student.full_name = old_full_name
    session.commit()


def test_soft_delete_student(session):
    from models import Student

    # Берём первого студента
    target_student = session.query(Student).first()

    # Моделируем мягкий DELETE (добавляем timestamp в поле deleted_at)
    target_student.deleted_at = datetime.now()
    session.commit()

    # Проверяем, что запись стала "удалённой"
    deleted_student = session.query(Student).filter_by(student_id=target_student.student_id).first()
    assert deleted_student.deleted_at is not None

    # Восстанавливаем студента
    deleted_student.deleted_at = None
    session.commit()


