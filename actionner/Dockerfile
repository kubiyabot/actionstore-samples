FROM bitnami/kubectl
ARG TARGETPLATFORM
ADD --chown=1001:1001 https://kubiya-cli.s3.eu-west-1.amazonaws.com/${TARGETPLATFORM}/kubiya-actionner /opt/kubiya-actionner
RUN chmod a+x /opt/kubiya-actionner
ENTRYPOINT /opt/kubiya-actionner -e /opt/bitnami/kubectl/bin/kubectl