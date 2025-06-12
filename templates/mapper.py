VALUE = {
        "path": "src/main/java/{main_package_path}/adapter/out/mapping",
        "content": """
package {main_package}.application.domain.mapper;

import org.mapstruct.Mapper;

@Mapper(componentModel = "spring")
public interface {prefix}Mapper {{
    //TODO implementar mappers
}}"""
    }