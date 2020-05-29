FROM  amancevice/pandas
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src /src
COPY ./logs /logs
CMD ["sh", "-c", "echo $LOGFILE; python logr-gaps.py $LOGFILE"]
