package {{base_package}}.pojo.po;

{% for ele in full_type_names %}import {{ele}};
{% endfor %}
import lombok.Data;

@Data
public class {{domain | capitalize}} {
    {% for key in col_type_dict %}
    private {{col_type_dict[key]}} {{key}};
    {% endfor %}
}