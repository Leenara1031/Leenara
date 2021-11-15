<%@page import="com.edu.center.member.vo.MemberVo"%>
<%@page import="java.util.List"%>
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
		List<MemberVo> memberVos = (List<MemberVo>) request.getAttribute("memberVos");
		MemberVo memberVo = memberVos.get(0);
	%>
	
	<form action="<%=contextPath%>/member/memberModifyConfirm" name="memberModifyForm" method="POST">
		<input type="hidden" name="m_no" value="<%=memberVo.getM_no()%>">
		ID: <input type="text" name="m_id" placeholder="input ID" readonly value="<%=memberVo.getM_id()%>"><br>
		PW: <input type="password" name="m_pw" placeholder="input PW" value="<%=memberVo.getM_pw()%>"><br>
		NAME: <input type="text" name="m_name" placeholder="input NAME" value="<%=memberVo.getM_name()%>"><br>
		GENDER: 
		<select name="m_gender">
			<option value="M" <% if (memberVo.getM_gender().equals("M")) {%>selected<%}%>>M</option>
			<option value="W" <% if (memberVo.getM_gender().equals("W")) {%>selected<%}%>>W</option>
		</select><br>
		AGE: <input type="number" name="m_age" placeholder="input AGE" value="<%=memberVo.getM_age()%>"><br>
		GRADE: <input type="number" name="m_grade" placeholder="input GRADE" value="<%=memberVo.getM_grade()%>"><br>
		MAJOR: <input type="text" name="m_major" placeholder="input MAJOR" value="<%=memberVo.getM_major()%>"><br>
		<input type="submit"> <input type="reset"><br>
		<a href="<%=contextPath%>/member/">member home</a>
	</form>

</body>
</html>




