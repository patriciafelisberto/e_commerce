SISTEMA DE E-COMMERCE COM DJANGO REST_FRAMEWORK

1 - clone o repositório;

2 - docker-compose up --build -d #Starta e roda os serviços definidos no "docker-compose.yml";

3 - docker-compose run web python manage.py makemigrations #Prepara as migrações dentro do ambiente docker;

4 - docker-compose run web python manage.py migrate #Efetua as migrações dentro do ambiente docker;

5 - docker-compose run web python manage.py runserver #Starta a aplicação mercadinho;

6 - acesse o site localhost:8000/admin #Acessar o Admin do Django e verificar o ambiente criado do back; 

7 - Para usar o sistema de testes - "docker-compose run web python manage.py test mercadinho.tests.MyTestCase" - "MyTestCase - Classe criada como exemplo para testar os models";

Obrigada e espero que tenha curtido o projeto!



E-COMMERCE SYSTEM WITH DJANGO REST_FRAMEWORK

1 - clone the repository;

2 - docker-compose up --build -d #Start and run the services defined in "docker-compose.yml";

3 - docker-compose run web python manage.py makemigrations #Prepare migrations within the docker environment;

4 - docker-compose run web python manage.py migrate #Perform migrations within the docker environment;

5 - docker-compose run web python manage.py runserver #Start the grocery store application;

6 - access the site localhost:8000/admin #Access the Django Admin and check the environment created in the back;

7 - To use the test system - "docker-compose run web python manage.py test mercadinho.tests.MyTestCase" - "MyTestCase - Class created as an example to test the models";

Thank you and I hope you enjoyed the project!