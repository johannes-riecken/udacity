FROM gcr.io/oss-fuzz-base/base-builder-python:v1
RUN apt-get update && apt-get install -y make autoconf automake libtool
COPY . $SRC/udacity
WORKDIR udacity
COPY .clusterfuzzlite/build.sh $SRC/
