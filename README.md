# drf-library

* GET api/v1/books возвращает список книг
* GET api/v1/authors возвращает список авторов
* GET api/v1/books/top возвращает 10 книг с наивысшим rating
* GET api/v1/books/year?from=<year_from>&to=<year_to> возвращает книги опубликованные между year_from и year_to
* GET api/v1/authors/top возвращает 10 авторов опубликовавших наибольшее количество книг
* GET api/v1/genres возвращает список жанров и количество книг в каждом жанре
* GET api/v1/find_by_authors?q=<authors_names> возвращает книги авторов, имена которых
были переданы в параметре authors_names. Книги в ответе должны быть сгруппированы
по автору
* DELETE api/v1/books/{book_id} делает soft delete книги с id = book_id. Запись из базы данных
не удаляется, но все остальные API методы должны думать, что этой записи больше нет.
* DELETE api/v1/authors/{author_id} soft delete авторов по аналогии с книгами
