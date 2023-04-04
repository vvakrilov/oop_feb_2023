from typing import List

from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    categories: list
    topics: list
    documents: List

    def __init__(self):
        self.categories: List = []
        self.topics: List = []
        self.documents: List = []

    @staticmethod
    def return_object_by_id(obj_id, obj_list):
        got_obj = list(o for o in obj_list if o.id == obj_id)
        if got_obj:
            return got_obj[0]

    def add_category(self, category: Category, ):
        if not self.return_object_by_id(category.id, self.categories):
            self.categories.append(category)

    def add_topic(self, topic: Topic, ):
        if not self.return_object_by_id(topic.id, self.topics):
            self.topics.append(topic)

    def add_document(self, document: Document, ):
        if not self.return_object_by_id(document.id, self.documents):
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str, ):
        cat_obj = self.return_object_by_id(category_id, self.categories)
        if cat_obj:
            cat_obj.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str, ):
        topic_obj = self.return_object_by_id(topic_id, self.topics)
        if topic_obj:
            topic_obj.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str, ):
        doc_obj = self.return_object_by_id(document_id, self.documents)
        if doc_obj:
            doc_obj.edit(new_file_name)

    def delete_category(self, category_id: int, ):
        cat = self.return_object_by_id(category_id, self.categories)
        if cat:
            self.categories.remove(cat)

    def delete_topic(self, topic_id: int, ):
        top = self.return_object_by_id(topic_id, self.topics)
        if top:
            self.topics.remove(top)

    def delete_document(self, document_id: int, ):
        doc = self.return_object_by_id(document_id, self.documents)
        if doc:
            self.documents.remove(doc)

    def get_document(self, document_id):
        return self.return_object_by_id(document_id, self.documents)

    def __repr__(self):
        str_repr = '\n'.join(repr(o) for o in self.documents)
        return str_repr

