FROM ubuntu:latest
ENV LC_CTYPE C.UTF-8
ENV DEBIAN_FRONTEND=interactive
RUN apt-get update && apt-get upgrade && \
dpkg --add-architecture i386 && \
apt-get install build-essential jq strace ltrace curl wget ruby rubygems cc dnsutils netcat gcc-multilib net-tools vim gdb gdb-multiarch python python3 python3-pip python3-dev libssl-dev libffi-dev git make procps libpcre3-dev libdb-dev libxt-dev libxaw7-dev libc6:i386 libncurses5:i386 libstdc++6:i386 -y && \
python3 -m pip install keystone-engine capstone ropper && \
pip3 install unicorn==1.0.2rc2 && \
pip3 install pwntools==4.4.0beta1 && \
mkdir tools && cd tools && \
git clone https://github.com/JonathanSalwan/ROPgadget && \
git clone https://github.com/radare/radare2 && cd radare2 && sys/install.sh &&\
cd .. && git clone https://github.com/longld/peda.git && cd peda && echo "source /tools/peda/peda.py" >> ~/.gdbinit && \
cd .. && git clone https://github.com/niklasb/libc-database && cd libc-database && ./get ubuntu && \
cd .. && cd .. && gem install one_gadget
