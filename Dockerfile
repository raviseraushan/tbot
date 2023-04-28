FROM python:3.10-slim

RUN pip3 install -U pyrogram tgcrypto
RUN pip3 install -U https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz

COPY dd.py dd.py

CMD ["python", "dd.py"]
