import os

token = os.environ['TOKEN']
print(f'The token retrieved is {token}')

if token == "production":
    print("The TOKEN retrieved from production environment")
elif token == "dev":
    print("The TOKEN retrieved from dev environment")
elif token == "repo":
    print("The TOKEN retrieved from repo secrets")
else:
    print("The TOKEN doesn't exist")