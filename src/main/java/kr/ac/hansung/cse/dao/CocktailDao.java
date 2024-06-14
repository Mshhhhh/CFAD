package kr.ac.hansung.cse.dao;

import kr.ac.hansung.cse.model.Cocktail;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import javax.sql.DataSource;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

@Repository
public class CocktailDao {

    private JdbcTemplate jdbcTemplate;

    @Autowired
    public void setDataSource(DataSource dataSource) {
        this.jdbcTemplate = new JdbcTemplate(dataSource);
    }

    public int getRowCount() {
        String sqlStatement= "select count(*) from cocktails";
        return jdbcTemplate.queryForObject(sqlStatement, Integer.class);

    }



    //query and return multiple objects
    // cRud method
    public List<Cocktail> getCocktailsBySurvey(int alcohol, int taste) {

        String sqlAlcohol = "(select * from cocktail_data where alcohol between 0 and 15) as c_alcohol";
        String sqlTaste = "(select num from cocktail_data where taste='sweet') as c_taste ON c_alcohol.num = c_taste.num";

        if(alcohol == 0){
            sqlAlcohol = "(select * from cocktail_data where alcohol between 0 and 15) as c_alcohol";
        }
        else if(alcohol == 1){
            sqlAlcohol = "(select * from cocktail_data where alcohol between 15 and 30) as c_alcohol";
        }
        else if(alcohol == 2){
            sqlAlcohol = "(select * from cocktail_data where alcohol between 30 and 60) as c_alcohol";
        }
        else if(alcohol == 3){
            sqlAlcohol = "(select * from cocktail_data) as c_alcohol";
        }

        if(taste == 0){
            sqlTaste = "(select num from cocktail_data where flavour='sweet') as c_taste ON c_alcohol.num = c_taste.num";
        }
        else if(taste == 1){
            sqlTaste = "(select a.num from cocktail_data as a join bitter as b on a.cocktail_name_en = b.cocktail_name_en) as c_taste ON c_alcohol.num = c_taste.num";
        }
        else if(taste == 2){
            sqlTaste = "(select a.num from cocktail_data as a join citrusy as b on a.cocktail_name_en = b.cocktail_name_en) as c_taste ON c_alcohol.num = c_taste.num";
        }
        else if(taste == 3){
            sqlTaste = "(select a.num from cocktail_data as a join sour as b on a.cocktail_name_en = b.cocktail_name_en) as c_taste ON c_alcohol.num = c_taste.num";
        }
        else if(taste == 4){
            sqlTaste = "(select a.num from cocktail_data as a join spicy as b on a.cocktail_name_en = b.cocktail_name_en) as c_taste ON c_alcohol.num = c_taste.num";
        }
        else if(taste == 5){
            sqlTaste = "(select num from cocktail_data) as c_taste ON c_alcohol.num = c_taste.num";
        }

        String sqlStatement= "select * from ( " + sqlAlcohol + " join " + sqlTaste + " ) group by c_alcohol.cocktail_name_en ORDER BY RAND() LIMIT 5";
        return jdbcTemplate.query(sqlStatement, new RowMapper<Cocktail>() {

            @Override
            public Cocktail mapRow(ResultSet rs, int rowNum) throws SQLException {

                Cocktail cocktail= new Cocktail();

                cocktail.setCocktail_name_en(rs.getString("cocktail_name_en"));
                cocktail.setCocktail_name_kr(rs.getString("cocktail_name_kr"));
                cocktail.setCocktail_ingredient_en(rs.getString("cocktail_ingredient_en"));
                cocktail.setCocktail_ingredient_kr(rs.getString("cocktail_ingredient_kr"));
                cocktail.setAlcohol(rs.getDouble("alcohol"));

                return cocktail;
            }
        });
    }

    public List<Cocktail> getCocktailsDetail(String name){

        String sqlStatement= "select * from cocktail_data where cocktail_name_en = '"+ name + "' ";
        return jdbcTemplate.query(sqlStatement, new RowMapper<Cocktail>() {

            @Override
            public Cocktail mapRow(ResultSet rs, int rowNum) throws SQLException {

                Cocktail cocktail= new Cocktail();

                cocktail.setCocktail_name_en(rs.getString("cocktail_name_en"));
                cocktail.setCocktail_name_kr(rs.getString("cocktail_name_kr"));
                cocktail.setCocktail_ingredient_en(rs.getString("cocktail_ingredient_en"));
                cocktail.setCocktail_ingredient_kr(rs.getString("cocktail_ingredient_kr"));
                cocktail.setUnit(rs.getString("unit"));
                cocktail.setOz_number(rs.getDouble("oz_number"));
                cocktail.setCategory(rs.getString("category"));
                cocktail.setAlcohol(rs.getDouble("alcohol"));

                return cocktail;
            }
        });

    }

    public List<Cocktail> getCocktailsByFacial(List<String> face) {


        String sqlStatement= "select * from cocktail_data ORDER BY RAND() LIMIT 5";
        return jdbcTemplate.query(sqlStatement, new RowMapper<Cocktail>() {

            @Override
            public Cocktail mapRow(ResultSet rs, int rowNum) throws SQLException {

                Cocktail cocktail = new Cocktail();

                cocktail.setCocktail_name_en(rs.getString("cocktail_name_en"));
                cocktail.setCocktail_name_kr(rs.getString("cocktail_name_kr"));
                cocktail.setCocktail_ingredient_en(rs.getString("cocktail_ingredient_en"));
                cocktail.setCocktail_ingredient_kr(rs.getString("cocktail_ingredient_kr"));
                cocktail.setAlcohol(rs.getDouble("alcohol"));

                return cocktail;
            }
        });

    }





}
