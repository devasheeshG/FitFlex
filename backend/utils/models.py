from pydantic import BaseModel, field_validator, ValidationError
import re
import datetime

class User(BaseModel):
    name: str = None
    email: str
    password: str
    password_hash: bytes = None
    salt: bytes = None
    gender: str = None
    age: int = None
    weight: float = None
    height: int = None
    goal: str = None
    activity_level: str = None
    joining_date: str = None
    
    @field_validator('name')
    def validate_name(cls, name: str):
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters")
        return name.title()
    
    @field_validator('email')
    def validate_email(cls, email: str):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address")
        return email
    
    @field_validator('password')
    def validate_password(cls, password: str):
        if len(password) < 8:
            raise ValueError("Invalid Password Size must be at least 8 characters")
        return password
    
    @field_validator('gender')
    def validate_gender(cls, gender: str):
        if not gender.title() in ['Male', 'Female']:
            raise ValueError("Gender must be `Male` or `Female`")
        return gender.title()
    
    @field_validator('age')
    def validate_age(cls, age: int):
        if age < 18:
            raise ValueError("Age must be at least 18")
        if age > 80:
            raise ValueError("Age must be at most 80")
        return age
    
    @field_validator('weight')
    def validate_weight(cls, weight: float):
        if weight < 40:
            raise ValueError("Weight must be at least 40 kg")
        if weight > 200:
            raise ValueError("Weight must be at most 200 kg")
        return weight
    
    @field_validator('height')
    def validate_height(cls, height: int):
        if height < 140:
            raise ValueError("Height must be at least 140 cm")
        if height > 220:
            raise ValueError("Height must be at most 220 cm")
        return height
    
    @field_validator('goal')
    def validate_goal(cls, goal: str):
        if not goal.title() in ['Lose Weight', 'Gain Weight', 'Build Muscle', 'Stay Fit', 'Improve Endurance', 'Stay Healthy']:
            raise ValueError("Goal must be `Lose Weight`, `Gain Weight`, `Build Muscle`, `Stay Fit`, `Improve Endurance`, or `Stay Healthy`")
        return goal.title()
    
    @field_validator('activity_level')
    def validate_activity_level(cls, activity_level: str):
        if not activity_level.title() in ['Rookie', 'Beginner', 'Intermediate', 'Advanced', 'Pro']:
            raise ValueError("Activity level must be `Rookie`, `Beginner`, `Intermediate`, `Advanced`, or `Pro`")
        return activity_level.title()

    @field_validator('joining_date')
    def validate_joining_date(cls, joining_date: datetime.datetime):
        if joining_date:
            return joining_date.strftime("%Y-%m-%d")
        else:
            return None
    
    @classmethod
    def get_error_message(cls, exc: ValidationError) -> str:
        for error in exc.errors():
            if error['type'] == 'value_error':
                error_msg = error['msg']
                if error_msg.startswith('Value error, '):
                    return error_msg[len('Value error, '):]
                return error_msg
        return ''