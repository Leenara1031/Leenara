package com.edu.center.member.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.edu.center.member.dao.IMemberDaoMapper;
import com.edu.center.member.dao.MemberDao;
import com.edu.center.member.vo.MemberVo;

@Service
public class MemberService {

//	@Autowired
//	MemberDao memberDao;
	

	@Autowired
	IMemberDaoMapper iMemberDaoMapper;
	
	@Transactional
	public void memberJoinConfirm(MemberVo memberVo) {
		iMemberDaoMapper.memberJoinConfirm(memberVo);
		
	}

	@Transactional
	public int memberLoginConfirm(MemberVo memberVo) {
		return iMemberDaoMapper.memberLoginConfirm(memberVo);
		
	}

	@Transactional
	public List<MemberVo> memberModify(MemberVo memberVo) {		
		return iMemberDaoMapper.memberModify(memberVo);
	}

	@Transactional
	public void memberModifyConfirm(MemberVo memberVo) {
		iMemberDaoMapper.memberModifyConfirm(memberVo);
		
	}

	@Transactional
	public void memberDeleteConfirm(MemberVo memberVo) {
		iMemberDaoMapper.memberDeleteConfirm(memberVo);
		
	}

	@Transactional
	public List<MemberVo> memberList() {
		return iMemberDaoMapper.memberList();
	}

}
