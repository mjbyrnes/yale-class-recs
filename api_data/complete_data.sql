/*add course subject and number to the evaluation_courses data*/
create table intermediate as
select b.subject, b.number, a.*
from evaluation_courses as a
left join evaluation_course_names as b
on a.id = b.course_id;

/*merge with API data*/
create table intermediate2 as
select b.subject, b.number, b.id, b.season, b.title,b.long_title,b.average_rating,b.average_difficulty, b.num_students, a.descrip, a.time, a.dist1, a.dist2, a.dist3
from yale_API_data as a
inner join intermediate as b
on (a.subject = b.subject and b.number = a.num) or b.title = a.shortTitle or b.long_title = a.longTitle;

/* only take the most recent evaluations */
delete from intermediate2 where id not in (select max(id) from intermediate2 group by subject, number, title, long_title);

/*remove dupes*/
create table complete_data as select distinct * from intermediate2;

drop table intermediate;
drop table intermediate2;