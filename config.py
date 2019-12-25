import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

write_head = True

node_count = 10000
rel_count = node_count * 17

paper_count = int(node_count * 0.65)
person_count = int(node_count * 0.33)
org_count = int(node_count * 0.0017)
topic_count = int(node_count * 0.0183)
be_cited_count = int(rel_count * 0.06)
paper_belong_topic_count = int(rel_count * 0.32)
person_belong_topic_count = int(rel_count * 0.1)
person_citation_count = int(rel_count * 0.26)
person_publication_count = int(rel_count * 0.15)
related_to_count = int(rel_count * 0.015)
topic_belong_topic_count = int(rel_count * 0.003)
work_for_count = int(rel_count * 0.015)
write_paper_count = int(rel_count * 0.077)

paper_csv_path = os.path.join(BASE_DIR, "output", "data_paper.csv")
paper_ids_path = os.path.join(BASE_DIR, "output", "data_paper_ids.bin")

person_csv_path = os.path.join(BASE_DIR, "output", "data_person.csv")
person_ids_path = os.path.join(BASE_DIR, "output", "data_person_ids.bin")

org_csv_path = os.path.join(BASE_DIR, "output", "data_org.csv")
org_ids_path = os.path.join(BASE_DIR, "output", "data_org_ids.bin")

topic_csv_path = os.path.join(BASE_DIR, "output", "data_topic.csv")
topic_ids_path = os.path.join(BASE_DIR, "output", "data_topic_ids.bin")

citations_csv_path = os.path.join(BASE_DIR, "output", "data_citations.csv")
publications_csv_path = os.path.join(BASE_DIR, "output", "data_publications.csv")


be_cited_csv_path = os.path.join(BASE_DIR, "output", "rel_be_cited.csv")

paper_belong_topic_csv_path = os.path.join(
    BASE_DIR, "output", "rel_paper_belong_topic.csv")

person_belong_topic_csv_path = os.path.join(
    BASE_DIR, "output", "rel_person_belong_topic.csv")

person_citation_csv_path = os.path.join(
    BASE_DIR, "output", "rel_person_citation.csv")

person_publication_csv_path = os.path.join(
    BASE_DIR, "output", "rel_person_publication.csv")

related_to_csv_path = os.path.join(
    BASE_DIR, "output", "rel_related_to.csv")

topic_belong_topic_csv_path = os.path.join(
    BASE_DIR, "output", "rel_topic_belong_topic.csv")

work_for_csv_path = os.path.join(
    BASE_DIR, "output", "rel_work_for.csv")

write_paper_csv_path = os.path.join(
    BASE_DIR, "output", "rel_write_paper.csv")
