# TaskManagement
Create a simple a project and task management web application. Think of an extremely simplified version of Teamwork or Asana.

###### This Repository is shared among all developers.

## Contribution

| **Name** | **Email** |  **Gitlab Access** |
| --- | --- | --- | --- |
| Sanju Sci | sanju.sci9@gmail.com  | Owner

## Prerequisites

- [Python](https://www.python.org/downloads/) = 3.6
- [Pip3](https://pypi.python.org/pypi/pip) >= 1.5
- [MySQL](https://www.mysql.com/downloads/) >=5.5
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)>= 1.11


## Setup & Installation

- Create virtual environment, and activate it (Optional)-

```bash
# Install `virtualenv`
virtualenv -p python3 .env

# Activate virtual environment
source .env/bin/activate
```

- Clone git repository -

```bash
git clone https://github.com/sanjusci/TaskManagement.git

# cd to `project-dir`
cd TaskManagement
```

- Install dependencies -

    On Local -
    
    ```bash
    pip3 install -r requirements.txt
    ```
    On Prod - 
    
    ```bash
    pip3 install -r requirements.txt --user
    ```

```bash
# Add current project to `PYTHONPATH`
export PYTHONPATH="$PYTHONPATH:."
```

- [Create MySQL database](https://dev.mysql.com/doc/refman/5.7/en/creating-database.html)

- Set environment variables -

> If project is being run under `virtualenv` then environment variables can be set under `.env/bin/activate` file.

```bash
vim .env/bin/activate

# Append following lines at the end of the file after making appropriate changes.
export MYSQL_DB_USERNAME='<mysql_username>'
export MYSQL_DB_NAME='<mysql_database>'
export MYSQL_DB_HOST=localhost
export MYSQL_DB_PASSWORD='<mysql_password>'
export MYSQL_DB_MAX_AGE=<mysql_connect_age>
export MYSQL_DB_PORT=<mysql_port>
```

