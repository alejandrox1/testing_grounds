#    Mappy
#
# https://gitlab.com/alejandrox1/mappy
#
FROM alejandrox1/ubuntu18_miniconda3-dev
MAINTAINER alejandrox1

ARG UID=1000
ARG USER=docker
ARG REPO=https://gitlab.com/alejandrox1/mappy
ARG REPO_LOC=mappy
ARG UPSTREAM=https://gitlab.com/sd2e/mappy

RUN apt-get update -y 
    # Commenting these out in order to have the system updated - may need to
    # install something during an interactive run
    #rm -rf /var/lib/apt/lists/* && \
    #rm -rf /src/.*deb

# Passwordless sudo.
#RUN useradd -u $UID -ms /bin/bash -G sudo $USER && echo "$USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
# Sudo with password.
RUN useradd -u $UID -ms /bin/bash -G sudo $USER && echo "$USER:docker" | chpasswd

# There should be a cool .bash_prompt and .vimrc here already.
RUN cp ~/.bash_prompt /home/$USER/.bash_prompt  && echo "source ~/.bash_prompt" >> /home/$USER/.bashrc && \
    cp ~/.vimrc /home/$USER/.vimrc


USER $USER

WORKDIR /home/$USER


# Get your repo.
ADD clone.sh .
CMD ./clone.sh && /bin/bash
