#FROM alpine:3

#LABEL author="Eko Kurniawa Khanedy"
#LABEL company="Programmer Zaman Now" website="https://www.programmerzamannow.com/"

#RUN mkdir hello
#RUN echo "Hello World" > "hello/world.txt"
#ADD text/*.txt hello
#COPY text/* hello

#CMD cat "hello/world.txt"
#CMD ls -l hello

#========================================
#FROM golang:1.18-alpine
#ENV APP_PORT=8080
#ENV APP_DATA=/logs

#RUN mkdir ${APP_DATA}
#RUN mkdir app
#COPY main.go app

#EXPOSE ${APP_PORT}
#VOLUME ${APP_DATA}
#CMD go run app/main.go

#========================================
#FROM golang:1.18-alpine

#WORKDIR /app
#COPY main.go /app

#EXPOSE 8080
#CMD go run main.go

#========================================
FROM golang:1.18-alpine

RUN mkdir /app

RUN addgroup -S pzngroup
RUN adduser -S -D -h /app pznuser pzngroup
RUN chown -R pznuser:pzngroup /app
USER pznuser

COPY main.go /app

EXPOSE 8080
CMD go run /app/main.go