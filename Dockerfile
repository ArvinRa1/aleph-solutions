#Deriving the latest base image
FROM python:latest


#Labels as key value pair
# LABEL Maintainer="roushan.me17"

COPY requirements.txt ./

RUN python -m pip install --upgrade pip
RUN pip uninstall mkl-fft
RUN pip install mkl-fft==1.3.1
RUN pip install -r requirements.txt

# Any working directory can be chosen as per choice like '/' or '/home' etc

WORKDIR /Users/arvinrastegar/Documents/aleph-solutions

#to COPY the remote file at working directory in container
COPY apis.py ./
# Now the structure looks like this '/Users/arvinrastegar/Documents/aleph-solutions/apis.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./apis.py"]