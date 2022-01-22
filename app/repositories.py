import time
import uuid
from typing import Dict, Any, Union

from app.schemas import ProductSchemaIn, ProductSchemaOut
from app.tables import ProductTable


class ProductRepository:
    table: ProductTable = ProductTable
    schema_out: ProductSchemaOut = ProductSchemaOut

    @staticmethod
    def _preprocess_create(values: Dict[str, Any]) -> Dict[str, Any]:
        timestamp_now = time.time()
        values["id"] = str(uuid.uuid4())
        values["created_at"] = timestamp_now
        values["updated_at"] = timestamp_now
        return values

    @classmethod
    def create(cls, product_in: ProductSchemaIn) -> ProductSchemaOut:
        data = cls._preprocess_create(product_in.dict())
        model = cls.table(**data)
        model.save()
        return cls.schema_out(**model.attribute_values)

    @classmethod
    def get(cls, entry_id: Union[str, uuid.UUID]) -> ProductSchemaOut:
        model = cls.table.get(str(entry_id))
        return cls.schema_out(**model.attribute_values)
