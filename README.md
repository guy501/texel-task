# texel-task

#requirement:

pip3 install urllib3==1.24
pip3 install requests-html==0.10.0

#build the image:

docker build -t guy:test .

#running the service:

kubectl apply -f date.yaml 

#running validation:

python3 validate_date.py

