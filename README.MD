
# Codacty Shop App

This is a task project. However, you may use it whichever way you want in your personal project.
## How to set up?

By using docker we can easily set up project.

###### To successfully set up this project ensure you have "Make" and "Docker" installed in your Mac or Linux environment or WSL2 (Windows users), enter the following commands in your terminal to get started:

```bash
  1 - git clone https://github.com/otuozeAhmed/codacty-shop.git
  2 - cd codacty-shop
  # Before the next step, rename .env.example to .env (Note: the values here are all examples just to get you up and running)
  3 - sudo make up
  4 - sudo make migrate
  5 - sudo make collectstatic

  ==> visit http://0.0.0.0/en/ to view your project
  5i - sudo make superuser (to create a superuser access to admin)
  admin ==> http://0.0.0.0/en/admin
  5ii - sudo make logs (to view all container logs)

  # look-up the Makefile in the codacty-shop
  # directory for more handy commands with make
```
Note: This project utilizes internationalization, kindly add the spanish version of any products or categories you create to avoid error response when their spanish version is requested. Project scaffold files, settings, modules are automatically translated.
