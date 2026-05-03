FROM alpine:3.21

RUN apk add --no-cache tinyproxy

# Create runtime directories for PID file and logs
RUN mkdir -p /var/run/tinyproxy /var/log/tinyproxy && \
    chown nobody:nogroup /var/run/tinyproxy /var/log/tinyproxy

# Copy default config that allows all connections
COPY tinyproxy.conf /etc/tinyproxy/tinyproxy.conf

EXPOSE 8888

ENTRYPOINT ["tinyproxy", "-d"]
CMD []
