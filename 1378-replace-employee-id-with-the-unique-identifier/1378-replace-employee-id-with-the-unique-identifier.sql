select eu.unique_id,e.name
from employees e
left join EmployeeUNI as eu
on e.id = eu.id;

