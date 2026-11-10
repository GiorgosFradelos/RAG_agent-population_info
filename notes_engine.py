from llama_index.core.tools import FunctionTool
import os

notes_file = os.path.join("data", "notes.txt")

def save_note(note: str) -> str:
    """
    Saves a text-based note to a file for the user.
    Call this tool only once per note request, then confirm to the user that it has been saved.
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(notes_file), exist_ok=True)

    with open(notes_file, "a") as f:
        f.write(note + "\n")

    return "Note saved successfully."

notes_engine = FunctionTool.from_defaults(
    fn = save_note,
    name = "note_saver",
    description=(
        "Use this tool whenever the user explicitly asks to save, "
        "remember, or write down a note. Pass the exact note content "
        "provided by the user as the note argument. "
        "Call this tool exactly once per note request. "
        "After successful execution, do not call it again. "
        "Tell the user that the note was saved."
    )
)