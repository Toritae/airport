Archetecture
===

#### APIs
+ Question1 Search form
  + GET /question1/ 
+ Question1 Search Result
  + GET /question1/search?iata={iata_code}
+ Question2 Search form
  + GET /question2/
+ Question2 Search result(ListView)
  + GET /question2/?search_tag={search_tag}&search_keyword={search_keyword}
  + search tag = [ 'iata' , 'name' , 'city' ]
#### Runbook
1. pip install -r requirements.txt
2. cd this folder, current directory location
3. python manage.py migrate
4. python manage.py runserver
5. localhost:8000/setup
