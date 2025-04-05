FROM python:3.9
WORKDIR /code
COPY requirements_app.txt .
RUN pip install --no-cache-dir --upgrade -r requirements_app.txt
COPY . /code
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]