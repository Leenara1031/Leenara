package com.edu.news.dao;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Component;
import com.edu.news.vo.NewsVo;

@Component
public class NewsDao {

	@Autowired
	JdbcTemplate jdbcTemplate;
	
	public List<NewsVo> getNewsList() {
		
		String sql = "SELECT * FROM tbl_news";
		List<NewsVo> newsVos = jdbcTemplate.query(sql, new RowMapper<NewsVo>() {

			@Override
			public NewsVo mapRow(ResultSet rs, int rowNum) throws SQLException {
				
				NewsVo newsVo = new NewsVo();
				newsVo.setN_no(rs.getInt("n_no"));
				newsVo.setN_title(rs.getString("n_title"));
				newsVo.setN_title_href(rs.getString("n_title_href"));
				newsVo.setN_photo_name(rs.getString("n_photo_name"));
				newsVo.setN_article(rs.getString("n_article"));
				newsVo.setN_publisher(rs.getString("n_publisher"));
				newsVo.setN_reg_date(rs.getString("n_reg_date"));
				
				return newsVo;
			}
			
		});
		
		return newsVos;
	}

}
