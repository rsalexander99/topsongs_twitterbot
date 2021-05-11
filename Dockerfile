FROM python

COPY replymentions.py replymentions.py
COPY Spotify_IDs.csv Spotify_IDs.csv
COPY latest_id.txt latest_id.txt
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "./replymentions.py" ]