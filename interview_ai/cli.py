import json
from typing import Optional

import fitz
from rich import print
from rich.prompt import Prompt
from rich.progress import Progress

import rich_click as click

from interview_ai.client import OpenAIClient
from interview_ai.environments import api_key, model, system, temperature, max_tokens

client = OpenAIClient(api_key, model, system, temperature, max_tokens)

def validate_file_extension(file: str) -> Optional[None]:
    """
    Check if the file is a PDF.
    """
    if not file.lower().endswith('.pdf'):
        raise click.BadParameter("File must be a PDF")

def parse_pdf_to_text(filepath: str) -> str:
    """
    Parse the contents of a PDF file and return the text.
    """
    try:
        with fitz.open(filepath) as pdf_doc:
            text_pages = [page.get_text() for page in pdf_doc]
        return " ".join(text_pages)
    except Exception as e:
        print(f"[bold red]Error extracting text from PDF: {e}")
        click.Abort()

def generate_questions(pdf_text: str, number_of_questions: int, role: str, client: OpenAIClient) -> str:
    """
    Generate interview questions based on the provided PDF text and role.
    """
    try:
        return client.generate_prompt(
            f"Generate {number_of_questions} questions for a {role}, "
            f"based on the following candidate's curriculum: {pdf_text} "
            "return the questions as a json. with the following format: "
            "questions: ['question': 'Question'] "
        )
    except Exception as e:
        print(f"[bold red]Error generating questions: {e}")
        click.Abort()

      
def prompt_questions(questions_json: str) -> list:
    """
    Prompt the user for answers to the generated questions.
    """
    questions_and_answers = []
    try:
        questions_json = json.loads(questions_json)
        cont = 1
        for question_item in questions_json['questions']:
            question = question_item['question']
            answer = Prompt.ask(f"[bold green]🔍 {cont}.[/] {question_item['question']}")
            question_and_answer = {"question": question, "answer": answer}
            questions_and_answers.append(question_and_answer)
            cont += 1
    except Exception as e:
        print(f"[bold red]Error prompting questions: {e}")
        click.Abort()
    return questions_and_answers

@click.command()
@click.argument("file", type=click.Path(exists=True) ,required=True)
@click.option("--role", "-r", required=True, help="Role to generate questions for")
@click.option("--num-questions", "-n", default=5, help="Number of questions to generate")
def cli(file: str, role: str, num_questions: int):
  """
  CLI application to generate interview questions based on a PDF file.
  """
  validate_file_extension(file)
  print("""[bold green]
  ******************************************
  *         Welcome to the OpenAI          *
  *        Interview CLI Application       *
  ******************************************
  [bold green]""")
  
  with Progress() as progress:
    task1 = progress.add_task("[bold green]Parsing the PDF file...", total=1)
    doc = parse_pdf_to_text(file)
    progress.update(task1, advance=1)

  with Progress() as progress:
    task2 = progress.add_task(f"[bold green]Generating {num_questions} questions for {role} role...", total=1)
    questions = generate_questions(doc, num_questions, role, client)
    progress.update(task2, advance=1)

  questions_and_answers = prompt_questions(questions)
  if questions_and_answers:
        print("\n[bold cyan]Questions and Answers:[/]\n")
        for qa in questions_and_answers:
            print(f"[bold yellow]📝 Question:[/] {qa['question']}")
            print(f"[bold blue]✅ Answer:[/] {qa['answer']}\n")

  
if __name__ == "__main__":
    cli()