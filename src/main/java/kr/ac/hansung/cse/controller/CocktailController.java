package kr.ac.hansung.cse.controller;

import kr.ac.hansung.cse.model.Cocktail;
import kr.ac.hansung.cse.service.CocktailService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.SessionAttribute;
import org.springframework.web.multipart.MultipartFile;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import javax.servlet.http.HttpSession;
import java.util.ArrayList;
import java.util.List;

@Controller
public class CocktailController {

    // Controller -> Service -> Dao
    @Autowired
    private CocktailService cocktailService;

    @GetMapping("/result")
    public String showCocktailsBySurvey(Model model, @RequestParam(required = false) int alcohol,
                                        @RequestParam(required = false) int taste) {
        List<Cocktail> cocktails = cocktailService.getCocktailBySurvey(alcohol, taste);
        model.addAttribute("id_cocktails", cocktails);

        return "result";
    }

    @GetMapping("/resultf")
    public String showCocktailsFacial(Model model) {
        List<String> face = null;
        try {
            String csvFile = "C://dev/workspace/Homework1/src/main/webapp/resources/FER_API/emotion_results.csv";
            BufferedReader br = new BufferedReader(new FileReader(csvFile));

            String line = br.readLine();

            face = new ArrayList<>();

            // CSV 파일을 한 줄씩 읽어서 얼굴 감정 정보를 추출
            while ((line = br.readLine()) != null) {
                String[] data = line.split(","); // CSV 파일의 각 열을 분리

                String facialEmotion = data[1];

                face.add(facialEmotion);
            }


            // BufferedReader를 닫음
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }


        List<Cocktail> cocktails = cocktailService.getCocktailByFacial(face);
        model.addAttribute("id_cocktails", cocktails);

        return "resultf";
    }



    @GetMapping("/cocktaildetail")
    public String showCocktailDetails(Model model, @RequestParam(required = false) String name) {
            List<Cocktail> cocktails = cocktailService.getCocktailDetail(name);
            model.addAttribute("id_cocktails", cocktails);

        return "cocktaildetail";
    }

    @GetMapping("/select")
    public String showSelect() {


        return "select";
    }

    @GetMapping("/survey1")
    public String showSurvey1() {


        return "survey1";
    }
    @GetMapping("/survey2")
    public String showSurvey2() {


        return "survey2";
    }

    @GetMapping("/survey3")
    public String showSurvey3() {


        return "survey3";
    }

    @GetMapping("/camera")
    public String showCamera() {


        return "camera";
    }

    @GetMapping("/cameraws")
    public String showCameraws() {


        return "cameraws";
    }






}
