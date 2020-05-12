package {{base_package}}.service.impl;

import {{base_package}}.dao.{{domain}}Dao;
import {{base_package}}.pojo.po.{{domain}};
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@Transactional
public class {{domain}}ServiceImpl {

    @Autowired
    private {{domain}}Dao {{domain}}Dao;

    public Long create({{domain}} record) {
        {{domain}}Dao.insertSelective(record);
        return record.getId();
    }

    public void deleteById(Long id) {
        {{domain}}Dao.deleteByPrimaryKey(id);
    }

    public void update({{domain}} record) {
        {{domain}}Dao.updateByPrimaryKeySelective(record);
    }

    public {{domain}} findById(Long id) {
        return {{domain}}Dao.selectByPrimaryKey(id);
    }
}
