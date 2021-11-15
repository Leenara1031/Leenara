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

	<div>
		ID or PW is not database.<br>
		<a href="<%=contextPath%>/member/memberLogin">member login</a>
	</div>

</body>
</html>