FROM ubuntu:latest
LABEL authors="Alexey Hramov, Luca Zabel"
RUN apt-get add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y python3.11
RUN apt-get install -y python3-pip

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
RUN pip install soundfile
RUN pip install playsound==1.2.2
RUN pip install bark
RUN pip install scipy

# run interactive python script
WORKDIR /app
COPY interactive.py /app
ENTRYPOINT ["python3", "interactive.py"]