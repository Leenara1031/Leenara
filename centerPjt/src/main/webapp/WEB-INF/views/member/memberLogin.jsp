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
	
		session = request.getSession();
		if (session.getAttribute("m_id") != null) {
	%>
	
	<div>
		Hello <%=session.getAttribute("m_id")%>.<br>
		<a href="<%=contextPath%>/member/memberLogout">log out</a><br>
		<a href="<%=contextPath%>/member/memberModify?m_id=<%=session.getAttribute("m_id")%>">modify</a><br>
		<a href="<%=contextPath%>/member/memberDeleteConfirm?m_id=<%=session.getAttribute("m_id")%>">delete</a>
	</div>
	
	<%
		} else {
	%>
	
	<div>
		<form action="<%=contextPath%>/member/memberLoginConfirm" name="memberLoginForm" method="POST">
			<input type="text" name="m_id" placeholder="input ID"><br>
			<input type="password" name="m_pw" placeholder="input PW"><br>
			<input type="submit"> <input type="reset"><br>
			<a href="<%=contextPath%>/member/memberJoin">join</a>
		</form>
	</div>
	
	<%
		}
	%>

</body>
</html>