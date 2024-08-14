import re, os
from pymilvus import MilvusClient, model, CollectionSchema, FieldSchema, DataType
from utils.image import get_image_vector

db = MilvusClient('database/images.db')

if db.has_collection(collection_name="image") == False:
  fields = [
     FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
     FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=512),
    #  FieldSchema(name="tag_vector", dtype=DataType.FLOAT_VECTOR, dim=512),
    #  FieldSchema(name="tag", dtype=DataType.VARCHAR, max_length=256),
     FieldSchema(name="path", dtype=DataType.VARCHAR, max_length=256)
  ]

  schema = CollectionSchema(fields=fields)

  db.create_collection(
      collection_name="image",
      schema=schema
  )

  index_params = db.prepare_index_params()

  index_params.add_index(field_name="vector", metric_type="COSINE", index_type="FLAT", params={ "nlist": 128 })

  db.create_index(collection_name="image", index_params=index_params)

async def insert_image(dir):
  pattern = re.compile(r'jpg$', re.IGNORECASE)

  images = [f"{dir}/{path}" for path in os.listdir(dir) if pattern.search(path)]

  print(images)

  data = [
    {
      "path": image_path,
      "vector": get_image_vector(image_path),
      # "tag_vector": None,
      # "tag": None
    }
    for image_path in images
  ]

  db.insert(collection_name="image", data=data)

def search_image(keyword):
   return db.search(collection_name="image", data=keyword, output_fields=['path'], search_params={"metric_type": "COSINE", "params": {}})
