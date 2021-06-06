# texel-task

#requirement:

urllib3 < 1.25

#build the image:

docker build -t guy:test .

#running the service:

kubectl apply -f date.yaml 

#running validation:

python3 validate_date.py

