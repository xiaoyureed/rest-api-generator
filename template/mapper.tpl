package {{base_package}}.dao.mapper;

import {{base_package}}.pojo.po.{{domain | capitalize}};
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface {{domain | capitalize}}Mapper {
    int insertSelective({{domain | capitalize}} record);

    int deleteByPrimaryKey(Long id);

    int updateByPrimaryKeySelective({{domain | capitalize}} record);

    {{domain | capitalize}} selectByPrimaryKey(Long id);
}