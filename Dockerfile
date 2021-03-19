# We're using Ubuntu 20.10
FROM koala21/dockerfile:latest

#
# Clone repo and prepare working directory
#
RUN git clone -b Kampang https://github.com/tungauicipiyey/kampang-bot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/tungauicipiyey/Kampang-Bot/Kampang/requirements.txt

CMD ["python3","-m","userbot"]
