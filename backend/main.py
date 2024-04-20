import os
import bcrypt
from fastapi import FastAPI, Form, HTTPException, status
from fastapi.responses import JSONResponse
from utils.models import User
from utils.database import Postgres
from dotenv import load_dotenv

load_dotenv()

# Create an instance of the Postgres class
postgress = Postgres(uri=os.getenv("POSTGRES_URI"),
                     database=os.getenv("POSTGRES_DATABASE"))

# Create instance of FastAPI
app = FastAPI(
    title="FitFlex API",
    description="API for FitFlex, a fitness app.",
    version=os.getenv("API_VERSION"),
    openapi_url='/api/openapi.json',
    docs_url='/api/docs',
    redoc_url='/api/redocs',
)

@app.post("/api/auth/signup")
async def signup(
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    gender: str = Form(...),
    age: int = Form(...),
    weight: float = Form(...),
    height: int = Form(...),
    goal: str = Form(...),
    activity_level: str = Form(...),
):
    """
    Register a new user.

    - **name**: Name of the user
    - **email**: Email address of the user
    - **password**: Password for the user account
    - **gender**: Gender of the user
    - **age**: Age of the user
    - **weight**: Weight of the user
    - **height**: Height of the user
    - **goal**: Fitness goal of the user
    - **activity_level**: Activity level of the user

    Returns:
    - **status**: Status of the registration process
    - **message**: Message indicating the result of the registration process
    """
    try:
        # Create a User instance
        user = User(
            name=name,
            email=email,
            password=password,
            gender=gender,
            age=age,
            weight=weight,
            height=height,
            goal=goal,
            activity_level=activity_level,
        )

        # Check if the user already exists in the database
        postgress.cursor.execute(
            f"SELECT * FROM users WHERE email='{user.email}'")
        if postgress.cursor.fetchone():
            # raise HTTPException(status_code=400, detail="Email already exists.")
            return JSONResponse(content={"status": "error", "message": "Email already exists."}, status_code=status.HTTP_409_CONFLICT)

        # Hash the password with a salt
        user.salt = bcrypt.gensalt()
        user.password_hash = bcrypt.hashpw(
            user.password.encode('utf-8'), user.salt)

        # Insert the user into the database
        postgress.cursor.execute(
            """INSERT INTO users (name, email, password_hash, salt, gender, age, weight, height, goal, activity_level)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (user.name, user.email, user.password_hash, user.salt, user.gender,
             user.age, user.weight, user.height, user.goal, user.activity_level)
        )

        return JSONResponse(content={"status": "success", "message": "User registered successfully."}, status_code=status.HTTP_201_CREATED)

    except ValueError as e:
        # raise HTTPException(status_code=400, detail=str(e))
        return JSONResponse(content={"status": "error", "message": str(User.get_error_message(e))}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/auth/login")
async def login(email: str = Form(...), password: str = Form(...)):
    """Verify a user."""
    try:
        # Create a User instance
        user = User(email=email, password=password)

        # Check if the user exists in the database
        postgress.cursor.execute(f"SELECT * FROM users WHERE email='{email}'")
        user_data = postgress.cursor.fetchone()
        if not user_data:
            # raise HTTPException(status_code=400, detail="User does not exist.")
            return JSONResponse(content={"status": "error", "message": "User does not exist."}, status_code=status.HTTP_404_NOT_FOUND)

        # Dump the user data into the User instance
        user.name, user.email, user.password_hash, user.salt, user.gender, user.age, user.weight, user.height, user.goal, user.activity_level, user.joining_date = user_data

        # Verify the password
        if not bcrypt.hashpw(user.password.encode('utf-8'), user.salt.tobytes()) == user.password_hash.tobytes():
            # raise HTTPException(status_code=400, detail="Invalid password.")
            return JSONResponse(content={"status": "error", "message": "Invalid password."}, status_code=status.HTTP_401_UNAUTHORIZED)
        return JSONResponse(content={"status": "success", "message": f"Welcome back {user.name}", "details": user.model_dump(exclude={'password', 'password_hash', 'salt', 'joining_date'})}, status_code=status.HTTP_200_OK)

    except ValueError as e:
        # raise HTTPException(status_code=400, detail=str(e))
        import traceback
        traceback.print_exc()
        return JSONResponse(content={"status": "error", "message": User.get_error_message(e)}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/auth/reset-password")
async def reset_password(email: str = Form(...), password: str = Form(...)):
    """Reset a user's password."""
    try:
        # Create a User instance
        user = User(email=email, password=password)

        # Check if the user exists in the database
        postgress.cursor.execute(f"SELECT * FROM users WHERE email='{email}'")
        user_data = postgress.cursor.fetchone()
        if not user_data:
            # raise HTTPException(status_code=400, detail="User does not exist.")
            return JSONResponse(content={"status": "error", "message": "User does not exist."}, status_code=status.HTTP_404_NOT_FOUND)

        # Dump the user data into the User instance
        user.name, user.email, user.password_hash, user.salt, user.gender, user.age, user.weight, user.height, user.goal, user.activity_level, user.joinined = user_data

        # Hash the new password with a salt
        user.salt = bcrypt.gensalt()
        user.password_hash = bcrypt.hashpw(
            user.password.encode('utf-8'), user.salt)
        
        # Update the user's password
        postgress.cursor.execute(
            f"UPDATE users SET password_hash='{user.password_hash}', salt='{user.salt}' WHERE email='{user.email}'")
        
        # Return a success message
        return JSONResponse(content={"status": "success", "message": "Password reset successfully."}, status_code=status.HTTP_200_OK)
    
    except ValueError as e:
        # raise HTTPException(status_code=400, detail=str(e))
        return JSONResponse(content={"status": "error", "message": User.get_error_message(e)}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
