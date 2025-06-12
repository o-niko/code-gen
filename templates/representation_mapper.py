VALUE = {
        "path": "src/main/java/{main_package_path}/adapter/in/web/mapper",
        "content": """
package br.com.rd.msagstreatmentsupport.adapter.in.web.mapper;
import org.mapstruct.Mapper;
import org.mapstruct.Mapping;

import java.util.List;

@Mapper(componentModel = "spring")
public interface {prefix}RepresentationMapper {{
    //TODO  implementar mappers
}}
"""
    }