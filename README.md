logr-gaps
. ├── app
│   ├── Dockerfile 
│   ├── logs 
│   │   └── test_small.log 
│   ├── requirements.txt 
│   └── src 
│   └── logr-gaps.py 
└── docker-compose.yml

On docker host execute:
`xhost +`

`docker-compose build`
`docker-compose run -d -e LOGFILE=test_small.log -e DISPLAY=unix:0 app`
`docker-compose down`

The logfile for parsing needs to be copied into the ./app/logs folder, 
then provide the name of the logfile to the LOGFILE environment variable

ex : `docker-compose run -d -e LOGFILE=20200526.log -e DISPLAY=unix:0 app`
