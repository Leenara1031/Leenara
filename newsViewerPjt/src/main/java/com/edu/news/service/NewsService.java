package com.edu.news.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.edu.news.dao.NewsDao;
import com.edu.news.vo.NewsVo;

@Service
public class NewsService {

	@Autowired
	NewsDao newsDao;
	
	public List<NewsVo> getNewsList() {
		return newsDao.getNewsList();
	}

}
