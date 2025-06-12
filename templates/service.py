VALUE = {
        "path": "src/main/java/{main_package_path}/service",
        "content": """
package {main_package}.application.domain.service;

import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@AllArgsConstructor
public class {prefix}Service implements {prefix}UseCase {{
    //TODO implementar métodos
}}"""
    }