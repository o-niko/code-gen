VALUE = {
    "path": "src/main/java/{main_package_path}/adapter/out/persistence/model",
    "content": """
package {main_package}.adapter.out.persistence.model;

import lombok.Data;
import org.springframework.data.mongodb.core.mapping.Document;
import jakarta.persistence.Id;

@Data
@Document(collection = "{prefix}")
public class {prefix}Entity {{
    @Id
    private String id;
    //TODO implementar outras propriedades
}}"""
}
