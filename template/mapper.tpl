package {{base_package}}.dao.mapper;

import {{base_package}}.pojo.po.{{domain}};
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface {{domain}}Mapper {
    int insertSelective({{domain}} record);

    int deleteByPrimaryKey(Long id);

    int updateByPrimaryKeySelective({{domain}} record);

    {{domain}} selectByPrimaryKey(Long id);
}