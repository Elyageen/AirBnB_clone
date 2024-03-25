from models.base_model import BaseModel


# This class inherits from the BaseModel class.
class User(BaseModel):
    """User class that inherits from BaseModel."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        The above function is a Python constructor method that initializes an object with optional arguments
        passed as positional or keyword arguments.
        """
        """Initializes User."""
        super().__init__(*args, **kwargs)
