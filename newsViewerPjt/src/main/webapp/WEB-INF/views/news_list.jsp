<%@page import="com.edu.news.vo.NewsVo"%>
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

<table>
	<tr>
		<td>no</td>
		<td>title</td>
		<td>photo</td>
		<td>article</td>
		<td>publisher</td>
		<td>reg_date</td>
	</tr>
	
	<% 
	
	List<NewsVo> newsVos = (List<NewsVo>) request.getAttribute("newsVos");
	for(int i = 0; i<newsVos.size(); i++){
	%>
		
	<tr>
		<td><%=newsVos.get(i).getN_no()%></td>
		<td><a href="<%= newsVos.get(i).getN_title_href() %>" target="_blank"><%=newsVos.get(i).getN_title()%></a></td>
		<td>photo</td>
		<td><%=newsVos.get(i).getN_article()%></td>
		<td><%=newsVos.get(i).getN_publisher()%></td>
		<td><%=newsVos.get(i).getN_reg_date()%></td>
	</tr>
		
	<%
	}
	%>
	
</table>

</body>
</html>