from datetime import date

from ninja import Schema


class BaseSchema(Schema):
    id: int


class BaseOutSchema(BaseSchema):
    created_at: date
    updated_at: date


class BaseInSchema(BaseSchema):
    pass
