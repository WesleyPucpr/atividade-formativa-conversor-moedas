FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
#RUN pip install --no-cache-dir "fastapi[standard]"


EXPOSE 80
COPY . .
CMD [ "fastapi", "run", "main.py", "--port", "80" ]
