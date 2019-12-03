
--Consulta que obtiene las materias y grupos de un estudiante que 
--puede ver en su correspondiente semestre
select codigo_mat, nombre_mat, nombre_gru
from (estudiantes as est join programas as pro on pro.codigo_pro = est.programa 
	  join materias as mat on pro.codigo_pro = mat.programa)
	  join grupos as gru on mat.codigo_mat = gru.materia
where est.semestre = mat.semestre and est.codigo_est = 'EST216758432';

--Consulta de las materias acargo de un docente determinado
SELECT DISTINCT nombre_mat
FROM Grupos join Docentes on docente = codigo_doc 
      join Materias as mat on codigo_mat = materia
WHERE docente = 'DOC21983789';

--Consulta los grupos que tiene una determinada materia
SELECT nombre_gru
FROM Grupos
WHERE materia = 'MAT152';

--consulta que trae los programas que tiene a cargp un administrador
SELECT nombre_pro
FROM (Administradores join facultades on facultad = codigo_fac) as t1
     join programas as pro on t1.codigo_fac = pro.facultad
where t1.codigo_adm = 'ADM213067892';

--Consulta de las materias de un programa en especifico
SELECT codigo_mat, nombre_mat
FROM Programas join materias on codigo_pro = programa
WHERE codigo_pro = 'PRO001';

--Consulta de los grupos de una materia en especifico
SELECT codigo_gru, nombre_gru
FROM Grupos join Materias on materia = codigo_mat
WHERE codigo_mat = 'MAT151';

select codigo_adm, contraseña
from administradores;

--Consulta materias matriculadas por un estudiante en especifico
/*SELECT nombre_mat, nombre_gru
FROM matriculas join materias on materia = codigo_mat
      join grupos on grupo = codigo_gru
WHERE estudiante = 'EST2159839';*/

-- Consulta para obtener los datos necesarios para registrar una matricula
SELECT codigo_gru, codigo_mat
FROM grupos join materias on materia = codigo_mat
WHERE nombre_gru = 'GRUPO 1' and nombre_mat = 'ECUACIONES DIFERENCIALES' and programa='PRO001';

SELECT nombre_mat, nombre_gru
FROM (estudiantes as est join programas as pro on pro.codigo_pro = est.programa
	  join materias as mat on pro.codigo_pro = mat.programa)
	  join grupos as gru on mat.codigo_mat = gru.materia
	  right join matriculas as ma on mat.codigo_mat = ma.materia
WHERE est.semestre = mat.semestre and est.codigo_est = 'EST216034580' and ma.materia is NULL;

/*
delete from matriculas join materias on materia = codigo_mat
where estudiante = 'EST216034580' and nombre_mat = 'ECUACIONES DIFERENCIALES';
*/

select *
from matriculas join materias on materia = codigo_mat
where estudiante = 'EST216034580' and nombre_mat = 'ECUACIONES DIFERENCIALES';

SELECT mat.codigo_mat, mat.nombre_mat, gru.nombre_gru, est.semestre
FROM matriculas matri join materias mat on matri.materia=mat.codigo_mat
	join grupos gru on matri.grupo=gru.codigo_gru
	join estudiantes est on matri.estudiante=est.codigo_est
WHERE codigo_est='EST216034580';

SELECT nombre_mat, nombre_gru, cupo
FROM (estudiantes as est join programas as pro on pro.codigo_pro = est.programa
	  join materias as mat on pro.codigo_pro = mat.programa)
	  join grupos as gru on mat.codigo_mat = gru.materia
WHERE est.semestre = mat.semestre and cupo > 0 and and est.codigo_est = '%s';

SELECT mat.nombre_mat, gru.nombre_gru, gru.cupo
FROM ((matriculas matri join estudiantes est in matri.estudiante=est.codigo_est)
	join materias mat on matri.materia=mat.codigo_mat)
	join grupos gru on matri.grupo=gru.codigo_gru
WHERE est.codigo='%s' and gru.cupo>0 and matri.estado='MATRICULADA';
 
