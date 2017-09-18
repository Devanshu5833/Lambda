FROM python:2
RUN mkdir -p python_code
COPY . /python_code
RUN cd python_code && pip install -r requirement.txt
CMD ["python","/python_code/index.py"]