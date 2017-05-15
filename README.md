# GraphQL demo app

### Description:
This is a short python Flask demo app, where we connect mysql database entities with graphql models, using sqlalchemy-graphene lib, in Relay style.

### Install app (development mode):
You will need to have python virtualenv installed.
Execute the following commands please, to install it:


```
git clone https://github.com/maddevsio/graphql-demo.git
cd graphql-demo
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
exit
./run.sh
```

Then open this address in your browser:

```
http://127.0.0.1:5000
```

And voila, you can see Graphiql interface open and ready!
