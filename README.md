### Azure code samples

#### SQL Server with Python

[Deploy Azure SQL Edge with Docker](https://learn.microsoft.com/en-us/azure/azure-sql-edge/disconnected-deployment)

##### With sqlmodel

```sh
# https://github.com/pymssql/pymssql/issues/769#issuecomment-1671579601
brew install FreeTDS
export CFLAGS="-I$(brew --prefix openssl)/include"
export LDFLAGS="-L$(brew --prefix openssl)/lib -L/usr/local/opt/openssl/lib"
export CPPFLAGS="-I$(brew --prefix openssl)/include"

pip3 install --pre --no-binary :all: -r requirements.txt --no-cache
python3 -m sqlmodel_sample.app
```

References: https://sqlmodel.tiangolo.com/tutorial/

##### With sqlalchemy

```sh

python3 -m sqlalchemy_sample.app
```

References: https://docs.sqlalchemy.org/en/20/tutorial/