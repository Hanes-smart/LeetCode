# Write your MySQL query statement below
select e.name as Employee
from Employee as e
join Employee as m
on e.ManagerId = m.id
where e.salary > m.salary;#here e.salary is detection sala of emp who is under manaid 3