package com.edu.center.member.dao;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Component;

import com.edu.center.member.vo.MemberVo;

@Component
public class MemberDao {
	
//	@Autowired
//	JdbcTemplate jdbcTemplate;
	
//	public void memberJoinConfirm(MemberVo memberVo) {
//
//		String sql = "INSERT INTO tbl_members(m_id, m_pw, m_name, m_gender, m_age, m_grade, m_major, m_reg_date, m_mod_date) "
//				+ "VALUES(?, ?, ?, ?, ?, ?, ?, NOW(), NOW())";
//		
//		Object[] args = {memberVo.getM_id(), memberVo.getM_pw(), memberVo.getM_name(), 
//				memberVo.getM_gender(), memberVo.getM_age(), memberVo.getM_grade(), memberVo.getM_major()};
//		
//		int result = jdbcTemplate.update(sql, args);
//		
//		if (result == 1)  System.out.println("MEMBER JOIN SUCCESS!!");
//		else System.out.println("MEMBER JOIN FAIL!!");
//		
//	}

//	public int memberLoginConfirm(MemberVo memberVo) {
//		
//		String sql = "SELECT COUNT(*) FROM tbl_members WHERE m_id = ? AND m_pw = ?";
//		
//		Object[] args = {memberVo.getM_id(), memberVo.getM_pw()};
//		int result = jdbcTemplate.queryForObject(sql, Integer.class, args);
//		
//		return result;
//		
//	}

//	public List<MemberVo> memberModify(MemberVo memberVo) {
//		
//		String sql = "SELECT * FROM tbl_members WHERE m_id = ?";
//		Object[] args = {memberVo.getM_id()};
//		List<MemberVo> memberVos = jdbcTemplate.query(sql, new RowMapper<MemberVo>() {
//
//				@Override
//				public MemberVo mapRow(ResultSet rs, int rowNum) throws SQLException {
//					
//					MemberVo memberVo = new MemberVo();
//					memberVo.setM_no(rs.getInt("m_no"));
//					memberVo.setM_id(rs.getString("m_id"));
//					memberVo.setM_pw(rs.getString("m_pw"));
//					memberVo.setM_name(rs.getString("m_name"));
//					memberVo.setM_gender(rs.getString("m_gender"));
//					memberVo.setM_age(rs.getInt("m_age"));
//					memberVo.setM_grade(rs.getInt("m_grade"));
//					memberVo.setM_major(rs.getString("m_major"));
//					memberVo.setM_reg_date(rs.getString("m_reg_date"));
//					memberVo.setM_mod_date(rs.getString("m_mod_date"));
//					
//					return memberVo;
//				}
//			
//		}, args);
//		
//		
//		return memberVos;
//	}

//	public void memberModifyConfirm(MemberVo memberVo) {
//		
//		String sql = "update tbl_members set m_pw = ?, "
//											+ "m_name = ?, "
//											+ "m_gender = ?, "
//											+ "m_age = ?, "
//											+ "m_grade = ?, "
//											+ "m_major = ?, "
//											+ "m_mod_date = NOW() "
//											+ "where m_no = ?";
//		Object[] args = {memberVo.getM_pw(), 
//							memberVo.getM_name(), 
//							memberVo.getM_gender(), 
//							memberVo.getM_age(), 
//							memberVo.getM_grade(), 
//							memberVo.getM_major(), 
//							memberVo.getM_no()};
//		
//		int result = jdbcTemplate.update(sql, args);
//		
//		if (result > 0) {
//			System.out.println("MEMBER MODIFY SUCCESS!!");
//		} else {
//			System.out.println("MEMBER MODIFY FAIL!!");
//		}
//		
//	}

//	public void memberDeleteConfirm(MemberVo memberVo) {
//		
//		String sql = "DELETE FROM tbl_members WHERE m_id = ?";
//		Object[] args = {memberVo.getM_id()};
//		int result = jdbcTemplate.update(sql, args);
//		
//		if (result > 0) {
//			System.out.println("MEMBER DELETE SUCCESS!!");
//		} else {
//			System.out.println("MEMBER DELETE FAIL!!");
//		}	
//	}

//	public List<MemberVo> memberList() {
//		
//		String sql = "SELECT * FROM tbl_members";
//		
//		List<MemberVo> memberVos = jdbcTemplate.query(sql, new RowMapper<MemberVo>() {
//
//			@Override
//			public MemberVo mapRow(ResultSet rs, int rowNum) throws SQLException {
//				
//				MemberVo memberVo = new MemberVo();
//				memberVo.setM_no(rs.getInt("m_no"));
//				memberVo.setM_id(rs.getString("m_id"));
//				memberVo.setM_pw(rs.getString("m_pw"));
//				memberVo.setM_name(rs.getString("m_name"));
//				memberVo.setM_gender(rs.getString("m_gender"));
//				memberVo.setM_age(rs.getInt("m_age"));
//				memberVo.setM_grade(rs.getInt("m_grade"));
//				memberVo.setM_major(rs.getString("m_major"));
//				memberVo.setM_reg_date(rs.getString("m_reg_date"));
//				memberVo.setM_mod_date(rs.getString("m_mod_date"));
//				
//				return memberVo;
//				
//			}
//			
//		});
//		
//		return memberVos;
//	}

}
