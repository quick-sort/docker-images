FROM alpine:3.21

RUN apk add --no-cache tinyproxy

# Copy default config that allows all connections
COPY tinyproxy.conf /etc/tinyproxy/tinyproxy.conf

EXPOSE 8888

ENTRYPOINT ["tinyproxy", "-d"]
CMD []
