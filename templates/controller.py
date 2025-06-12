VALUE = {
    "path": "src/main/java/{main_package_path}/adapter/in/web/controller",
    "content": """
package {main_package}.adapter.in.web.controller;

import br.com.rd.openapi.api.{prefix}Api;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.RestController;
import lombok.RequiredArgsConstructor;

@RestController
@RequiredArgsConstructor
@Slf4j
public class {prefix}Controller implements {prefix}Api {{
    //TODO implementar métodos
}}"""
}