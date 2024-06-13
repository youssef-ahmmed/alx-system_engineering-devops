# Project: 0x1A. Application server

## Resources

#### Read or watch:

* [Application server vs web server](https://f5.com/glossary)
* [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04)
* [Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html)
* [Be careful with the way Flask manages slash](https://werkzeug.palletsprojects.com/en/3.0.x/)
* [Upstart documentation](https://doc.ubuntu-fr.org/upstart)

## Tasks

| Task                                 | File                                                             |
|--------------------------------------|------------------------------------------------------------------|
| 0. Set up development with Python    | [README.md](./README.md)                                         |
| 1. Set up production with Gunicorn   | [DIR](./)                                                        |
| 2. Serve a page with Nginx           | [2-app_server-nginx_config](./2-app_server-nginx_config)         |
| 3. Add a route with query parameters | [3-app_server-nginx_config](./3-app_server-nginx_config)         |
| 4. Let's do this for your API        | [4-app_server-nginx_config](./4-app_server-nginx_config)         |
| 5. Serve your AirBnB clone           | [5-app_server-nginx_config](./5-app_server-nginx_config)         |
| 6. Deploy it!                        | [gunicorn.service](./gunicorn.service)                           |
| 7. No service interruption           | [4-reload_gunicorn_no_downtime](./4-reload_gunicorn_no_downtime) |