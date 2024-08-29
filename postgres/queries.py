from util import get_connection


queries = [
    "select * from tasks where user_id = 98",
    "select * from tasks where status_id = (select id from status where name='completed')",
    "update tasks set status_id = (select id from status where name = 'in progress') where id = 87",
    "select u.* from tasks t left join users u on u.id = t.user_id where status_id not in (select id from status)",
    "insert into tasks(title, description, status_id, user_id) values('manual', 'manual added tasks', 1, 37)",
    "select * from tasks where status_id not in (select id from status where name not in ('completed'))",
    "delete from tasks where id = 42",
    "select * from users where email like 'cole%'",
    "update users set fullname = 'Manual Manual' where id = 54",
    "select status_id, count(1) from tasks group by status_id",
    "select t.* from tasks as t left join users as u on u.id = t.user_id where u.email like '%@example.com'",
    "select * from tasks where description is null",
    "select u.* from tasks as t left join users as u on u.id = t.id left join status as s on s.id = t.status_id where s.name = 'in progress'",
    "with cte as (select t.user_id as user_id, count(t.id) as task_count from tasks as t left join users u on u.id = t.user_id group by t.user_id) \
    select u.fullname, c.task_count from users as u left join cte as c on c.user_id = u.id"
]

if __name__ == '__main__':
    conn = get_connection('192.168.88.211', 'postgres', 'tasks', 'hw03')
    n = 10

    with conn.cursor() as curr:
        for s in queries:
            print('=======')
            curr.execute(s)
            print(curr.query)
            print(curr.rowcount)
            try:
                res = curr.fetchmany(n)
                for r in res:
                    print(r)
            except:
                pass
            print('=======\n\n')
