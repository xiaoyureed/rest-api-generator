package {{base_package}}.dao;

import {{base_package}}.dao.mapper.{{domain | capitalize}}Mapper;
import {{base_package}}.pojo.po.{{domain | capitalize}};
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

@Repository
public class {{domain | capitalize}}Dao {
    @Autowired
    private {{domain | capitalize}}Mapper {{domain}}Mapper;

    public {{domain | capitalize}} selectByPrimaryKey(Long id) {
        return {{domain}}Mapper.selectByPrimaryKey(id);
    }

    public int insertSelective({{domain | capitalize}} record) {
        return {{domain}}Mapper.insertSelective(record);
    }

    public int deleteByPrimaryKey(Long id) {
        return {{domain}}Mapper.deleteByPrimaryKey(id);
    }

    public int updateByPrimaryKeySelective({{domain | capitalize}} record) {
        return {{domain}}Mapper.updateByPrimaryKeySelective(record);
    }

}