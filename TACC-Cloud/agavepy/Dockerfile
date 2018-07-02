#    AGAVEPY
#
# Install agavePY from source.
#
FROM alejandrox1/ubuntu18_python-dev
MAINTAINER alejandrox1

ARG UID=1000
ARG USER=docker
ARG REPO=https://github.com/alejandrox1/agavepy
ARG REPO_LOC=agavepy
ARG UPSTREAM=https://github.com/TACC/agavepy

RUN apt-get update -y && pip install virtualenv 
    # Commenting these out in order to have the system updated - may need to
    # install something during an interactive run
    #rm -rf /var/lib/apt/lists/* && \
    #rm -rf /src/.*deb

###############################################################################
#                                                                             #
#                           Agavepy dependencies!                             #
#                                                                             #
###############################################################################
#RUN apt-get install -y bats jq

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
RUN git clone $REPO $REPO_LOC && \
    cd $REPO_LOC && \
    git remote add upstream $UPSTREAM


CMD ["/bin/bash"]
