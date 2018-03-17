gunicorn run:app -p run.pid -b  192.168.1.101:6666 -D --error-logfile error.log --access-logfile debug.log 
