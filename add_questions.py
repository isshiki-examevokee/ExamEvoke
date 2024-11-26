import os
import csv
import uuid
import django


from admin_panel.questions.model import Question
from admin_panel.subjects.model import Subject
from admin_panel.topics.model import Topic


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'examevoke.settings')
django.setup()


def handle():
    question_paper_directory = '/Users/isshiki/Personal/ExamEvoke/examevoke/question_papers/'  # Set the correct path

    for filename in os.listdir(question_paper_directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(question_paper_directory, filename)
            import_questions_from_csv(file_path)


def import_questions_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            create_question_from_row(row)


def create_question_from_row(row):
    subject, _ = Subject.objects.get_or_create(name=row['Subject'])
    topic, _ = Topic.objects.get_or_create(name=row['Topic'])

    options = {
        "Option1": row['Option1'],
        "Option2": row['Option2'],
        "Option3": row['Option3'],
        "Option4": row['Option4'],
        "Option5": row['Option5'],
        "Option6": row['Option6'],
    }
    # Filter out any empty options
    options = {k: v for k, v in options.items() if v}

    question = Question(
        id=uuid.uuid4(),
        text=row['Question'],
        subject=subject,
        topic=topic,
        type=row['Question Type'],
        language=row.get('Language', 'English'),
        difficulty=row['Difficulty Level'],
        solution=row.get('Solution', ''),
        options=options,
        answer={"correct": row['Answer']} if row['Answer'] else None,
    )

    question.save()


if __name__ == "__main__":
    handle()
