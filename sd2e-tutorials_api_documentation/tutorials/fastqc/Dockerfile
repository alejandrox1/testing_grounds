FROM sd2e/base:ubuntu16

#RUN mkdir /opt/scripts
#ADD /src/hello.sh /opt/scripts/hello.sh
#CMD /opt/scripts/hello.sh "I am a container-basd app"

WORKDIR /opt
ADD https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip .

RUN apt-get update -y && apt-get install -y zip default-jre && \
    unzip fastqc_v0.11.5.zip && \
    rm fastqc_v0.11.5.zip && \
    chmod +x /opt/FastQC/fastqc

ENV PATH "$PATH:/opt/FastQC/"

CMD ["bash"]
