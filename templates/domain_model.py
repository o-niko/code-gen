VALUE = {
    "path": "src/main/java/{main_package_path}/application/domain/model",
    "content": """
package {main_package}.application.domain.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class {prefix} {{
    //TODO implementar propriedades
}}"""
}
