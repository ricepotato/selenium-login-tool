FROM ricepotato/chrome-selenium-docker:latest
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY app.py /app
COPY browser.py /app
COPY dockerentrypoint.sh /app
CMD [ "./dockerentrypoint.sh" ]