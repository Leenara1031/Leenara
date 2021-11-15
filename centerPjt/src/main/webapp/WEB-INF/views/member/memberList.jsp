<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

	<%
		String contextPath = request.getContextPath();
	%>
	
	<form action="<%=contextPath%>/member/memberJoinConfirm" name="memberJoinForm" method="POST">
		ID: <input type="text" name="m_id" placeholder="input ID"><br>
		PW: <input type="password" name="m_pw" placeholder="input PW"><br>
		NAME: <input type="text" name="m_name" placeholder="input NAME"><br>
		GENDER: 
		<select name="m_gender">
			<option value="M">M</option>
			<option value="W">W</option>
		</select><br>
		AGE: <input type="number" name="m_age" placeholder="input AGE"><br>
		GRADE: <input type="number" name="m_grade" placeholder="input GRADE"><br>
		MAJOR: <input type="text" name="m_major" placeholder="input MAJOR"><br>
		<input type="submit"> <input type="reset"><br>
		<a href="<%=contextPath%>/member/">member login</a>
	</form>

</body>
</html>




