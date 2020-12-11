SELECT name Teacher,StudentCount
FROM
  (SELECT name,StudentCount, rownum rn
   FROM
     (SELECT t.name,count(s.id) StudentCount
      FROM Students s,Teachers t,StudentTeacherAssoc st
      WHERE s.id=st.studentid AND t.id=st.teacherid AND s.grade<=5
      GROUP BY t.name
      UNION SELECT DISTINCT t.name,0 AS StudentCount
      FROM Students s,Teachers t,StudentTeacherAssoc st
      WHERE s.id=st.studentid AND t.id=st.teacherid AND s.grade>5
      ORDER BY StudentCount DESC))
WHERE rn <=3;

