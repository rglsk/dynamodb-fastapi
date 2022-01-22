resource "aws_dynamodb_table" "product-table" {
  name           = "ProductTable"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "id"

  attribute {
    name = "id"
    type = "S"
  }

  attribute {
    name = "name"
    type = "N"
  }


  attribute {
    name = "updated_at"
    type = "N"
  }

  ttl {
    attribute_name = "TimeToExist"
    enabled        = false
  }

  global_secondary_index {
    name               = "product-name-index"
    hash_key           = "name"
    range_key          = "created_at"
    write_capacity     = 10
    read_capacity      = 10
    projection_type    = "INCLUDE"
    non_key_attributes = ["id"]
  }

  tags = {
    Name        = "product-table"
    Environment = "production"
  }
}