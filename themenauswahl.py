from random import randint
from os import remove


ORIGINAL_TOPIC_FILE = "themen_original.txt"
TEMP_TOPIC_FILE = "themen_temp.txt"
OUTPUT_FILE = "3 zufaellige Themen.txt"

def draw_topic():
    try:
        with open(TEMP_TOPIC_FILE, "r") as topic_file:
            available_topics = topic_file.readlines()
    except FileNotFoundError:
        with open(ORIGINAL_TOPIC_FILE, "r") as orig_topic_file:
            original_topics = orig_topic_file.readlines()
        with open(TEMP_TOPIC_FILE, "w") as topic_file:
            topic_file.writelines(original_topics)
        available_topics = original_topics
    index = randint(0, len(available_topics)-1)
    topic = available_topics.pop(index)
    if len(available_topics) == 0:
        remove(TEMP_TOPIC_FILE)
    else:
        with open(TEMP_TOPIC_FILE, "w") as topic_file:
            topic_file.writelines(available_topics)
    return topic.strip()


if __name__ == '__main__':
    current_topics = []
    while len(current_topics) < 3:
        topic = draw_topic()
        if topic not in current_topics:
            current_topics.append(topic)
    print("\n".join(current_topics))
    with open(OUTPUT_FILE, 'w') as outfile:
        outfile.writelines("\n".join(current_topics))
