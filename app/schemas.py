from uuid import UUID

from pydantic import BaseModel


class ProductSchema(BaseModel):
    name: str
    description: str


class ProductSchemaIn(ProductSchema):
    pass


class ProductSchemaOut(ProductSchema):
    id: UUID
    updated_at: int
    created_at: int
