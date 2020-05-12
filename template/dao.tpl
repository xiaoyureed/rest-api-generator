package {{base_package}}.dao;

import {{base_package}}.dao.mapper.{{domain}}Mapper;
import {{base_package}}.pojo.po.{{domain}};
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

@Repository
public class {{domain}}Dao {
    @Autowired
    private {{domain}}Mapper {{domain}}Mapper;

    public {{domain}} selectByPrimaryKey(Long id) {
        return {{domain}}Mapper.selectByPrimaryKey(id);
    }

    public int insertSelective({{domain}} record) {
        return {{domain}}Mapper.insertSelective(record);
    }

    public int deleteByPrimaryKey(Long id) {
        return {{domain}}Mapper.deleteByPrimaryKey(id);
    }

    public int updateByPrimaryKeySelective({{domain}} record) {
        return {{domain}}Mapper.updateByPrimaryKeySelective(record);
    }

}