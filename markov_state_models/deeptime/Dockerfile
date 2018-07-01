FROM alejandrox1/ubuntu18_miniconda3-dev
MAINTAINER alejandrox1

ARG UID=1000
ARG USER=docker
ARG REPO=https://github.com/alejandrox1/deeptime
ARG REPO_LOC=deeptime                            
ARG UPSTREAM=https://github.com/markovmodel/deeptime                            

RUN apt-get update -y && pip install virtualenv jupyter && \
    conda install -y pytorch-cpu torchvision-cpu -c pytorch && \
    conda config --add channels conda-forge && conda install -y pyemma
# Passwordless sudo.
#RUN useradd -u $UID -ms /bin/bash -G sudo $USER && echo "$USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
# Sudo with password.
RUN useradd -u $UID -ms /bin/bash -G sudo $USER && echo "$USER:docker" | chpasswd

# There should be a cool .bash_prompt and .vimrc here already.
RUN cp ~/.bash_prompt /home/$USER/.bash_prompt  && echo "source ~/.bash_prompt" >> /home/$USER/.bashrc && \
    cp ~/.vimrc /home/$USER/.vimrc

WORKDIR /home/$USER
# Get your repo.
RUN git clone $REPO $REPO_LOC && \
    cd $REPO_LOC && \
    git remote add upstream $UPSTREAM && \
    python time-lagged-autoencoder/setup.py install && \
    cd ../ && chmod -R go=u $REPO_LOC

USER $USER                                                                      

WORKDIR /home/$USER/$REPO_LOC
EXPOSE 8888
RUN jupyter notebook --generate-config && \
    pwd && ls -l ../deeptime  && echo "jupyter notebook password && jupyter notebook --ip 0.0.0.0 --no-browser" >> run.sh && \
    chmod +x run.sh
CMD ["/bin/bash"] 
