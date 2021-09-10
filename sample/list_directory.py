from snakebite.client import Client


client = Client('localhost',9000)


for l in client.ls(['/']):
    print(l)