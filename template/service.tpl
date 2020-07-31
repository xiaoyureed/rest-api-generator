package {{base_package}}.service.impl;

import {{base_package}}.dao.{{domain | capitalize}}Dao;
import {{base_package}}.pojo.po.{{domain | capitalize}};
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@Transactional
public class {{domain | capitalize}}ServiceImpl {

    @Autowired
    private {{domain | capitalize}}Dao {{domain}}Dao;

    public Long create({{domain | capitalize}} record) {
        {{domain}}Dao.insertSelective(record);
        return record.getId();
    }

    public void deleteById(Long id) {
        {{domain}}Dao.deleteByPrimaryKey(id);
    }

    public void update({{domain | capitalize}} record) {
        {{domain}}Dao.updateByPrimaryKeySelective(record);
    }

    public {{domain | capitalize}} findById(Long id) {
        return {{domain}}Dao.selectByPrimaryKey(id);
    }
}
