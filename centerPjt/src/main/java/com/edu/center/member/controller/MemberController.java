package com.edu.center.member.controller;

import java.util.List;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import com.edu.center.member.service.MemberService;
import com.edu.center.member.vo.MemberVo;

@Controller
@RequestMapping(value = "/member")
public class MemberController {

	@Autowired
	MemberService memberService;
	
	@RequestMapping(value = {"", "/"}, method = RequestMethod.GET)
	public String member() {
		return "redirect:/member/memberLogin";
	}
	
	@RequestMapping(value = "/memberJoin", method = RequestMethod.GET)
	public String memberJoin() {
		return "member/memberJoin";
	}
	
	@RequestMapping(value = "/memberJoinConfirm", method = RequestMethod.POST)
	public String memberJoinConfirm(MemberVo memberVo) {
		
		memberService.memberJoinConfirm(memberVo);
		
		return "redirect:/member/";
	}
	
	@RequestMapping(value = "/memberLogin", method = RequestMethod.GET)
	public String memberLogin() {
		return "member/memberLogin";
	}
	
	@RequestMapping(value = "/memberLoginConfirm", method = RequestMethod.POST)
	public String memberLoginConfirm(MemberVo memberVo, HttpSession session) {
		
		int result = memberService.memberLoginConfirm(memberVo);
		
		if (result <= 0) 
			return "member/memberLoginFail";
		
		session.setAttribute("m_id", memberVo.getM_id());
		return "redirect:/member/";
	}
	
	@RequestMapping(value = "/memberLogout", method = RequestMethod.GET)
	public String memberLogout(HttpSession session) {
		session.invalidate();
		return "redirect:/member/";
	}
	
	@RequestMapping(value = "/memberModify", method = RequestMethod.GET)
	public ModelAndView memberModify(MemberVo memberVo, ModelAndView modelAndView) {

		List<MemberVo> memberVos = memberService.memberModify(memberVo);
		
		modelAndView.addObject("memberVos", memberVos);
		modelAndView.setViewName("member/memberModify");
		
		return modelAndView;
	}
	
	@RequestMapping(value = "/memberModifyConfirm", method = RequestMethod.POST)
	public String memberModifyConfirm(MemberVo memberVo) {
		
		memberService.memberModifyConfirm(memberVo);
		
		return "redirect:/member/";
	}
	
	@RequestMapping(value = "/memberDeleteConfirm", method = RequestMethod.GET)
	public String memberDeleteConfirm(MemberVo memberVo, HttpSession session) {
		
		memberService.memberDeleteConfirm(memberVo);
		session.invalidate();
		
		return "redirect:/member/";
	}
	
	@RequestMapping(value = "/memberList", method = RequestMethod.GET)
	public ModelAndView memberList(ModelAndView modelAndView) {
		
		List<MemberVo> memberVos = memberService.memberList();
		
		modelAndView.addObject("memberVos", memberVos);
		modelAndView.setViewName("member/memberList");
		
		return modelAndView;

	}
	
}
