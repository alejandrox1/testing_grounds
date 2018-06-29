#    SD2E-CLI
#
# Install sd2e-cli from source. This image specification file allows you to
# specify what branch to build off of.
#
FROM alejandrox1/ubuntu18-dev
MAINTAINER alejandrox1

ARG UID=1000
ARG USER=docker
ARG REPO=https://github.com/alejandrox1/sd2e-cli
ARG REPO_LOC=sd2e-cli
ARG UPSTREAM=https://github.com/SD2E/sd2e-cli

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
RUN git clone --recurse-submodules $REPO $REPO_LOC && \
    cd $REPO_LOC && \
    git remote add upstream $UPSTREAM

# COntainer specific commands.
ENV PATH /home/$USER/$REPO_LOC/bin:$PATH

CMD ["/bin/bash"]
