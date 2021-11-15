package com.edu.center.member.dao;

import java.util.List;

import com.edu.center.member.vo.MemberVo;

public interface IMemberDaoMapper {
	public void memberJoinConfirm(MemberVo memberVo);
	public int memberLoginConfirm(MemberVo memberVo);
	public List<MemberVo> memberModify(MemberVo memberVo);
	public void memberModifyConfirm(MemberVo memberVo);
	public void memberDeleteConfirm(MemberVo memberVo); 
	public List<MemberVo> memberList();
	
}
