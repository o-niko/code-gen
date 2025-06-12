VALUE = {
    "path": "src/main/java/{main_package_path}/adapter/out",
    "content": """
package {main_package}.adapter.out;
import {main_package}.application.port.out.{prefix}Port;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Component;
@Component
@AllArgsConstructor
public class {prefix}Adapter implements {prefix}Port{{
    //TODO implementar métodos
}}"""
}
