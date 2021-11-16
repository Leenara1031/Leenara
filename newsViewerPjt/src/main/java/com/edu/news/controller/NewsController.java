package com.edu.news.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.edu.news.service.NewsService;
import com.edu.news.vo.NewsVo;

@Controller
public class NewsController {

	@Autowired
	NewsService newsService;
	
	@RequestMapping(value="/newsList", method=RequestMethod.GET)
	public String newsList(Model model) {
		
		List<NewsVo> newsVos = newsService.getNewsList();
		model.addAttribute("newsVos", newsVos);
		
		return "news_list";
	}
	
}
