from datetime import datetime

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (MetaData, Integer, ForeignKey,
                        String, Column, DateTime,
                        Text, Float)
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

metadata = MetaData()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Author(Base):
    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(256))


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128))


class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(512))
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float(precision=2))
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id'))
    author: Mapped['Author'] = relationship('Author', cascade='all, delete-orphan', back_populates='books')
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category: Mapped['Category'] = relationship('Category', cascade='all, delete-orphan', back_populates='books')


class Cart(Base):
    __tablename__ = 'cart'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['Category'] = relationship('User', cascade='all, delete-orphan', back_populates='cart')
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'))
    book: Mapped['Category'] = relationship('Book', cascade='all, delete-orphan', back_populates='cart')


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['Category'] = relationship('User', cascade='all, delete-orphan', back_populates='orders')
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'))
    book: Mapped['Category'] = relationship('Book', cascade='all, delete-orphan', back_populates='orders')
