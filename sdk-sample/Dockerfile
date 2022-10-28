FROM python:3.11

ADD requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

ADD organization.py /opt/
CMD python -m kubiya.serve /opt/organization.py
