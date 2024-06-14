package kr.ac.hansung.cse.model;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
@NoArgsConstructor
public class Cocktail {
    private int num;

    private String cocktail_name_en;

    private String cocktail_name_kr;

    private String cocktail_ingredient_en;

    private String cocktail_ingredient_kr;

    private String unit;

    private double oz_number;

    private String category;

    private double alcohol;

    private String flavour;
}
