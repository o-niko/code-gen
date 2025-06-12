VALUE = {
        "path": "src/main/java/{main_package_path}/adapter/out/persistence/repository",
        "content": """
package {main_package}.adapter.out.persistence.repository;

import org.springframework.stereotype.Repository;
import org.springframework.data.mongodb.repository.MongoRepository;
import {main_package}.adapter.out.persistence.model.{prefix}Entity;

@Repository
public interface {prefix}Repository extends MongoRepository<{prefix}Entity, String> {{
    //TODO implementar métodos
}}"""
    }