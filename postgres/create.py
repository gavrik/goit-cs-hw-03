from util import get_connection, execute_query

objects = ["create table if not exists users (\
           id serial primary key, \
           fullname varchar(100), \
           email varchar(100) \
           )",
           "create table if not exists status ( \
           id serial primary key, \
           name varchar(50) not null \
           )",
           "create table if not exists tasks ( \
           id serial primary key, \
           title varchar(100), \
           description varchar, \
           status_id integer not null, \
           user_id integer not null \
           )",
           "create unique index UDX_users_email on users(email) include (id)",
           "create unique index UDX_status_name on status(name) include (id)",
           "alter table tasks add constraint FK_status foreign key (status_id) references status(id) on delete cascade",
           "alter table tasks add constraint FK_user foreign key (user_id) references users(id) on delete cascade"
           ]


if __name__ == "__main__":
    conn = get_connection('192.168.88.211', 'postgres', 'tasks', 'hw03')
    for q in objects:
        _, err = execute_query(conn, q)
