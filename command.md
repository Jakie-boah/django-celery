pip freeze > requirements.txt
http://0.0.0.0:8000/
docker-compose up -d --build
docker exec -it django /bin/sh
celery inspect active
from dcelery.celerytasks.ex1_try_except import my_task
from dcelery.celerytasks.ex5_chain import run_task


t2.apply_async(priority=5)
t1.apply_async(priority=6)
t3.apply_async(priority=9)
t2.apply_async(priority=5)
t1.apply_async(priority=6)
t3.apply_async(priority=9)