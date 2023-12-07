FROM archlinux:latest
USER root
RUN pacman-key --init
RUN pacman -Syu --noconfirm python wget tar python-requests nvidia
COPY main.py requirements.txt /miner/
WORKDIR /miner
RUN python main.py
WORKDIR /miner/lolminer
CMD ./lolMiner -a KARLSEN -p kls.baikalmine.com:2626 -u karlsen:qqyyzmaggnmtcje272lvgzy4lf8z7lt2pvv50zh5tms99a6wd56rygsgpu958.5600x --coff 150 --cclk 1200 --mclk 810 --pl 150
