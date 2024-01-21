FROM ubuntu:latest
LABEL authors="myhun"

ENTRYPOINT ["top", "-b"]