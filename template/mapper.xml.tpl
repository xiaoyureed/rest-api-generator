<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="{{base_package}}.dao.mapper.{{domain | capitalize}}Mapper">
    <resultMap id="BaseResultMap" type="{{base_package}}.pojo.po.{{domain | capitalize}}">
        {% for item in result_map %}<result column="{{item.column}}" jdbcType="{{item.jdbc_type}}" property="{{item.property}}"/>
        {% endfor %}
        {% for item in result_map_jsonb %}<result column="{{item.column}}" jdbcType="{{item.jdbc_type}}" property="{{item.property}}"
            typeHandler="{{item.type_handler}}"/>
        {% endfor %}
    </resultMap>

    <sql id="Base_Column_List">
    {{base_column_list}}
    </sql>

    <select id="selectByPrimaryKey" parameterType="java.lang.Long" resultMap="BaseResultMap">
        select <include refid="Base_Column_List" />
        from {{table_name}}
        where id = #{id,jdbcType=BIGINT}
    </select>

    <delete id="deleteByPrimaryKey" parameterType="java.lang.Long">
        delete from {{table_name}}
        where id = #{id,jdbcType=BIGINT}
    </delete>

    <insert id="insertSelective" parameterType="{{base_package}}.pojo.po.{{domain | capitalize}}" keyProperty="id" useGeneratedKeys="true">
        insert into {{table_name}}
        <trim prefix="(" suffix=")" suffixOverrides=",">
            {% for item in result_map %}<if test="{{item.property}} != null">
                {{item.column}},
            </if>
            {% endfor %}
            {% for item in result_map_jsonb %}<if test="{{item.property}} != null">
                {{item.column}},
            </if>
            {% endfor %}
        </trim>
        <trim prefix="values (" suffix=")" suffixOverrides=",">
            {% for item in result_map %}<if test="{{item.property}} != null">
                #[{{item.property}},jdbcType={{item.jdbc_type}}],
            </if>
            {% endfor %}
            {% for item in result_map_jsonb %}<if test="{{item.property}} != null">
                #[{{item.property}},jdbcType={{item.jdbc_type}},typeHandler={{item.type_handler}}],
            </if>
            {% endfor %}
        </trim>
    </insert>

    <update id="updateByPrimaryKeySelective" parameterType="{{base_package}}.pojo.po.{{domain | capitalize}}">
        update {{table_name}}
        <set>
            {% for item in result_map %}<if test="{{item.property}} != null">
                {{item.column}} = #[{{item.property}},jdbcType={{item.jdbc_type}}],
            </if>
            {% endfor %}
            {% for item in result_map_jsonb %}<if test="{{item.property}} != null">
                {{item.column}} = #[{{item.property}},jdbcType={{item.jdbc_type}},typeHandler={{item.type_handler}}],
            </if>
            {% endfor %}
        </set>
        where id = #{id,jdbcType=BIGINT}
    </update>
</mapper>