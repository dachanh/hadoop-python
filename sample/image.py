import cv2
from snakebite.client import Client

client = Client('localhost',9000)


for l in client.ls(['/home/']):
    print(l)

