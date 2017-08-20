AppCourse
=========

=== O que é o AppCourse

Uma simples plataforma para ensino a distância
Focada em cursos abertos e massivos
Desenvolvida em Python 3.6.1 e Django 1.10.3

== Funcionalidades

Sistema de Aulas
Fórum de Dúvidas
Exercícios de submissão
Sistema de Avisos
Sistema de Contas

== Sistema de Aulas

Criação, edição e remoção de aulas e módulos

Aulas compostas por:
video aulas
Downloads
Quizzes
As aulas estarão associadas a um curso

== Fórum de dúvidas

Um fórum aberto
Tópicos separados por categoria
Usuários precisam estar logados

== Exercicios de submissão

Os alunos poderão enviar sua solução via arquivo
Poderá conter algum tipo de validação automática
As submissões irão gerar notas para os alunos


== Sistema de Avisos


Mural de avisos
Os avisos serão enviados para os alunos por email
Terão uma página onde poderão receber comentários

== Sistema de contas

Os usuários poderão se cadastrar e logar no sistema
Os usuários poderão alterar o seu perfil
Os usuários terão um perfil público

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: GPLv3


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html
