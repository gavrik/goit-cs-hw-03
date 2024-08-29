from pymongo import MongoClient


class Mcrud:
    def __init__(self, conn_string):
        self.client = MongoClient(conn_string)
        self.db = self.client['pets_db']
        self.collection = self.db['pets']

    def create_document(self, document):
        res = self.collection.insert_one(document)
        print("Inserted doc_id: ", res.inserted_id)

    def read_documents(self, query):
        docs = self.collection.find(query)
        for d in docs:
            print(d)

    def update_document(self, query, new_val):
        res = self.collection.update_many(query, {'$set': new_val})
        print("Matched: ", res.matched_count,
              ", Updated: ", res.modified_count)

    def delete_document(self, query):
        res = self.collection.delete_many(query)
        print("Deleted: ", res.deleted_count)

    def get_pet_by_name(self, name):
        self.read_documents({"name": name})

    def update_age_by_name(self, name, age):
        self.update_document({"name": name}, {"are": age})

    def add_feature_by_name(self, name, feature):
        res = self.collection.update_many(
            {"name": name}, {'$push': {"features": feature}})
        print("Matched: ", res.matched_count,
              ", Updated: ", res.modified_count)

    def delete_pet_by_name(self, name):
        self.delete_document({"name": name})


if __name__ == "__main__":
    doc = {"name": "", "age": 0, "features": []}

    pets = Mcrud("mongodb://task:task@192.168.88.211:27017/")

    # Create samples
    new_doc = doc.copy()
    new_doc["name"] = 'cat_1'
    new_doc["age"] = 2
    new_doc["features"] = ["f1", "f2"]
    pets.create_document(new_doc)

    new_doc = doc.copy()
    new_doc["name"] = 'cat_2'
    new_doc["age"] = 3
    new_doc["features"] = ["f1", "f2", "f4"]
    pets.create_document(new_doc)

    new_doc = doc.copy()
    new_doc["name"] = 'cat_4'
    new_doc["age"] = 6
    new_doc["features"] = ["f1", "f2"]
    pets.create_document(new_doc)

    new_doc = doc.copy()
    new_doc["name"] = 'cat_3'
    new_doc["age"] = 5
    new_doc["features"] = ["f1", "f2", "f3"]
    pets.create_document(new_doc)

    # Read documents
    pets.read_documents({})
    print("\n")
    pets.get_pet_by_name("cat_3")

    # Update document
    pets.update_age_by_name("cat_2", 8)
    pets.add_feature_by_name("cat_4", "f8")

    # Delete documents
    pets.delete_pet_by_name('cat_3')
    pets.delete_document({})
