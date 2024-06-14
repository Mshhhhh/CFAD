package kr.ac.hansung.cse.service;

import kr.ac.hansung.cse.dao.CocktailDao;
import kr.ac.hansung.cse.model.Cocktail;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CocktailService {

    //service -> dao
    @Autowired
    private CocktailDao cocktailDao;

    public List<Cocktail> getCocktailBySurvey(int alcohol, int taste)
    { return cocktailDao.getCocktailsBySurvey(alcohol, taste); }

    public List<Cocktail> getCocktailDetail(String name)
    { return cocktailDao.getCocktailsDetail(name); }

    public List<Cocktail> getCocktailByFacial(List<String> face)
    { return cocktailDao.getCocktailsByFacial(face); }



}
